from sys import exit
from os.path import getsize
import argparse


class ArgumentHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.switches = []  # carrying data about the switches (flags)
        self.parser.add_argument("-c", "--bytes", help="Print only the byte counts.", action="store_true")
        self.parser.add_argument("-m", "--chars", help="Print only the character counts.", action="store_true")
        self.parser.add_argument("-w", "--words", help="Print only the word counts.", action="store_true")
        self.parser.add_argument("-l", "--lines", help="Print only the newline counts.", action="store_true")
        self.parser.add_argument("-L", "--max-line-length", help="Print the maximum display width.", action="store_true")
        self.parser.add_argument("--version", help="Output version information and exit.", action="store_true")

        self.parser.add_argument("file", help="Path to the file.", type=str)

        self.args = self.parser.parse_args()
        self.response_handler()

    def get_switches(self):  # return switches (flags)
        return self.switches

    def get_file(self):
        return self.args.file

    def response_handler(self):
        """
        it must be stored in the right order (newline, word, character, byte, max line length)
        """
        if self.args.lines:
            self.switches.append("l")
        if self.args.words:
            self.switches.append("w")
        if self.args.chars:
            self.switches.append("m")
        if self.args.bytes:
            self.switches.append("c")
        if self.args.max_line_length:
            self.switches.append("L")
        if self.args.version:
            print("version 1.0, written by Gasper Hribar")
            exit()
        if self.args.file:
            self.validate_file(self.args.file)

    def validate_file(self, file):
        try:
            data = open(file, "r")
            data.close()
        except FileNotFoundError:
            print("No such file:  " + file)
            exit()
        except IsADirectoryError:
            print("Not a directory:  " + file)
            exit()
        except PermissionError:
            print("Permission denied:  " + file)
            exit()


class ProcessFile:
    def __init__(self, file, switches):
        self.content = self.get_file_content(file)  # file is ok for processing
        self.file = file
        self.switches = switches

    def get_file_content(self, source):
        file = open(source, "r", encoding="utf-8")  # file is already validated. Check function "validate_file" for details
        text = file.read()
        file.close()
        return text

    def process(self):
        output = ""
        for switch in self.switches:
            if switch == "l":
                output += str(self.count_lines())
            if switch == "w":
                output += str(self.count_words())
            if switch == "m":
                output += str(self.count_chars())
            if switch == "c":
                output += str(self.count_bytes())
            if switch == "L":
                output += str(self.count_max_line_length())
            output += " "
        print(output + self.file)

    def count_lines(self):
        return len(self.content.split("\n")) - 1

    def count_chars(self):
        return len(list(self.content)) + self.count_lines()  # "\n" is considered as one char, that is why adding

    def count_words(self):
        return len(self.content.split())

    def count_bytes(self):
        return getsize(self.file)

    def count_max_line_length(self):
        if len(self.content.split("\n")) == 0:
            return 0
        return len(max(self.content.split("\n"), key=len))


def main():
    argumentHandler = ArgumentHandler()
    ProcessFile(argumentHandler.get_file(), argumentHandler.get_switches()).process()


if __name__ == "__main__":
    main()
