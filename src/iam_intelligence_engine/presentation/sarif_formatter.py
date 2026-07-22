from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary


class SarifFormatter:
    """
    Converts an ExecutiveSummary into a SARIF dictionary.
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
            "version": "2.1.0",
            "$schema": (
                "https://json.schemastore.org/sarif-2.1.0.json"
            ),
            "runs": [
                {
                    "tool": {
                        "driver": {
                            "name": "IAM Intelligence Engine",
                            "version": summary.metadata.version,
                        }
                    },
                    "results": results,
                }
            ],
        }
