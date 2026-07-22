from iam_intelligence_engine.domain.models.finding import Finding
from iam_intelligence_engine.domain.models.severity import Severity


class RiskScoreEngine:
    """
    Calculates an overall risk score from findings.
    """

    SCORE_MAP = {
        Severity.CRITICAL: 25,
        Severity.HIGH: 15,
        Severity.MEDIUM: 8,
        Severity.LOW: 3,
        Severity.INFO: 1,
    }

    MAX_SCORE = 100

    def calculate(self, findings: list[Finding]) -> int:
        score = 0

        for finding in findings:
            score += self.SCORE_MAP.get(finding.severity, 0)

        return min(score, self.MAX_SCORE)
