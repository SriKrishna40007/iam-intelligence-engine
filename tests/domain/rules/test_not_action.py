from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.not_action import NotActionRule


def test_detects_not_action_usage():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                not_actions=["iam:DeleteUser"],
                resources=["*"],
            )
        ],
    )

    findings = NotActionRule().evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM004"


def test_policy_without_not_action_passes():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                resources=["*"],
            )
        ]
    )

    findings = NotActionRule().evaluate(policy)

    assert findings == []
