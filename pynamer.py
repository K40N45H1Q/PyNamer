from sys import argv
from random import choices
from string import ascii_letters, digits
from os import listdir, path, rename, system, name

class PyNamer:
    def __init__(self):
        self.directory = None
        self.filename = path.basename(__file__)

    def show_help(self):
        system("cls" if name == "nt" else "clear")
        print(f"Usage: {self.filename} /path/to/dir --random or --numbers\n")

    def random_mode(self):
        files = [
            f for f in listdir(self.directory)
            if path.isfile(path.join(self.directory, f)) and f != self.filename
        ]
        for f in files:
            extension = path.splitext(f)[1]
            filename = "".join(choices(ascii_letters + digits, k=9)) + extension
            rename(path.join(self.directory, f), path.join(self.directory, filename))

    def numbers_mode(self):
        files = [
            f for f in listdir(self.directory)
            if path.isfile(path.join(self.directory, f)) and f != self.filename
        ]
        for i, f in enumerate(files, start=1):
            extension = path.splitext(f)[1]
            filename = f"{i}{extension}"
            rename(path.join(self.directory, f), path.join(self.directory, filename))

    def main(self):
        if len(argv) < 3:
            self.show_help(); exit(1)
        self.directory = argv[1]
        if argv[2] in ["-r", "--random"]:
            self.random_mode()
        elif argv[2] in ["-n", "--numbers"]:
            self.numbers_mode()
        else:
            self.show_help(); exit(1)

if __name__ == "__main__":
    PyNamer().main()
