from iam_intelligence_engine.application.correlation_engine import CorrelationEngine
from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.severity import Severity


def finding(rule_id: str) -> Finding:
    return Finding(
        rule_id=rule_id,
        rule_name=rule_id,
        severity=Severity.CRITICAL,
        message="test",
        description="test",
        resource="IAM Policy",
        recommendation="fix",
        passed=False,
    )


def test_detects_privilege_escalation():
    engine = CorrelationEngine()

    correlations = engine.correlate(
        [
            finding("IAM003"),
            finding("IAM007"),
        ]
    )

    assert len(correlations) == 1
    assert correlations[0].title == "Potential Privilege Escalation"
    assert correlations[0].risk_score == 95


def test_no_correlation_when_rules_missing():
    engine = CorrelationEngine()

    correlations = engine.correlate(
        [
            finding("IAM001"),
        ]
    )

    assert correlations == []
