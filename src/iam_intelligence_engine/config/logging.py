import logging


def get_logger(name: str) -> logging.Logger:
    """
    Returns a configured logger instance.
    """

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )

    return logging.getLogger(name)
