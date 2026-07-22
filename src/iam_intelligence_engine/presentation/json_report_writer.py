import json
from pathlib import Path

from iam_intelligence_engine.domain.models.executive_summary import (
    ExecutiveSummary,
)
from iam_intelligence_engine.presentation.json_formatter import JsonFormatter


class JsonReportWriter:
    """
    Writes an ExecutiveSummary as a JSON report.
    """

    def __init__(self) -> None:
        self._formatter = JsonFormatter()

    def write(
        self,
        summary: ExecutiveSummary,
        output_file: str,
    ) -> None:

        data = self._formatter.format(summary)

        path = Path(output_file)

        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
            )
