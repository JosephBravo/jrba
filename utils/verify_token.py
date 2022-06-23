from fastapi import Request
from utils.jwt_token import validate_token
from fastapi.routing import APIRoute
from fastapi.responses import JSONResponse

class VerifyTokenRoute(APIRoute):
    
    def get_route_handler(self):
        original_route = super().get_route_handler()
        
        async def verify_token_middleware(request:Request):
            try:
                token = request.headers["Authorization"].split(" ")[1]
            except KeyError: 
                return JSONResponse(content={"message": "authorization token not found"}, status_code=404)
            validation = validate_token(token, output=False)
            if validation == None:
                return await original_route(request)
            else:
                return validation

        return verify_token_middleware
