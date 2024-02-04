from __future__ import annotations
import logging
import os
import sys
from typing import Optional

from . import __name__


level_mapping = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}


class Formatter(logging.Formatter):
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


def get_logger(
    *,
    type_: str = 'stream',
    level: int = None,
    logs_path: str = None,
    filename: str = None,
    process_id: str | None = None
) -> logging.Logger:
    if type_ == 'file' and logs_path is not None and filename is not None:
        if not os.path.exists(logs_path):
            os.makedirs(logs_path, exist_ok=True)

        logs_output = os.path.join(logs_path, filename)
        if not os.path.isfile(logs_output):
            with open(logs_output, "w") as file:
                file.write("")
            file.close()

        logging.basicConfig(
            filename=os.path.join(logs_path, filename),
            filemode='w',
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True,
            encoding='utf-8'
        )
    elif type_ == 'stream':
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(Formatter())
        logging.basicConfig(
            format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
            level=logging.DEBUG if level is None else level_mapping.get(level),
            datefmt="%Y-%m-%d %H:%M:%S",
            force=True,
            encoding='utf-8',
            handlers=[stream_handler]
        )
    else:
        raise Exception("Type of logger not supported or unknown")

    name = __name__ if not process_id else f"{__name__}-{process_id}"
    return logging.getLogger(name)


logger = get_logger(type_='stream')
