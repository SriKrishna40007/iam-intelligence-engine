from iam_intelligence_engine.config.logging import get_logger
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.rules.registry import RuleRegistry


logger = get_logger(__name__)


class RuleEngine:
    """
    Executes all registered security rules against an IAM policy.
    """

    def __init__(self, registry: RuleRegistry) -> None:
        self._registry = registry

    def evaluate(self, policy: Policy):
        findings = []

        logger.info(
            "Executing %d security rules",
            len(self._registry),
        )

        for rule in self._registry:
            logger.debug(
                "Running %s",
                rule.__class__.__name__,
            )

            findings.extend(rule.evaluate(policy))

        logger.info(
            "Rule evaluation completed. %d finding(s) generated.",
            len(findings),
        )

        return findings
