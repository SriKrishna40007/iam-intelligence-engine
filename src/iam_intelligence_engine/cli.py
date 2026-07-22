from pathlib import Path

import typer
from rich.console import Console

from iam_intelligence_engine.application.analysis_service import AnalysisService
from iam_intelligence_engine.presentation.cli_formatter import CLIFormatter
from iam_intelligence_engine.presentation.json_report_writer import JsonReportWriter
from iam_intelligence_engine.presentation.output_format import OutputFormat
from iam_intelligence_engine.presentation.sarif_report_writer import (
    SarifReportWriter,
)

console = Console()

app = typer.Typer(
    help="IAM Intelligence Engine",
    no_args_is_help=True,
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


@app.command()
def scan(
    policy_file: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        help="Path to IAM policy JSON file.",
    ),
    output: OutputFormat = typer.Option(
        OutputFormat.CLI,
        "--output",
        "-o",
        help="Output format.",
    ),
) -> None:
    """
    Scan an IAM policy.
    """

    service = AnalysisService()

    summary = service.analyze(str(policy_file))

    if output is OutputFormat.CLI:
        formatter = CLIFormatter()
        console.print(formatter.format(summary))
        return

    if output is OutputFormat.JSON:
        JsonReportWriter().write(summary, "report.json")
        console.print(
            "[green]✓ JSON report written to report.json[/green]"
        )
        return

    if output is OutputFormat.SARIF:
        SarifReportWriter().write(summary, "report.sarif")
        console.print(
            "[green]✓ SARIF report written to report.sarif[/green]"
        )
        return
