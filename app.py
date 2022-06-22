from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata
from dotenv import load_dotenv
from routes.auth import auth_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(  
  title="jrba",
  description="REST API using Fastapi and Mongodb",
  version="0.0.1",
  openapi_tags=tags_metadata)


app.include_router(user, prefix='/api') # responses={404: {"description": "Not found"}},
app.include_router(auth_routes, prefix='/api')

origins = [
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origins],
    allow_methods=['*'],
    allow_headers=['*']
)

load_dotenv()
