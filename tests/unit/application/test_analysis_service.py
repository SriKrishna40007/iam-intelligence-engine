from pathlib import Path

from iam_intelligence_engine.application.analysis_service import AnalysisService


def test_analysis_service_returns_summary():
    service = AnalysisService()

    policy = Path("examples/administrator_access.json")

    summary = service.analyze(str(policy))

    assert summary is not None
    assert hasattr(summary, "overall_risk_score")
    assert hasattr(summary, "findings")
    assert hasattr(summary, "recommendations")
