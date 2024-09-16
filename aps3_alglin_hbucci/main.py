import my_lib
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
    my_lib.run()
    script_path = Path(os.path.abspath(__file__))
    print("Script path:", script_path)

if __name__ == "__main__":
    app()