from pydantic import BaseModel, Field, EmailStr
from typing import Optional, Dict, Any, List, Literal


# Define a Pydantic model for validating personal information.
class personal_info(BaseModel):

    # Required string with length validation.
    name: str = Field(..., min_length=3, max_length=20, description="this is name")

    # Required integer (can also be None) with minimum value 0.
    age: int | None = Field(..., ge=0, description="this is age")

    # Validates that the input is a proper email address.
    email: EmailStr = Field(..., description="this is email")

    # Accepts only one of the specified values.
    gender: Literal["male", "female", "other"] = Field(..., description="this is gender")

    # List of integer salaries.
    salaries: List[int] = Field(..., description="this is salaries")


# Function that accepts a validated personal_info object.
def main(para1: personal_info):

    print("name:", para1.name)
    print("age:", para1.age)
    print("email:", para1.email)
    print("gender:", para1.gender)
    print("salaries:", para1.salaries)


# Create a validated Pydantic object.
# ** unpacks the dictionary into keyword arguments.
pyd_ins = personal_info(
    **{
        "name": "Ansh Lamba",
        "age": 25,
        "email": "anshlamba@example.com",
        "gender": "male",
        "salaries": [0, 0]
    }
)

# Pass the validated object to the function.
main(pyd_ins)
