from rich.console import Console
import os

console = Console()


def create_folder(folder_name):
    # try:
    os.mkdir(folder_name)
    # console.print(f"[green]Directory {folder_name} created successfully![/green]")
    # except FileExistsError:
    #     console.print(f"[red]Directory {folder_name} already exists![/red]")

# create_folder("./deleted/test1")