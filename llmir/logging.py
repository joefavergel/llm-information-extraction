import logging
import sys
from logging.handlers import MemoryHandler


class APIFormatter(logging.Formatter):
    grey = "\x1b[38;21m"
    cyan = "\x1b[36;20m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    green = "\x1b[32m"
    asctime = "%(asctime)s"
    name = "[%(name)s]"
    levelname = "[%(levelname)-4s]"
    message = "%(message)s"

    FORMATS = {
        logging.DEBUG: f"{asctime} {cyan} {name} {levelname} {reset} {message}",
        logging.INFO: f"{asctime} {green} {name} {levelname} {reset} {message}",
        logging.WARNING: f"{asctime} {yellow} {name} {levelname} {message} {reset}",
        logging.ERROR: f"{asctime} {red} {name} {levelname} {message} {reset}",
        logging.CRITICAL: f"{asctime} {bold_red} {name} {levelname} {message} {reset}",
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# Configuración básica del logger
def setup_logger():
    logger = logging.getLogger("iq-server")
    logger.setLevel(logging.INFO)

    # Handler to write logs in memory, with flushing to disk
    memory_handler = MemoryHandler(capacity=10000000, flushLevel=logging.ERROR)
    memory_handler.setFormatter(APIFormatter())
    logger.addHandler(memory_handler)

    # Handler for standard output (console)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(APIFormatter())
    logger.addHandler(console_handler)

    return logger


# Crear y configurar el logger
logger = setup_logger()
