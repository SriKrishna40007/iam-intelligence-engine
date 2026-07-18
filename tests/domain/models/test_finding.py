from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.severity import Severity


def test_finding_creation():
    finding = Finding(
        rule_id="IAM001",
        rule_name="Wildcard Action",
        severity=Severity.CRITICAL,
        message="Wildcard action detected",
        description="Allows every AWS action.",
        resource="Statement 1",
        recommendation="Use explicit actions.",
        passed=False,
    )

    assert finding.rule_id == "IAM001"
    assert finding.severity == Severity.CRITICAL
    assert finding.passed is False


def test_finding_is_immutable():
    finding = Finding(
        rule_id="IAM001",
        rule_name="Wildcard Action",
        severity=Severity.CRITICAL,
        message="Wildcard action detected",
        description="Allows every AWS action.",
        resource="Statement 1",
        recommendation="Use explicit actions.",
        passed=False,
    )

    import pytest

    with pytest.raises(AttributeError):
        finding.rule_id = "IAM999"