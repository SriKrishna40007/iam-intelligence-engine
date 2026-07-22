from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.wildcard_action import WildcardActionRule


def test_detects_wildcard_action():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["*"],
                resources=["*"],
            )
        ],
    )

    rule = WildcardActionRule()

    findings = rule.evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM001"
    assert findings[0].passed is False


def test_does_not_flag_specific_actions():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=[
                    "s3:GetObject",
                    "s3:PutObject",
                ],
                resources=["*"],
            )
        ],
    )

    rule = WildcardActionRule()

    findings = rule.evaluate(policy)

    assert findings == []
