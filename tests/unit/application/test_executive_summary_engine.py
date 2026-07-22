from iam_intelligence_engine.application.executive_summary_engine import ExecutiveSummaryEngine


def test_build_summary():
    engine = ExecutiveSummaryEngine()

    summary = engine.build(
        findings=[],
        correlations=[],
        risk_score=95,
    )

    assert summary.overall_risk_score == 95
    assert summary.findings == []
    assert summary.correlations == []
    assert summary.recommendations == []
    assert summary.metadata is not None
    assert summary.metadata.tool == "IAM Intelligence Engine"
    assert summary.metadata.version == "0.1.0"
