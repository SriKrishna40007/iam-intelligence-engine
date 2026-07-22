from iam_intelligence_engine.config.constants import (
    SARIF_SCHEMA,
    SARIF_VERSION,
)
from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary


class SarifFormatter:
    """
    Converts an ExecutiveSummary into a SARIF document.
    """

    def format(
        self,
        summary: ExecutiveSummary,
    ) -> dict:
        results = []

        for finding in summary.findings:
            results.append(
                {
                    "ruleId": finding.rule_id,
                    "level": finding.severity.name.lower(),
                    "message": {
                        "text": finding.message,
                    },
                }
            )

        return {
            "version": SARIF_VERSION,
            "$schema": SARIF_SCHEMA,
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": summary.metadata.tool,
                            "version": summary.metadata.version,
                        }
                    },
                    "results": results,
                }
            ],
        }
