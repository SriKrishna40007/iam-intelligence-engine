from iam_intelligence_engine.domain.models.correlation import Correlation
from iam_intelligence_engine.domain.models.finding import Finding


class CorrelationEngine:
    """
    Builds higher-level security correlations from individual findings.
    """

    def correlate(
        self,
        findings: list[Finding],
    ) -> list[Correlation]:

        correlations: list[Correlation] = []

        rule_ids = {finding.rule_id for finding in findings}

        if {"IAM003", "IAM007"}.issubset(rule_ids):

            related = [
                finding
                for finding in findings
                if finding.rule_id in {"IAM003", "IAM007"}
            ]

            correlations.append(
                Correlation(
                    title="Potential Privilege Escalation",
                    description=(
                        "Administrator access together with "
                        "iam:PassRole may enable privilege escalation."
                    ),
                    findings=related,
                    risk_score=95,
                    recommendation=(
                        "Remove unnecessary administrator permissions "
                        "and restrict iam:PassRole."
                    ),
                )
            )

        return correlations
