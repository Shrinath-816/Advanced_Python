
"""
===============================================================================
File: 04_asyncio_gather.py

Topic:
    asyncio.gather()

Author:
    Shrinath Patil

Description:
    This file demonstrates how to execute multiple asynchronous operations
    concurrently using asyncio.gather().

    In the previous lesson, we created multiple tasks using
    asyncio.create_task() and awaited each task individually.

    asyncio.gather() provides a cleaner and more scalable approach by
    running multiple coroutines concurrently and waiting for all of them
    to complete.

Why use asyncio.gather()?

    • Executes multiple coroutines concurrently.
    • Waits until every coroutine completes.
    • Collects and returns results in the same order they were passed.
    • Produces cleaner and more maintainable code.

Real-world AI Examples:
    • Query multiple LLM APIs simultaneously.
    • Retrieve documents from multiple knowledge sources.
    • Generate embeddings for multiple documents.
    • Execute multiple AI agent tools in parallel.
    • Perform concurrent API calls in FastAPI services.

===============================================================================
"""

import asyncio


# ------------------------------------------------------------------------------
# Example Coroutine
# ------------------------------------------------------------------------------

async def fetch_stock_price(company: str, delay: int) -> str:
    """
    Simulates fetching stock data from an external API.

    Parameters
    ----------
    company : str
        Company name.

    delay : int
        Simulated network delay.

    Returns
    -------
    str
        Mock stock information.
    """

    print(f"Fetching data for {company}...")

    await asyncio.sleep(delay)

    print(f"Completed {company}")

    return f"{company} : Stock data received"


# ------------------------------------------------------------------------------
# Main Coroutine
# ------------------------------------------------------------------------------

async def main() -> None:
    """
    Demonstrates asyncio.gather().

    Multiple coroutines are executed concurrently.
    gather() waits until all of them finish and
    returns their results.
    """

    print("\nStarting concurrent API calls...\n")

    results = await asyncio.gather(
        fetch_stock_price("Apple", 3),
        fetch_stock_price("Microsoft", 2),
        fetch_stock_price("Google", 1)
    )

    print("\nResults Returned:\n")

    for result in results:
        print(result)


# ------------------------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())

