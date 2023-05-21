import os
import shutil
from create_folder import create_folder


def handle_delete(file_path):
    dst_folder = "temporary"

    if not os.path.exists(dst_folder):
        create_folder(dst_folder)

    for file_name in os.listdir(file_path):
        new_file_path = os.path.join(file_path, file_name)
        shutil.move(new_file_path, dst_folder)


handle_delete("./users/user1")
handle_delete("./users/user2")

