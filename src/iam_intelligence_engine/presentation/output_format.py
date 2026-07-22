from enum import Enum


class OutputFormat(str, Enum):
    CLI = "cli"
    JSON = "json"
    SARIF = "sarif"
