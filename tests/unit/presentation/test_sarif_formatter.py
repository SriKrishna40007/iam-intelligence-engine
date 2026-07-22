from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.domain.models.report_metadata import ReportMetadata
from iam_intelligence_engine.presentation.sarif_formatter import SarifFormatter


def test_sarif_formatter():
    formatter = SarifFormatter()

    summary = ExecutiveSummary(
        overall_risk_score=0,
        metadata=ReportMetadata(
            tool="IAM Intelligence Engine",
            version="0.1.0",
            generated_at="2026-01-01T00:00:00Z",
        ),
    )

    result = formatter.format(summary)

    assert result["version"] == "2.1.0"
    assert result["runs"][0]["tool"]["driver"]["name"] == "IAM Intelligence Engine"
