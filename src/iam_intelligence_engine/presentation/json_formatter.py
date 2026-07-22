from dataclasses import asdict

from iam_intelligence_engine.domain.models.executive_summary import (
    ExecutiveSummary,
)


class JsonFormatter:
    """
    Converts an ExecutiveSummary into a JSON-serializable dictionary.
    """

    def format(
        self,
        summary: ExecutiveSummary,
    ) -> dict:
        return asdict(summary)
