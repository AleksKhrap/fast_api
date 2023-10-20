from fastapi import FastAPI, HTTPException
from .models import Notification
from .database import create_notification, read_notification

app = FastAPI()


@app.post("/notifications")
async def create_notification_api(notification: Notification):
    notification_id = create_notification(notification)
    if notification_id:
        return notification_id
    else:
        raise HTTPException(status_code=500, detail="Ошибка при создании уведомления")


@app.get("/notifications/{notification_id}")
async def read_notification_api(notification_id: str):
    notification = read_notification(notification_id)
    if notification:
        return notification
    else:
        raise HTTPException(status_code=404, detail="Уведомление не найдено")
