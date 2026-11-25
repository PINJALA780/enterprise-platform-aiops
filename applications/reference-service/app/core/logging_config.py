import json
import logging
import sys
from datetime import datetime, timezone

from app.core.config import APP_ENV, APP_NAME, LOG_LEVEL


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": record.levelname,
            "service": APP_NAME,
            "environment": APP_ENV,
            "logger": record.name,
            "message": record.getMessage(),
        }

        for field in (
            "event",
            "request_id",
            "method",
            "path",
            "status_code",
            "duration_ms",
        ):
            value = getattr(record, field, None)
            if value is not None:
                log_entry[field] = value

        if record.exc_info:
            log_entry["exception"] = self.formatException(record.exc_info)

        return json.dumps(log_entry)


def configure_logging():
    level = getattr(logging, LOG_LEVEL, logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.addHandler(handler)
    root_logger.setLevel(level)
