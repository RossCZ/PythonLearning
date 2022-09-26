import pytest


# tested code - usually in different file
class DataLoader:
    def __init__(self, n):
        self.data = [num + 1 for num in range(n)]

    def get_len(self):
        return len(self.data)

    def get_item(self, i):
        return self.data[i]

    def delete_item(self, i):
        self.data.pop(i)


# pytest fixture code - data
@pytest.fixture
def dataloader():
    return DataLoader(10)


# tests (test_...)
def test_dataloader(dataloader):
    # assert False/True
    assert dataloader.get_len() == 10
    assert dataloader.get_item(0) == 1


def test_delete_item(dataloader):
    dataloader.delete_item(3)
    assert dataloader.get_len() == 9


def test_to_fail(dataloader):
    # assert dataloader.get_len() == 1  # assert False
    dataloader.get_item(42)  # raised exception


# set configuration as Python tests in PyCharm
# https://www.jetbrains.com/help/pycharm/pytest.html
# run test separately or run whole test module
