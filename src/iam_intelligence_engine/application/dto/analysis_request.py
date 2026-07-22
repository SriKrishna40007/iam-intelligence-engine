from dataclasses import dataclass


@dataclass(frozen=True)
class AnalysisRequest:
    """
    Input contract for the analysis pipeline.
    """

    policy_data: dict
