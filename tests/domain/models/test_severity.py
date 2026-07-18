from iam_intelligence_engine.domain.models.severity import Severity


def test_severity_values():
    assert Severity.CRITICAL.value == "CRITICAL"
    assert Severity.HIGH.value == "HIGH"
    assert Severity.MEDIUM.value == "MEDIUM"
    assert Severity.LOW.value == "LOW"
    assert Severity.INFO.value == "INFO"


def test_severity_is_string():
    assert isinstance(Severity.CRITICAL, str)


def test_all_severities_exist():
    assert len(Severity) == 5