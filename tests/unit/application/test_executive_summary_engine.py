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
