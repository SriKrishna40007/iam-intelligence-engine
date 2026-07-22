from iam_intelligence_engine.domain.models.correlation import Correlation


def test_create_correlation():
    correlation = Correlation(
        title="Privilege Escalation",
        description="Multiple findings indicate a privilege escalation path.",
        risk_score=95,
        recommendation="Reduce excessive IAM permissions.",
    )

    assert correlation.title == "Privilege Escalation"
    assert correlation.risk_score == 95
    assert correlation.findings == []
