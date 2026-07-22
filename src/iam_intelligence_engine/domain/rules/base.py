from abc import ABC, abstractmethod

from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.models.statement import Statement


class BaseRule(ABC):
    """
    Base contract for all IAM security rules.
    """

    @property
    @abstractmethod
    def rule_id(self) -> str:
        ...

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    @abstractmethod
    def description(self) -> str:
        ...

    @property
    @abstractmethod
    def severity(self) -> Severity:
        ...

    @abstractmethod
    def evaluate(self, policy: Policy) -> list[Finding]:
        """
        Evaluate an IAM policy and return findings.
        """
        ...

    def is_allow_statement(self, statement: Statement) -> bool:
        """
        Returns True when the statement grants permissions.
        """
        return statement.effect == "Allow"

    def create_finding(
        self,
        *,
        message: str,
        resource: str,
        recommendation: str,
    ) -> Finding:
        """
        Creates a standardized Finding.
        """
        return Finding(
            rule_id=self.rule_id,
            rule_name=self.name,
            severity=self.severity,
            message=message,
            description=self.description,
            resource=resource,
            recommendation=recommendation,
            passed=False,
        )
