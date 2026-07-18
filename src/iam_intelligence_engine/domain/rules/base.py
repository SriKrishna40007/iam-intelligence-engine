from abc import ABC, abstractmethod

from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity


class BaseRule(ABC):
    """
    Base class for all IAM security rules.
    """

    @property
    @abstractmethod
    def rule_id(self) -> str:
        """Unique identifier for the rule."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable rule name."""

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of what the rule checks."""

    @property
    @abstractmethod
    def severity(self) -> Severity:
        """Default severity assigned to this rule."""

    @abstractmethod
    def evaluate(self, policy: Policy) -> list[Finding]:
        """
        Evaluate the policy and return any findings.

        Returns an empty list when no issues are detected.
        """