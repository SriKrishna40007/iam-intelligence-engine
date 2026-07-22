from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class FullServiceAccessRule(BaseRule):
    """
    Detects full administrative access to AWS services.
    """

    @property
    def rule_id(self) -> str:
        return "IAM006"

    @property
    def name(self) -> str:
        return "Full Service Administrative Access"

    @property
    def description(self) -> str:
        return (
            "Granting service:* permissions provides full control "
            "over an AWS service."
        )

    @property
    def severity(self) -> Severity:
        return Severity.HIGH

    def evaluate(self, policy: Policy):
        findings = []

        for statement in policy.statements:
            if not self.is_allow_statement(statement):
                continue

            for action in statement.actions:
                if action == "*":
                    continue

                if action.endswith(":*"):
                    findings.append(
                        self.create_finding(
                            message=f"Full administrative access detected: {action}",
                            resource="IAM Policy",
                            recommendation=(
                                "Grant only the required IAM actions "
                                "instead of service-wide administrative access."
                            ),
                        )
                    )

        return findings
