from iam_intelligence_engine.infrastructure.parser.policy_parser import PolicyParser


def test_parse_returns_policy():
    # Arrange
    parser = PolicyParser()

    policy_data = {
        "Version": "2012-10-17",
        "Statement": []
    }

    # Act
    policy = parser.parse(policy_data)

    # Assert
    assert policy.version == "2012-10-17"