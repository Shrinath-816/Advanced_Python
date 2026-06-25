from pydantic import BaseModel, Field, field_validator
from typing import Optional, Dict, Any, List, Literal


# Define a Pydantic model for validating user information.
class personal_info(BaseModel):

    name: str = Field(..., min_length=3, max_length=20, description="this is name")
    age: int | None = Field(..., ge=0, description="this is age")
    email: str = Field(..., description="this is email")

    # Custom validator for the 'email' field.
    # Runs automatically whenever a personal_info object is created.
    @field_validator('email')
    def email_check(cls, value):

        # Raise an error if '@' is missing.
        if "@" not in value:
            raise ValueError("Invalid email address")

        # If '.com' is missing, append it automatically.
        elif ".com" not in value:
            return value + ".com"

        # Otherwise, return the email as it is.
        else:
            return value


# Create and validate the Pydantic object.
# ** unpacks the dictionary into keyword arguments.
pyd_ins = personal_info(
    **{
        "name": "Ansh Lamba",
        "age": 25,
        "email": "ansh.lamb@aexample"
    }
)

# Print the validated object.
print(pyd_ins)
