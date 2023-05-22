from create_folder import create_folder
from handle_delete import handle_delete
from handle_sort import handle_sort
from parse import parse
from list_files import list_files
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os


def main():

    directory = ["Create a Directory", "Delete a Directory", "Sort a Directory", "Parse a file", "List Directory Files"]

    def list_directory():
        table.add_column("[green]Option List[/green]", style="bold")
        for selection in directory:
            table.add_row(f"{directory.index(selection) + 1}.{selection} ")
        console.print(table)

    list_directory()

    while True:
        user_selection = Prompt.ask("\nPlease select an option")
        if not user_selection.isnumeric() or int(user_selection) > len(directory):
            console.print("\n[red]Invalid Selection![/red]")
        elif user_selection == "1":
            file_path = Prompt.ask("Please enter the file path")
            directory_name = Prompt.ask("Please enter the name of the directory")
            directory_path = os.path.join(file_path, directory_name)
            create_folder(directory_path)
            break
        elif user_selection == "2":
            pass
        elif user_selection == "3":
            pass
        elif user_selection == "4":
            pass
        elif user_selection == "5":
            pass

        else:
            break




    console.print(f"You have selected {directory[int(user_selection) - 1]}")


if __name__ == "__main__":
    console = Console()
    table = Table(title="\n")
    main()

