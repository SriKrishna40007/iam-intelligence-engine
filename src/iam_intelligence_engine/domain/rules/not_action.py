from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class NotActionRule(BaseRule):
    """
    Detects IAM policies that use NotAction with Allow.
    """

    @property
    def rule_id(self) -> str:
        return "IAM004"

    @property
    def name(self) -> str:
        return "Dangerous NotAction Usage"

    @property
    def description(self) -> str:
        return (
            "Using NotAction with Allow may unintentionally grant "
            "broad permissions."
        )

    @property
    def severity(self) -> Severity:
        return Severity.HIGH

    def evaluate(self, policy: Policy):
        findings = []

        for statement in policy.statements:
            if not self.is_allow_statement(statement):
                continue

            if not statement.not_actions:
                continue

            findings.append(
                self.create_finding(
                    message="Policy uses NotAction with Allow.",
                    resource="IAM Policy",
                    recommendation=(
                        "Replace NotAction with explicit allowed actions "
                        "following least privilege."
                    ),
                )
            )

        return findings
