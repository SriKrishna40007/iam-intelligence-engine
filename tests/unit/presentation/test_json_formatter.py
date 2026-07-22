from iam_intelligence_engine.domain.models.executive_summary import (
    ExecutiveSummary,
)
from iam_intelligence_engine.presentation.json_formatter import (
    JsonFormatter,
)


def test_json_formatter():
    formatter = JsonFormatter()

    summary = ExecutiveSummary(
        overall_risk_score=88,
    )

    result = formatter.format(summary)

    assert result["overall_risk_score"] == 88
    assert "findings" in result
    assert "recommendations" in result
