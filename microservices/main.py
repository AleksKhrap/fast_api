from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from ProductService.product_app.routers.products import router as product_router
from OrderService.order_app.routers.order import router as order_router
from InventoryService.inventory_app.routers.inventory import router as inventory_router

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"error": "Неверный формат данных"}
    )


# Обработчик глобальных исключений, который "ловит" все необработанные исключения
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": "Ошибка сервера"}
    )


app.include_router(product_router, prefix='/product')
app.include_router(order_router, prefix='/order')
app.include_router(inventory_router, prefix='/inventory')
