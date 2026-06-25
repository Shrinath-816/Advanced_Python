# Import the asyncio module.
#
# asyncio is Python's built-in library used for asynchronous programming.
# It allows multiple tasks to run concurrently using a single thread
# through an Event Loop.
import asyncio


# Import the time module.
#
# NOTE:
# The time module is imported here but is not used anywhere in this program.
import time


# ------------------------------------------------------------------
# Define an asynchronous function (coroutine).
#
# A coroutine is created using the 'async def' keyword.
# Unlike a normal function, this function can pause its execution
# using the 'await' keyword.
# ------------------------------------------------------------------
async def process1():

    # Print the first step of process1.
    print("process-1 First Step")

    # Pause this coroutine for 3 seconds.
    #
    # asyncio.sleep() is a non-blocking sleep.
    #
    # During these 3 seconds, the Event Loop is free to execute
    # other coroutines instead of waiting idly.
    await asyncio.sleep(3)

    # This statement executes after the 3-second wait completes.
    print("process-1 Second Step")


# ------------------------------------------------------------------
# Another asynchronous coroutine.
# ------------------------------------------------------------------
async def process2():

    # Print the first step of process2.
    print("process-2 First Step")

    # Pause this coroutine for 6 seconds.
    #
    # While this coroutine is waiting,
    # the Event Loop can continue executing other coroutines.
    await asyncio.sleep(6)

    # Executes after the wait completes.
    print("process-2 Second Step")


# ------------------------------------------------------------------
# Main coroutine of the program.
#
# This acts as the entry point for all asynchronous tasks.
# ------------------------------------------------------------------
async def main():

    # --------------------------------------------------------------
    # asyncio.gather() executes multiple coroutines concurrently.
    #
    # Here, both process1() and process2() are scheduled together.
    #
    # Internally, the Event Loop starts both coroutines almost
    # at the same time.
    #
    # process1() → waits for 3 seconds
    # process2() → waits for 6 seconds
    #
    # Since both are running concurrently,
    # the total execution time is approximately 6 seconds,
    # not 3 + 6 = 9 seconds.
    #
    # gather() waits until ALL supplied coroutines complete.
    #
    # If the coroutines return values,
    # gather() returns them as a list in the same order they
    # were passed.
    #
    # In this example, neither coroutine returns anything,
    # so 'tasks' will contain:
    #
    # [None, None]
    # --------------------------------------------------------------
    tasks = await asyncio.gather(process1(), process2())

    # This statement executes only after BOTH coroutines finish.
    print("Main Completed")


# ------------------------------------------------------------------
# Start the asynchronous program.
#
# asyncio.run():
#
# 1. Creates the Event Loop.
# 2. Executes the main() coroutine.
# 3. Waits until it finishes.
# 4. Closes the Event Loop.
# ------------------------------------------------------------------
asyncio.run(main())
