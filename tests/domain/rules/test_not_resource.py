from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.not_resource import NotResourceRule


def test_detects_not_resource_usage():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                not_resources=["arn:aws:s3:::company-sensitive/*"],
            )
        ],
    )

    findings = NotResourceRule().evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM005"


def test_policy_without_not_resource_passes():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                resources=["arn:aws:s3:::company-data/*"],
            )
        ],
    )

    findings = NotResourceRule().evaluate(policy)

    assert findings == []
