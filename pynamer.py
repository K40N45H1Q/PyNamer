from sys import argv, exit
from random import choices
from os import listdir, path, rename
from string import ascii_letters, digits

class PyNamer:
    def __init__(self):
        self.directory = None
        self.filename = path.basename(__file__)
        self.options = {
            "-r": self.random_mode(),
            "--random": self.random_mode(),
            "-n": self.numbers_mode(),
            "--numbers": self.numbers_mode()
        }

    def show_help(self):
        print(f"Usage: {self.filename} /path/to/directory [--random, -r] or [--numbers, -n]")

    def numbers_mode(self):
        files = [
            f for f in listdir(self.directory)
            if path.isfile(
                path.join(self.directory, f)) and path.realpath(path.join(self.directory, f)) != self.filename
        ]
        for number, file in enumerate(files, start=1):
            extension = path.splitext(file)[1]
            filename = f"{number}{extension}"
            rename(path.join(self.directory, file), path.join(self.directory, filename))

    def random_mode(self):
        files = [
            file for file in listdir(self.directory)
            if path.isfile(
                path.join(self.directory, file)) and path.realpath(path.join(self.directory, file)) != self.filename
        ]
        for file in files:
            extension = path.splitext(file)[1]
            filename = "".join(choices(ascii_letters + digits, k=9)) + extension
            rename(path.join(self.directory, file), path.join(self.directory, filename))

    def main(self):
        if len(argv) < 3:
            self.show_help(); exit(1)
        self.directory = argv[1]
        if not path.isdir(self.directory):
            print("Directory does not exist!"); exit(1)
        function = self.options.get(argv[2])
        if function:
            function()
            print("File names changed successfully!")
        else:
            self.show_help(); exit(1)

if __name__ == "__main__":
    PyNamer().main()
