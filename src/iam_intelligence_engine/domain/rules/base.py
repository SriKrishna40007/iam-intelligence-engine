from abc import ABC, abstractmethod

from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity


class BaseRule(ABC):
    """Base contract for all IAM security rules."""

    @property
    @abstractmethod
    def rule_id(self) -> str:
        """Unique identifier for the rule."""
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        """Human-readable rule name."""
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        """Description of the rule."""
        raise NotImplementedError

    @property
    @abstractmethod
    def severity(self) -> Severity:
        """Severity assigned to findings produced by this rule."""
        raise NotImplementedError

    @abstractmethod
    def evaluate(self, policy: Policy) -> list[Finding]:
        """
        Evaluate an IAM policy.

        Returns:
            list[Finding]: Zero or more findings.
        """
        raise NotImplementedError