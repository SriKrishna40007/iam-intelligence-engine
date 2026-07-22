from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class NotResourceRule(BaseRule):
    """
    Detects IAM policies that use NotResource with Allow.
    """

    @property
    def rule_id(self) -> str:
        return "IAM005"

    @property
    def name(self) -> str:
        return "Dangerous NotResource Usage"

    @property
    def description(self) -> str:
        return (
            "Using NotResource with Allow may unintentionally grant "
            "access to unintended resources."
        )

    @property
    def severity(self) -> Severity:
        return Severity.HIGH

    def evaluate(self, policy: Policy):
        findings = []

        for statement in policy.statements:
            if not self.is_allow_statement(statement):
                continue

            if not statement.not_resources:
                continue

            findings.append(
                self.create_finding(
                    message="Policy uses NotResource with Allow.",
                    resource="IAM Policy",
                    recommendation=(
                        "Prefer explicitly listing allowed resources "
                        "instead of excluding resources with NotResource."
                    ),
                )
            )

        return findings
