import json
from pathlib import Path

from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.presentation.sarif_formatter import SarifFormatter


class SarifReportWriter:
    """
    Writes SARIF reports to disk.
    """

    def __init__(self) -> None:
        self._formatter = SarifFormatter()

    def write(
        self,
        summary: ExecutiveSummary,
        output_file: str,
    ) -> None:
        data = self._formatter.format(summary)

        path = Path(output_file)

        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
