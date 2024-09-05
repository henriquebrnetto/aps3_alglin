import aps3_alglin_hbucci
import os
from pathlib import Path
from rich.console import Console
import typer

app = typer.Typer()
console = Console()

@app.command('info')
def print_info(custom_message : str = ""):
    """
    Print information about the module
    """
    console.print("Hello! I am aps3_alglin_hbucci")
    console.print(f"Author: aps3_alglin_hbucci.__author__")
    console.print(f"Version: aps3_alglin_hbucci.__version__")
    if custom_message != "":
        console.print(f"Custom message: {custom_message}")

@app.command()
def demo():
    print("Hello world!")
    aps3_alglin_hbucci.my_function()
    script_path = Path(os.path.abspath(__file__))
    parent_path = script_path.parent
    print("Script path:", script_path)
    with open(parent_path / "assets/poetry.txt") as f:
        print(f.read())
    with open(parent_path / "assets/test_folder/test_something.txt") as f:
        print(f.read())

if __name__ == "__main__":
    app()