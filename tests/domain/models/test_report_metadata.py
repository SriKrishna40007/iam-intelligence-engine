from iam_intelligence_engine.domain.models.report_metadata import (
    ReportMetadata,
)


def test_report_metadata():
    metadata = ReportMetadata(
        tool="IAM Intelligence Engine",
        version="0.1.0",
        generated_at="2026-07-22T10:00:00Z",
    )

    assert metadata.tool == "IAM Intelligence Engine"
    assert metadata.version == "0.1.0"
