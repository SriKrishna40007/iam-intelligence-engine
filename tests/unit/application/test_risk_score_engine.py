from iam_intelligence_engine.application.risk_score_engine import RiskScoreEngine
from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.severity import Severity


def finding(severity: Severity) -> Finding:
    return Finding(
        rule_id="TEST",
        rule_name="Test Rule",
        severity=severity,
        message="message",
        description="description",
        resource="IAM Policy",
        recommendation="recommendation",
        passed=False,
    )


def test_calculates_risk_score():
    engine = RiskScoreEngine()

    score = engine.calculate(
        [
            finding(Severity.CRITICAL),
            finding(Severity.HIGH),
            finding(Severity.MEDIUM),
        ]
    )

    assert score == 48


def test_caps_score_at_100():
    engine = RiskScoreEngine()

    findings = [
        finding(Severity.CRITICAL)
        for _ in range(10)
    ]

    assert engine.calculate(findings) == 100


def test_empty_findings_have_zero_score():
    engine = RiskScoreEngine()

    assert engine.calculate([]) == 0
