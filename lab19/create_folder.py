from rich.console import Console
import os

console = Console()


def create_folder(folder_name):
    os.mkdir(folder_name)
    console.print(f"[green]Directory {folder_name} created successfully![/green]")
