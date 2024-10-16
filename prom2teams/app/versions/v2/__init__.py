import logging
from flask_restx import Api
from werkzeug.exceptions import HTTPException

log = logging.getLogger(__name__)

api_v2 = Api(version='2.0', title='Prom2Teams API v2',
             description='A swagger interface for Prom2Teams webservices')


@api_v2.errorhandler
def default_error_handler(e):
    # Define a default error message at the start
    msg = 'An unhandled exception occurred.'

    # Log the full stack trace for debugging
    # log.exception(f"{msg}: {str(e)}\n{traceback.format_exc()}")

    # Customize the response based on the type of exception
    if isinstance(e, HTTPException):
        # Set a specific message for HTTPException
        msg = e.description
        # Return a dictionary for the HTTPException's description and code
        return {'message': msg}, e.code
    elif isinstance(e, ValueError):
        # For ValueError, set a specific message and return a 400 Bad Request code
        msg = 'Invalid value provided.'
        return {'message': msg}, 400
    elif isinstance(e, KeyError):
        # For KeyError, set a specific message and return a 400 Bad Request code
        msg = 'Missing required data.'
        return {'message': msg}, 400
    else:
        # Generic response for other unhandled exceptions
        return {'message': msg}, 500