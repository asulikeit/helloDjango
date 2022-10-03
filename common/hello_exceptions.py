from rest_framework.views import exception_handler

def custom_exception_hander(exc, context):

    response = exception_handler(exc, context)

    if response:
        response.data = {
            'status_code': response.status_code,
            'message': response.data,
        }

    return response
    