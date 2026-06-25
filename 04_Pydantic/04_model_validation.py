from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Optional, Dict, Any, List, Literal


# Pydantic model for validating API authentication data.
class API_auth(BaseModel):

    email: str = Field(..., description="this is email")

    # Password must contain at least 8 characters.
    password: str = Field(..., min_length=8, description="this is password")

    # Confirmation password must also contain at least 8 characters.
    confirm_password: str = Field(..., min_length=8, description="this is confirm password")

    # Model validator runs after all fields are validated.
    # Used when validation depends on multiple fields.
    @model_validator(mode='after')
    def password_check(cls, values):

        # Ensure both passwords match.
        if values.password != values.confirm_password:
            raise ValueError("Password not mathing")

        return values


# Create and validate the Pydantic object.
pyd_ins = API_auth(
    **{
        "email": "ansh.lamba@example.com",
        "password": "password123",
        "confirm_password": "password123"
    }
)

# Print the validated object.
print(pyd_ins)

