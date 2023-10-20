from pydantic import BaseModel


class Notification(BaseModel):
    message_type: str
    description: str
    date: str
