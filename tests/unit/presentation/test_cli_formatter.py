from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.presentation.cli_formatter import CLIFormatter


def test_formatter_outputs_summary():
    formatter = CLIFormatter()

    summary = ExecutiveSummary(
        overall_risk_score=95,
        recommendations=[
            "Restrict iam:PassRole",
            "Replace wildcard permissions",
        ],
    )

    output = formatter.format(summary)

    assert "IAM INTELLIGENCE ENGINE REPORT" in output
    assert "95" in output
    assert "Restrict iam:PassRole" in output
