# Import required classes from the Pydantic library.
from pydantic import BaseModel, Field, StrictInt


# Create a Pydantic model by inheriting from BaseModel.
class ansh(BaseModel):

    # Required field of type StrictInt.
    # StrictInt accepts only integer values (no automatic type conversion).
    x: StrictInt = Field(..., description="this is x")

    # Optional field with a default value.
    y: str = Field(default="Ansh Lamba")


# Create an object of the model.
# ** unpacks the dictionary into keyword arguments.
# Since 'y' is not provided, its default value is used.
pyd_input = ansh(**{"x": 1})

# Print the validated Pydantic object.
print(pyd_input)


# Function expecting an object of type 'ansh'.
def main(para1: ansh):

    print("Hello Ansh Lamba")


# Pass the Pydantic object to the function.
main(pyd_input)