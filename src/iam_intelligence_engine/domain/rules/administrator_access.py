from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class AdministratorAccessRule(BaseRule):
    """
    Detects IAM policies that effectively grant administrator access.
    """

    @property
    def rule_id(self) -> str:
        return "IAM003"

    @property
    def name(self) -> str:
        return "Administrator Access"

    @property
    def description(self) -> str:
        return "IAM policy grants administrator-level permissions."

    @property
    def severity(self) -> Severity:
        return Severity.CRITICAL

    def evaluate(self, policy: Policy):
        findings = []

        for statement in policy.statements:
            if not self.is_allow_statement(statement):
                continue

            if "*" not in statement.actions:
                continue

            if "*" not in statement.resources:
                continue

            findings.append(
                self.create_finding(
                    message="Administrator access detected.",
                    resource="IAM Policy",
                    recommendation=(
                        "Grant only the minimum permissions required "
                        "following the Principle of Least Privilege."
                    ),
                )
            )

        return findings
