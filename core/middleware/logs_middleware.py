import logging


class LogsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger = logging.getLogger(__name__)
        logger.info(f'Request: {request}')
        response = self.get_response(request)
        logger.info(f'Response: {response}')
        if response.status_code == 404:
            logger.critical(f"HttpResponseNotFound Error from Requested url: {request.path}")

        return response
