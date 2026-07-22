from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.full_service_access import FullServiceAccessRule


def test_detects_service_wildcard():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["iam:*"],
                resources=["*"],
            )
        ],
    )

    findings = FullServiceAccessRule().evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM006"


def test_specific_action_is_allowed():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["iam:GetUser"],
                resources=["*"],
            )
        ],
    )

    findings = FullServiceAccessRule().evaluate(policy)

    assert findings == []
