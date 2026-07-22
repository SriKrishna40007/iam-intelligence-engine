from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.pass_role import PassRoleRule


def test_detects_pass_role():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["iam:PassRole"],
                resources=["*"],
            )
        ],
    )

    findings = PassRoleRule().evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM007"


def test_policy_without_pass_role():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["iam:GetRole"],
                resources=["*"],
            )
        ],
    )

    findings = PassRoleRule().evaluate(policy)

    assert findings == []
