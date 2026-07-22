from dataclasses import dataclass


@dataclass(slots=True)
class ReportMetadata:
    """
    Metadata describing a generated security report.
    """

    tool: str
    version: str
    generated_at: str
