from dataclasses import dataclass, field

from iam_intelligence_engine.domain.statement import Statement


@dataclass(slots=True)
class Policy:
    """
    Represents an AWS IAM Policy.
    """

    version: str
    statements: list[Statement] = field(default_factory=list)