import os
import time
import subprocess as sp
from datetime import datetime


class FileProcessor:
    def __init__(self, targeted_path, file_name, program_name):
        self.targeted_path = targeted_path
        self.file_name = file_name
        self.program_name = program_name

    def process_files(self):
        """Process the files in the targeted directory and write results to a file."""
        try:
            with open(f"{self.file_name}.txt", "a") as output_file:
                for file_name in os.listdir(self.targeted_path):
                    # Check file extension and write to output file accordingly
                    if file_name.endswith(".xmodel_export"):
                        line = f"precachemodel(\"{file_name.split('.')[0]}\");\n"
                        output_file.write(line)
                        print(line.strip())

                    elif file_name.endswith(".json"):
                        line = f"precacheitem(\"{file_name.split('.')[0]}\");\n"
                        output_file.write(line)
                        print(line.strip())

            # Open the output file in the specified program
            sp.Popen([self.program_name, f"{self.file_name}.txt"])
            print("Finished!...")

        except Exception as e:
            print(f"An error occurred: {e}")


def main():
    targeted_path = input("Go ahead Alpha!: ")
    print("Your Path is: " + targeted_path)

    file_name = input("Precache file name: ")
    print("Your precache file name is: " + file_name)

    program_name = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"

    processor = FileProcessor(targeted_path, file_name, program_name)
    processor.process_files()

    # Optional: add a delay to keep the console open
    time.sleep(3)


if __name__ == "__main__":
    main()
