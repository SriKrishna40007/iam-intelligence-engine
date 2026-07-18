from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule
from iam_intelligence_engine.domain.rules.registry import RuleRegistry


class DummyRule(BaseRule):
    @property
    def rule_id(self) -> str:
        return "DUMMY001"

    @property
    def name(self) -> str:
        return "Dummy Rule"

    @property
    def description(self) -> str:
        return "Dummy rule used for testing."

    @property
    def severity(self) -> Severity:
        return Severity.LOW

    def evaluate(self, policy: Policy):
        return []


def test_register_rule():
    registry = RuleRegistry()
    rule = DummyRule()

    registry.register(rule)

    assert len(registry) == 1


def test_registry_returns_registered_rules():
    registry = RuleRegistry()

    rule = DummyRule()
    registry.register(rule)

    rules = registry.all()

    assert len(rules) == 1
    assert rules[0] is rule