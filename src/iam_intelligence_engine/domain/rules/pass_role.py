from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class PassRoleRule(BaseRule):
    """
    Detects iam:PassRole permissions.
    """

    @property
    def rule_id(self) -> str:
        return "IAM007"

    @property
    def name(self) -> str:
        return "IAM PassRole Permission"

    @property
    def description(self) -> str:
        return (
            "iam:PassRole may enable privilege escalation if "
            "roles can be passed to AWS services."
        )

    @property
    def severity(self) -> Severity:
        return Severity.CRITICAL

    def evaluate(self, policy: Policy):
        findings = []

        for statement in policy.statements:
            if not self.is_allow_statement(statement):
                continue

            if "iam:PassRole" not in statement.actions:
                continue

            findings.append(
                self.create_finding(
                    message="iam:PassRole permission detected.",
                    resource="IAM Policy",
                    recommendation=(
                        "Restrict iam:PassRole to specific IAM roles "
                        "required by the workload."
                    ),
                )
            )

        return findings
