from fastapi.responses import JSONResponse
from typing import Dict, Any
from functools import wraps
from pydantic import ValidationError
import logging
import traceback
logger = logging.getLogger(__name__)


def excepction_response(status_code: int,
                        message: str = None,
                        headers: Dict[str, Any] | None = None):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "message": message,
            "data": None
        },
        headers=headers
    )


def trackback_str(exc):
    traceback_s: str = ''.join(traceback.format_exception(
        None, exc, exc.__traceback__))
    traceback_split = traceback_s.splitlines()
    if len(traceback_split) > 4:
        last_lines = traceback_split[-4:]
        return last_lines[0] + '\n' + last_lines[1] + '\n' + last_lines[2] + '\n' + last_lines[3]
    return traceback_s


def exception(moduleName, functName, fullpath):
    def handler(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            extraData = {
                "moduleName": moduleName,
                "functName": functName,
                "fullpath": fullpath
            }
            try:
                result = await func(*args, **kwargs)
                return result
            except ValidationError as exc:
                extraData['traceback'] = trackback_str(exc)
                logger.error(str(exc), extra=extraData)
                return excepction_response(400, str(exc))
            except ValueError as exc:
                extraData['traceback'] = trackback_str(exc)
                logger.error(str(exc), extra=extraData)
                return excepction_response(400, str(exc).capitalize())
            except Exception as exc:
                extraData['traceback'] = trackback_str(exc)
                logger.critical(str(exc), extra=extraData)
                return excepction_response(500, 'Unexpected situation')
        return wrapper
    return handler
