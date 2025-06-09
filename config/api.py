from ninja import NinjaAPI

from posts.api import router as post_router

api = NinjaAPI(docs_url='docs/')
api.add_router('posts/', post_router)
