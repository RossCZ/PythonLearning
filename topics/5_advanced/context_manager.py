from pathlib import Path


# with context
temp_file = Path("test.txt")
with open(temp_file, "w") as f:
    f.write("Hello!")
temp_file.unlink()


# as class - e.g. manages connection to a database
class FileManager:
    def __init__(self, file_path):
        print("init")
        self.file_path = Path(file_path)
        self.file = open(self.file_path, "w")

    def __enter__(self):
        print("enter")
        return self.file  # returns the underlying object

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit")
        self.file.close()
        self.file_path.unlink()  # cleanup


with FileManager("test_file.txt") as f:
    f.write("Ola!")  # calls method on the underlying object
