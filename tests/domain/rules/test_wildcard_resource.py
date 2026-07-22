from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.wildcard_resource import WildcardResourceRule


def test_detects_wildcard_resource():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                resources=["*"],
            )
        ],
    )

    rule = WildcardResourceRule()

    findings = rule.evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM002"
    assert findings[0].passed is False


def test_does_not_flag_specific_resources():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                resources=[
                    "arn:aws:s3:::company-data/*",
                ],
            )
        ],
    )

    rule = WildcardResourceRule()

    findings = rule.evaluate(policy)

    assert findings == []
