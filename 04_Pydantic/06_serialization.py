from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal


# Pydantic model representing the input schema.
class input(BaseModel):

    query: str = Field(..., description="this is query")


# Pydantic model representing the output schema.
class output(BaseModel):

    query: str = Field(..., description="query")
    result: str = Field(..., description="this is result")


# Function accepts an 'input' object and returns an 'output' object.
# The return type hint (-> output) indicates the expected return model.
def process_data(p_input: input) -> output:

    # Extract the query from the validated input object.
    input_query = p_input.query

    # Simulate processing of the input.
    result = "Hello Bro"

    # Create a validated output object.
    pyd_output = output(
        **{
            "query": input_query,
            "result": result
        }
    )

    return pyd_output


# Create and validate the input object.
input_query = input(**{"query": "How are you?"})

# Pass the input object to the function.
response = process_data(input_query)

# Print the Pydantic model.
print(response)

print("-------------------------------")

# Convert the Pydantic model into a Python dictionary.
print(response.model_dump())

print("---------------------------------")

# Convert the Pydantic model into a JSON string.
print(response.model_dump_json())
