from iam_intelligence_engine.application.rule_engine import RuleEngine
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule
from iam_intelligence_engine.domain.rules.registry import RuleRegistry


class DummyRule(BaseRule):
    @property
    def rule_id(self) -> str:
        return "TEST001"

    @property
    def name(self) -> str:
        return "Dummy Rule"

    @property
    def description(self) -> str:
        return "Testing rule."

    @property
    def severity(self) -> Severity:
        return Severity.LOW

    def evaluate(self, policy: Policy):
        return []


def test_rule_engine_executes_registered_rules():
    registry = RuleRegistry()
    registry.register(DummyRule())

    engine = RuleEngine(registry)

    policy = Policy(
    version="2012-10-17",
    statements=[],
)

    findings = engine.evaluate(policy)

    assert findings == []
