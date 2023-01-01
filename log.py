import logging

import sys


logger = logging.getLogger("WEB_APP")
fmt = logging.Formatter("%(levelname)s  %(asctime)s - %(message)s")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(fmt)
logger.addHandler(handler)


def create_log_record(message: str, level: int):
    logger.log(level, message)
    logging.log(level, message)


