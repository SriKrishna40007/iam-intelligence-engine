from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.severity import Severity
from iam_intelligence_engine.domain.rules.base import BaseRule


class WildcardActionRule(BaseRule):
    """
    Detects IAM policy statements that allow all actions ("*").
    """

    @property
    def rule_id(self) -> str:
        return "IAM001"

    @property
    def name(self) -> str:
        return "Wildcard Action"

    @property
    def description(self) -> str:
        return "IAM policy allows all actions."

    @property
    def severity(self) -> Severity:
        return Severity.HIGH

    def evaluate(self, policy: Policy) -> list[Finding]:
        findings: list[Finding] = []

        for statement in policy.statements:
            if statement.effect != "Allow":
                continue

            if "*" not in statement.actions:
                continue

            findings.append(
                Finding(
                    rule_id=self.rule_id,
                    rule_name=self.name,
                    severity=self.severity,
                    message="Wildcard action detected.",
                    description=self.description,
                    resource="IAM Policy",
                    recommendation=(
                        "Replace '*' with only the required IAM actions "
                        "following the Principle of Least Privilege."
                    ),
                    passed=False,
                )
            )

        return findings
