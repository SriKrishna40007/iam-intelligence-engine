from dataclasses import dataclass, field

from iam_intelligence_engine.domain.models.correlation import Correlation
from iam_intelligence_engine.domain.models.finding import Finding


@dataclass(slots=True)
class ExecutiveSummary:
    """
    High-level summary of an IAM security assessment.
    """

    overall_risk_score: int

    findings: list[Finding] = field(default_factory=list)

    correlations: list[Correlation] = field(default_factory=list)

    recommendations: list[str] = field(default_factory=list)
