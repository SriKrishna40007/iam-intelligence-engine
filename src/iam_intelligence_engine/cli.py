import typer
from rich.console import Console

console = Console()

app = typer.Typer(
    help="IAM Intelligence Engine"
)


@app.callback()
def main() -> None:
    """
    IAM Intelligence Engine CLI.
    """
    pass


@app.command()
def version() -> None:
    """
    Display application version.
    """
    console.print("[bold green]IAM Intelligence Engine[/bold green]")
    console.print("Version: 0.1.0")