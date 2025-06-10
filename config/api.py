from ninja import NinjaAPI

from posts.api import router as post_router
from auth.api import router as auth_router

api = NinjaAPI(docs_url='docs/')
api.add_router('posts/', post_router)
api.add_router('auth/', auth_router)
