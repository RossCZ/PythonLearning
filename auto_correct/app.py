import os
from importlib import import_module
from pathlib import Path
from dataclasses import dataclass
import numpy as np
import pandas as pd
from enum import Enum
from inspect import signature


@dataclass
class Test:
    input_args: tuple
    expected_output: float


class EvaluationResult(Enum):
    OK = "OK"
    MODULE_ERROR = "module"
    MISSING_METHOD = "method"
    EXCEPTION = "except"
    INCORRECT_INTERFACE = "interface"
    WRONG_RESULT_TYPE = "result-type"
    WRONG_RESULT_VALUE = "result-value"


class AutoCorrector:
    def __init__(self, source_dir_name, method_name, tests):
        self.source_dir_name = source_dir_name
        self.method_name = method_name
        self.tests = tests

    def get_files(self):
        files = []
        for file in os.listdir(self.source_dir_name):
            if file.endswith(".py"):
                files.append(Path(file).stem)
        return files

    def evaluate_test(self, test, module_name):
        try:
            module = import_module(module_name)
        except:
            return EvaluationResult.MODULE_ERROR

        try:
            method = getattr(module, self.method_name)
        except AttributeError:
            return EvaluationResult.MISSING_METHOD

        try:
            result = method(*test.input_args)
        except Exception as e:
            # print(module, e)  # debug

            # test method interface
            params = signature(method).parameters
            if ("args" not in params.keys()) and ("kwargs" not in params.keys()) and (len(params) != len(test.input_args)):
                return EvaluationResult.INCORRECT_INTERFACE

            # general exception within method
            return EvaluationResult.EXCEPTION

        # expecting numerical result only
        try:
            result = float(result)
            same = np.isclose(result, test.expected_output)
            if not same:
                return EvaluationResult.WRONG_RESULT_VALUE
            else:
                return EvaluationResult.OK
        except:
            return EvaluationResult.WRONG_RESULT_TYPE

    def evaluate_file(self, file):
        module_name = f"{self.source_dir_name}.{file}"
        evaluation_result = [self.evaluate_test(test, module_name).value for test in self.tests]
        return evaluation_result

    def evaluate_files(self, files):
        evaluation_result = {}
        for file in files:
            evaluation_result[file] = self.evaluate_file(file)

        df = pd.DataFrame.from_dict(evaluation_result, orient="index").transpose()
        df.index.name = "test"
        return df

    def evaluate(self):
        files = self.get_files()
        res = self.evaluate_files(files)
        pd.set_option("display.max_columns", None)
        pd.set_option("display.max_rows", None)
        print(res)


if __name__ == "__main__":
    t = [
        Test((4.0, 2.0), 2.0),
        Test((3.0, 2.0), 1.5),
        Test((0.0, 2.0), 0.0),
    ]
    AutoCorrector(source_dir_name="handed", method_name="divide", tests=t).evaluate()
