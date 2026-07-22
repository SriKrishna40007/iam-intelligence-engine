from iam_intelligence_engine.bootstrap.rule_loader import RuleLoader


def test_load_registers_default_rules():
    registry = RuleLoader.load()

    assert len(registry) > 0
