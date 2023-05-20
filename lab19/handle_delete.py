import os
import shutil
from create_folder import create_folder


def handle_delete(user):
    dst_folder = "temporary"

    if not os.path.exists(dst_folder):
        create_folder(dst_folder)

    for file_name in os.listdir(f"./users/{user}"):
        file_path = os.path.join(f"./users/{user}", file_name)
        shutil.move(file_path, dst_folder)


# handle_delete("user1")
