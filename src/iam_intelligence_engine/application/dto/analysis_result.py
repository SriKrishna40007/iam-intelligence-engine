from dataclasses import dataclass

from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary


@dataclass(frozen=True)
class AnalysisResult:
    """
    Output contract for the analysis pipeline.
    """

    summary: ExecutiveSummary
