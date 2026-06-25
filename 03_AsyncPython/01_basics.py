# Import the asyncio module.
#
# asyncio is Python's built-in library for writing asynchronous programs.
#
# It allows multiple tasks to run concurrently without creating multiple
# threads or processes.
#
# Instead of blocking while waiting (for an API, database, file, etc.),
# an async function can "pause" itself and allow other async tasks
# to execute.
import asyncio


# Import the time module.
#
# NOTE:
# In this program, the time module is imported but never used.
#
# It would normally be used for:
# time.sleep()
#
# However, in asynchronous programming we should prefer:
# asyncio.sleep()
#
# because time.sleep() blocks the entire program,
# whereas asyncio.sleep() only pauses the current coroutine.
import time


# ------------------------------------------------------------------
# Define an asynchronous function (coroutine).
#
# async def creates a coroutine instead of a normal function.
#
# A coroutine:
#
# ✔ Can pause execution.
# ✔ Can resume later.
# ✔ Can await other coroutines.
#
# Unlike a normal function, this function does not execute immediately
# when called.
#
# Calling:
#
# process1()
#
# simply creates a coroutine object.
#
# It starts executing only when the event loop runs it.
# ------------------------------------------------------------------
async def process1():

    # First step of Process 1.
    print("process-1 First Step")

    # --------------------------------------------------------------
    # await tells Python:
    #
    # "Pause this coroutine until the awaited operation completes."
    #
    # asyncio.sleep(6)
    #
    # does NOT block the entire program.
    #
    # Instead:
    #
    # ✔ process1 pauses
    # ✔ Event Loop gets control back
    # ✔ Other async tasks (if any) can execute
    #
    # In real-world applications,
    # instead of sleep(), this could be:
    #
    # - API call
    # - Database query
    # - File download
    # - LLM request
    # - HTTP request
    # --------------------------------------------------------------
    await asyncio.sleep(6)

    # --------------------------------------------------------------
    # Call another asynchronous function.
    #
    # Since process2() is also async,
    # it must be awaited.
    #
    # Python pauses process1 until process2 completes.
    #
    # The returned value is stored in 'result'.
    # --------------------------------------------------------------
    result = await process2()

    # Execution resumes here only after process2 finishes.
    print("process-1 Second Step")

    # Print the value returned by process2().
    print(f"process2 result {result}")


# ------------------------------------------------------------------
# Another asynchronous coroutine.
# ------------------------------------------------------------------
async def process2():

    # First step.
    print("process-2 First Step")

    # Pause this coroutine for 9 seconds.
    #
    # Again,
    # this is a non-blocking wait.
    #
    # While this coroutine is waiting,
    # the event loop can execute other async tasks.
    await asyncio.sleep(9)

    # Executed after the wait completes.
    print("process-2 Second Step")

    # Return a value back to the caller.
    #
    # In this program,
    # process1 receives this value.
    return "process-2 completed"


# ------------------------------------------------------------------
# asyncio.run() is the entry point of an asynchronous program.
#
# It performs three important tasks:
#
# 1. Creates an Event Loop.
# 2. Runs the given coroutine.
# 3. Closes the Event Loop after completion.
#
# Without asyncio.run(),
# async functions would never execute.
#
# Calling:
#
# process1()
#
# only creates a coroutine object.
#
# Calling:
#
# asyncio.run(process1())
#
# actually starts executing the coroutine.
# ------------------------------------------------------------------
asyncio.run(process1())