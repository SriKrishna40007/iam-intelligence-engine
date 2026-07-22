import json
from pathlib import Path

from iam_intelligence_engine.bootstrap.container import ApplicationContainer


def test_analysis_service_returns_summary():
    service = ApplicationContainer.build()

    policy = Path("examples/administrator_access.json")

    with policy.open(encoding="utf-8") as file:
        policy_data = json.load(file)

    summary = service.analyze(policy_data)

    assert summary.overall_risk_score > 0