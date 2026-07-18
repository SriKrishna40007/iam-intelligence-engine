from abc import ABC, abstractmethod

from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity


class BaseRule(ABC):
    """Base contract for all IAM security rules."""

    @property
    @abstractmethod
    def rule_id(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def description(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def severity(self) -> Severity:
        raise NotImplementedError

    @abstractmethod
    def evaluate(self, policy: Policy) -> list[Finding]:
        raise NotImplementedError
