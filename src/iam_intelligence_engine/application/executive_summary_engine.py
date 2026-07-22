from datetime import UTC, datetime

from iam_intelligence_engine.domain.models.correlation import Correlation
from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.report_metadata import ReportMetadata


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

        metadata = ReportMetadata(
            tool="IAM Intelligence Engine",
            version="0.1.0",
            generated_at=datetime.now(UTC).isoformat(),
        )

        return ExecutiveSummary(
            overall_risk_score=risk_score,
            metadata=metadata,
            findings=findings,
            correlations=correlations,
            recommendations=recommendations,
        )