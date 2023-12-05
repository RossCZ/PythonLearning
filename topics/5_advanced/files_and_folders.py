import os
from pathlib import Path
import pandas as pd


def os_options():
    # https://www.geeksforgeeks.org/os-module-python-examples/
    # join path
    for root, dirs, files in os.walk(os.getcwd()):  # walk recursively all files/folders in CWD
        print(root)
        print(dirs)

    print(os.path.join("Output", "file.txt"))

    # path exist
    print(os.path.exists("Data"))

    # make directory
    # os.mkdir("Output")

    # other useful options
    # rename a file
    # os.rename("old_file.txt", "new_file.txt")

    # remove a file
    # os.remove("file.txt")

    # remove empty directory
    # os.rmdir("directory")


def os_example():
    df = pd.read_csv(os.path.join("../../data", "portfolio_data.csv"))
    foldername = "output"
    filename = "BTC_df.csv"
    if not os.path.exists(foldername):
        os.mkdir(foldername)

        # Pandas - save series/dataframe to csv
        df["BTC"].to_csv(os.path.join(foldername, filename), sep=";")


def file_handling():
    # https://www.w3schools.com/python/python_file_open.asp
    # https://www.w3schools.com/python/python_file_write.asp

    # create an empty file
    f = open("my_file.txt", "x")

    # write to a file
    f = open("my_file.txt", "w")
    f.write("Hello world")
    f.close()

    # open and read a file
    f = open("my_file.txt", "r")
    print(f.read())


def pathlib_options():
    # path object
    cwd = Path.cwd()
    py_files = cwd.glob("*.py")
    subfolders = [f for f in cwd.rglob("*") if f.is_dir()]  # rglob: recursively
    print(f"{len(list(py_files))} python files in CWD")
    print(f"{len(subfolders)} subfolders in CWD")

    file = Path("output", "file.txt")  # create path from arbitrary number of components
    folder = Path("output")

    # file/folder (path) exists
    print("exists:", file.exists(), folder.exists())

    # create a directory
    folder.mkdir()
    # Path("output", "data", "test").mkdir(parents=True, exist_ok=True)  # exist_ok=False: error if the target directory exists

    # create a file
    with file.open("w") as f:
        f.write("hello")

    # check type
    print("is file:", file.is_file(), folder.is_file())
    print("is dir:", file.is_dir(), folder.is_dir())

    # rename/move a file
    new_file = Path("output", "my_file.txt")
    file.rename(new_file)

    # remove a file
    new_file.unlink()

    # remove an empty directory
    folder.rmdir()  # or unlink but rmdir is recommended for dirs


def pathlib_example():
    df = pd.read_csv(os.path.join("../../data", "portfolio_data.csv"))
    outfolder = Path("output")
    outfile = Path(outfolder, "BTC_df.csv")
    if not outfolder.exists():
        outfolder.mkdir()

        # Pandas - save series/dataframe to csv
        df["BTC"].to_csv(outfile, sep=";")

    # cleanup
    outfile.unlink()
    outfolder.rmdir()


if __name__ == "__main__":
    # old
    # os_options()
    # os_example()
    # file_handling()

    # pathlib: modern solution
    pathlib_options()
    # pathlib_example()
