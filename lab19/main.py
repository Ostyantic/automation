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
        user_selection = Prompt.ask("\nPlease select an option. 'q' to quit.")

        if user_selection == "q":
            break
        elif not user_selection.isnumeric() or int(user_selection) > len(directory):
            console.print("\n[red]Invalid Selection![/red]")
        elif user_selection == "1":
            try:
                file_path = Prompt.ask("Please enter the file path")
                directory_name = Prompt.ask("Please enter the name of the directory")
                directory_path = os.path.join(file_path, directory_name)
                create_folder(directory_path)
            except FileExistsError:
                console.print(f"[red]Directory {directory_name} already exists![/red]")
            console.print(f"[green]Directory {directory_name} created successfully!")
        elif user_selection == "2":
            file_path = Prompt.ask("Please enter the file path")
            directory_name = Prompt.ask("Please enter the name of the directory you would like to delete")
            directory_path = os.path.join(file_path, directory_name)
            handle_delete(directory_path)
        elif user_selection == "3":
            file_path = Prompt.ask("Please enter the file path")
            handle_sort(file_path)
        elif user_selection == "4":
            file_path = Prompt.ask("Please enter the file path")
            file_name = Prompt.ask("Please enter the name of the file you would like to parse")
            directory_path = os.path.join(file_path, file_name)
            parse(directory_path)
        elif user_selection == "5":
            file_path = Prompt.ask("Please enter a file path")
            pattern = Prompt.ask("Please enter the file extension")
            list_files(file_path, pattern)


if __name__ == "__main__":
    console = Console()
    table = Table(title="\n")
    main()

