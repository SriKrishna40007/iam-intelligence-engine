import json
from pathlib import Path

import typer
from rich.console import Console

from iam_intelligence_engine.bootstrap.container import ApplicationContainer
from iam_intelligence_engine.config.logging import get_logger
from iam_intelligence_engine.config.settings import (
    APP_NAME,
    DEFAULT_JSON_REPORT,
    DEFAULT_SARIF_REPORT,
    VERSION,
)
from iam_intelligence_engine.presentation.cli_formatter import CLIFormatter
from iam_intelligence_engine.presentation.json_report_writer import JsonReportWriter
from iam_intelligence_engine.presentation.output_format import OutputFormat
from iam_intelligence_engine.presentation.sarif_report_writer import (
    SarifReportWriter,
)

logger = get_logger(__name__)

console = Console()

app = typer.Typer(
    help=APP_NAME,
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
    console.print(f"[bold green]{APP_NAME}[/bold green]")
    console.print(f"Version: {VERSION}")


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

    logger.info("Starting IAM policy analysis")

    with policy_file.open(encoding="utf-8") as file:
        policy_data = json.load(file)

    service = ApplicationContainer.build()

    summary = service.analyze(policy_data)

    if output is OutputFormat.CLI:
        console.print(CLIFormatter().format(summary))
        return

    if output is OutputFormat.JSON:
        JsonReportWriter().write(
            summary,
            DEFAULT_JSON_REPORT,
        )
        console.print(
            f"[green]✓ JSON report written to {DEFAULT_JSON_REPORT}[/green]"
        )
        return

    if output is OutputFormat.SARIF:
        SarifReportWriter().write(
            summary,
            DEFAULT_SARIF_REPORT,
        )
        console.print(
            f"[green]✓ SARIF report written to {DEFAULT_SARIF_REPORT}[/green]"
        )