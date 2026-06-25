from pydantic import BaseModel, Field, computed_field
from typing import Optional, Dict, Any, List, Literal


# Pydantic model representing an order.
class orders(BaseModel):

    id: int = Field(..., description="Order Id")
    units: int = Field(..., description="Units")
    amount: int = Field(..., description="Amount Per Unit")

    # Computed field is calculated automatically and
    # is not required in the input data.
    @computed_field
    @property
    def total_amount(self) -> int:

        # Calculate the total order amount.
        return self.units * self.amount


# Create and validate the Pydantic object.
pyd_ins = orders(**{"id": 1, "units": 10, "amount": 100})

# Print the object including the computed field.
print(pyd_ins)
