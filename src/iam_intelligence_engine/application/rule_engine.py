from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.rules.registry import RuleRegistry


class RuleEngine:
    """
    Executes every registered rule against a policy and aggregates findings.
    """

    def __init__(self, registry: RuleRegistry) -> None:
        self._registry = registry

    def evaluate(self, policy: Policy) -> list[Finding]:
        findings: list[Finding] = []

        for rule in self._registry:
            findings.extend(rule.evaluate(policy))

        return findings
