from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class WildcardResourceRule(BaseRule):
    """
    Detects IAM policy statements that allow access to all resources ("*").
    """

    @property
    def rule_id(self) -> str:
        return "IAM002"

    @property
    def name(self) -> str:
        return "Wildcard Resource"

    @property
    def description(self) -> str:
        return "IAM policy grants access to all resources."

    @property
    def severity(self) -> Severity:
        return Severity.HIGH

    def evaluate(self, policy: Policy) -> list[Finding]:
        findings: list[Finding] = []

        for statement in policy.statements:
            if statement.effect != "Allow":
                continue

            if "*" not in statement.resources:
                continue

            findings.append(
                Finding(
                    rule_id=self.rule_id,
                    rule_name=self.name,
                    severity=self.severity,
                    message="Wildcard resource detected.",
                    description=self.description,
                    resource="IAM Policy",
                    recommendation=(
                        "Replace '*' with specific resource ARNs whenever possible."
                    ),
                    passed=False,
                )
            )

        return findings
