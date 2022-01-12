from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError, IntegrityError
from werkzeug.exceptions import BadRequest, InternalServerError
import logger

log = logger.get_logger(__name__)

db = SQLAlchemy()

def save_data():
    """Save and commit changed in Database or Rollback
    """
    try:
        db.session.commit()
    except IntegrityError as ex:
        log.warning("got integrity error with text %s", ex)
        raise BadRequest(f"Could not save user, probably name or email is not unique")
    except DatabaseError as e:
        db.session.rollback()
        log.exception("Database error: %s", e)
        raise InternalServerError(f"Could not save user!")



__all__ = (
    "db",
    "save_data",
)