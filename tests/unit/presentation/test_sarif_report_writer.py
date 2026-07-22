import json

from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.domain.models.report_metadata import ReportMetadata
from iam_intelligence_engine.presentation.sarif_report_writer import (
    SarifReportWriter,
)


def test_sarif_report_writer(tmp_path):
    writer = SarifReportWriter()

    output = tmp_path / "report.sarif"

    summary = ExecutiveSummary(
        overall_risk_score=0,
        metadata=ReportMetadata(
            tool="IAM Intelligence Engine",
            version="0.1.0",
            generated_at="2026-01-01T00:00:00Z",
        ),
    )

    writer.write(summary, str(output))

    assert output.exists()

    data = json.loads(output.read_text())

    assert data["version"] == "2.1.0"
