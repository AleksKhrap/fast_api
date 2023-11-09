from fastapi import FastAPI, Request, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from ProductService.app.routers.products import router as product_router
from OrderService.app.routers.order import router as order_router
'''
from NotificationService.main import app as notification_app
from InventoryService.main import app as inventory_app
'''

app = FastAPI()

app.include_router(product_router, prefix='/product')
app.include_router(order_router, prefix='/order')

'''
app.include_router(notification_app.router, prefix='')
app.include_router(inventory_app.router, prefix='')
'''


class CustomException(HTTPException):
    def __init__(self, detail: str, status_code: int = 400):
        super().__init__(status_code=status_code, detail=detail)


@app.exception_handler(CustomException)
async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail}
    )


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
