class HttpResponse:
    def __init__(self, code, data, message):
        self.code = code
        self.data = data
        self.message = message
    
    def send(self):
        return {
            "code": self.code,
            "data": self.data,
            "message": self.message,
        }, 200

