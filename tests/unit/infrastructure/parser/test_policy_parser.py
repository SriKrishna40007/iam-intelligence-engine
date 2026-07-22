from iam_intelligence_engine.infrastructure.parser.policy_parser import PolicyParser


def test_parser_converts_policy_dictionary_to_domain_model():
    parser = PolicyParser()

    policy = parser.parse(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": ["s3:GetObject"],
                    "Resource": "*",
                }
            ],
        }
    )

    assert policy.version == "2012-10-17"
    assert len(policy.statements) == 1

    statement = policy.statements[0]

    assert statement.effect == "Allow"
    assert statement.actions == ["s3:GetObject"]
    assert statement.resources == ["*"]

    assert statement.not_actions == []
    assert statement.not_resources == []
    assert statement.conditions == {}
    assert statement.sid is None


def test_parser_supports_extended_iam_fields():
    parser = PolicyParser()

    policy = parser.parse(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "AllowEverythingExceptDeleteUser",
                    "Effect": "Allow",
                    "NotAction": "iam:DeleteUser",
                    "NotResource": "*",
                    "Condition": {
                        "StringEquals": {
                            "aws:RequestedRegion": "ap-south-1"
                        }
                    },
                }
            ],
        }
    )

    statement = policy.statements[0]

    assert statement.effect == "Allow"
    assert statement.actions == []
    assert statement.not_actions == ["iam:DeleteUser"]
    assert statement.resources == []
    assert statement.not_resources == ["*"]

    assert statement.conditions == {
        "StringEquals": {
            "aws:RequestedRegion": "ap-south-1"
        }
    }

    assert statement.sid == "AllowEverythingExceptDeleteUser"
