class HttpError:
    def __init__(self, error):
        self.name = error.name
        self.code = error.code
        self.description = error.description
    
    def send(self):
        return {
            "error": self.name,
            "code": self.code,
            "description": self.description,
        }, self.code

