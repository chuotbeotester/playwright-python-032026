from .base_api import BaseAPI

class Auth(BaseAPI):
    
    def register(self, payload):
        return self.request.post("/api/register", data= payload)
    
    