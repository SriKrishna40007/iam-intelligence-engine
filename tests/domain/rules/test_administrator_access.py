from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement
from iam_intelligence_engine.domain.rules.administrator_access import AdministratorAccessRule


def test_detects_administrator_access():
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

    findings = AdministratorAccessRule().evaluate(policy)

    assert len(findings) == 1
    assert findings[0].rule_id == "IAM003"


def test_specific_permissions_are_not_admin():
    policy = Policy(
        version="2012-10-17",
        statements=[
            Statement(
                effect="Allow",
                actions=["s3:GetObject"],
                resources=["arn:aws:s3:::company/*"],
            )
        ],
    )

    findings = AdministratorAccessRule().evaluate(policy)

    assert findings == []
