from iam_intelligence_engine.presentation.output_format import OutputFormat


def test_output_formats():
    assert OutputFormat.CLI.value == "cli"
    assert OutputFormat.JSON.value == "json"
    assert OutputFormat.SARIF.value == "sarif"
