from dataclasses import dataclass, field

from iam_intelligence_engine.domain.models.finding import Finding


@dataclass(slots=True)
class Correlation:
    """
    Represents a higher-level security issue formed by combining
    multiple findings.
    """

    title: str
    description: str

    findings: list[Finding] = field(default_factory=list)

    risk_score: int = 0

    recommendation: str = ""
