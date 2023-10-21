from fastapi import FastAPI

from ProductService.routers.products import app as product_app

'''
from OrderService.main import app as order_app
from NotificationService.main import app as notification_app
from InventoryService.main import app as inventory_app
'''

app = FastAPI()

app.include_router(product_app.router, prefix='/products')

'''
app.include_router(order_app.router, prefix='')
app.include_router(notification_app.router, prefix='')
app.include_router(inventory_app.router, prefix='')
'''
