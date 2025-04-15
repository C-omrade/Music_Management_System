import rest_framework.response

class Response(rest_framework.response.Response):
    """The various HTTP responses for use in returning proper HTTP codes.
    """

    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False,
                 content_type=None):
        super().__init__(data, status, template_name, headers, exception, content_type)
        
        
class BadRequest(Response):
    status_code = 400