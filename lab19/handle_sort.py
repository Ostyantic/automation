import shutil
import os
from create_folder import create_folder


def handle_sort(file_path):

    mail_folder = os.path.join(f"{file_path}", "mail")
    doc_folder = os.path.join(f"{file_path}", "documents")
    logs_folder = os.path.join(f"{file_path}", "logs")

    if not os.path.exists(mail_folder):
        create_folder(mail_folder)
    if not os.path.exists(doc_folder):
        create_folder(doc_folder)
    if not os.path.exists(logs_folder):
        create_folder(logs_folder)

    for file in os.listdir(file_path):
        new_file_path = os.path.join(file_path, file)
        if ".txt" in file:
            shutil.move(new_file_path, doc_folder)
        if ".mail" in file:
            shutil.move(new_file_path, mail_folder)
        if ".log" in file:
            shutil.move(new_file_path, logs_folder)


handle_sort("./temporary")
