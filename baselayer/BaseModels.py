from pydantic import BaseModel

"""Request Body Structure"""

class LoginPayload(BaseModel):
    phone_number: str
    resend: bool
    is_social: bool
