def function(param1: int, param2: dict[int, int]) -> (str, list[float]):
    """Example function.

    Detailed description of the example function.

    Args:
        param1 (int): The first parameter.
        param2 (dict[int, int]): The second parameter.

    Returns:
        (str, list[float]): Return value.
    """
    return "hello", [i for i in range(param2[param1])]


# input and output variables
in1 = 1
in2 = {
    1: 2,
    2: 4,
    3: 8,
    4: 16,
    5: 32,
}
res = function(in1, in2)
print(type(in1))
print(type(in2))
print(type(res))
