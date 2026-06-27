
"""
===============================================================================
File: 03_async_tasks.py

Topic:
    Async Tasks in Python (asyncio.create_task)

Author:
    Shrinath Patil

Description:
    This file explains what Async Tasks are and why they are important in
    asynchronous programming.

    Until now, we have learned:
        ✓ async functions
        ✓ await keyword
        ✓ coroutines
        ✓ event loop

    In this file, we will learn how to execute multiple coroutines
    concurrently using asyncio.create_task().

Why Async Tasks?

    Simply awaiting one coroutine after another executes them sequentially.

    Async Tasks allow the event loop to schedule multiple coroutines
    independently so they can make progress concurrently.

Real-world Examples:
    • Calling multiple LLM APIs
    • Querying multiple databases
    • Fetching documents from multiple services
    • Running parallel tool calls in AI Agents
    • Processing multiple files simultaneously

===============================================================================
"""

import asyncio


# ------------------------------------------------------------------------------
# Example Coroutine
# ------------------------------------------------------------------------------

async def process_document(document_name: str, delay: int) -> None:
    """
    Simulates processing a document.

    Parameters
    ----------
    document_name : str
        Name of the document.

    delay : int
        Time taken to process the document.

    Returns
    -------
    None
    """

    print(f"Started processing {document_name}")

    # Simulate I/O operation
    await asyncio.sleep(delay)

    print(f"Finished processing {document_name}")


# ------------------------------------------------------------------------------
# Main Coroutine
# ------------------------------------------------------------------------------

async def main() -> None:
    """
    Demonstrates Async Tasks.

    Instead of awaiting each coroutine immediately,
    we convert them into Tasks.

    The event loop schedules all tasks together.
    """

    print("\nCreating Tasks...\n")

    task1 = asyncio.create_task(
        process_document("Research_Report.pdf", 3)
    )

    task2 = asyncio.create_task(
        process_document("Annual_Report.pdf", 2)
    )

    task3 = asyncio.create_task(
        process_document("Financial_Report.pdf", 1)
    )

    print("All tasks created.\n")

    # Wait until every task finishes

    await task1
    await task2
    await task3

    print("\nAll documents processed successfully.")


# ------------------------------------------------------------------------------
# Driver Code
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main())

#done