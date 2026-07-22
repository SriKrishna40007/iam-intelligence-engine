from iam_intelligence_engine.domain.models.correlation import Correlation
from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.domain.models.finding import Finding


class ExecutiveSummaryEngine:
    """
    Builds a high-level summary from findings,
    correlations, and the calculated risk score.
    """

    def build(
        self,
        findings: list[Finding],
        correlations: list[Correlation],
        risk_score: int,
    ) -> ExecutiveSummary:

        recommendations = sorted(
            {
                finding.recommendation
                for finding in findings
            }
        )

        return ExecutiveSummary(
            overall_risk_score=risk_score,
            findings=findings,
            correlations=correlations,
            recommendations=recommendations,
        )
