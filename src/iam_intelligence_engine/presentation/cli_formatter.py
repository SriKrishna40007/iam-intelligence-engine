from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary


class CLIFormatter:
    """
    Formats an ExecutiveSummary for terminal output.
    """

    def format(self, summary: ExecutiveSummary) -> str:
        lines: list[str] = []

        lines.append("=" * 60)
        lines.append("IAM INTELLIGENCE ENGINE REPORT")
        lines.append("=" * 60)
        lines.append("")

        lines.append(f"Overall Risk Score : {summary.overall_risk_score}")
        lines.append(f"Findings           : {len(summary.findings)}")
        lines.append(f"Correlations       : {len(summary.correlations)}")
        lines.append("")

        lines.append("Recommendations")

        if summary.recommendations:
            for recommendation in summary.recommendations:
                lines.append(f"  • {recommendation}")
        else:
            lines.append("  None")

        return "\n".join(lines)
