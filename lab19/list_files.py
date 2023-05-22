import os
import re
from rich.console import Console
from rich.table import Table

console = Console()


def list_files(file_path, pattern):

    files = os.listdir(file_path)
    matches = [file for file in files if re.search(pattern, file)]
    table = Table(title=f"Files in [green]{file_path}[/green] ending in [green]{pattern}[/green].")
    table.add_column("File Name", style="dim")
    for match in matches:
        table.add_row(f"{matches.index(match) + 1}.{match}")
    console.print(table)



# list_files("./users/user1", ".log")
# list_files("./users/user1", ".txt")
# list_files("./users/user1", ".mail")

