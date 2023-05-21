import os
import shutil
import re


def parse(file_path):

    # cdir = os.getcwd()

    warnings_file = os.path.join(os.path.dirname(file_path), "warnings.log")
    errors_file = os.path.join(os.path.dirname(file_path), "errors.log")

    with open(file_path, 'r') as file:
        text = file.read()

    warning_matches = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, WARNING:.*", text)
    error_matches = re.findall(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}, ERROR: .*", text)

    with open(warnings_file, 'w') as file:
        for warning_match in warning_matches:
            file.write(warning_match + "\n")
    with open(errors_file, 'w') as file:
        for error_match in error_matches:
            file.write(error_match + "\n")

    # print(cdir)
    # print(warnings_file)
    # print(errors_file)

# parse("./temporary/logs/log1.log")
