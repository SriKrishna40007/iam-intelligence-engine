import json

from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.presentation.json_report_writer import (
    JsonReportWriter,
)


def test_writes_json_report(tmp_path):
    writer = JsonReportWriter()

    output = tmp_path / "report.json"

    summary = ExecutiveSummary(
        overall_risk_score=95,
    )

    writer.write(summary, str(output))

    assert output.exists()

    data = json.loads(output.read_text())

    assert data["overall_risk_score"] == 95
