# Import the threading module.
#
# NOTE:
# In this program, the threading module is imported but never used directly.
# ThreadPoolExecutor internally creates and manages threads for us.
#
# If we were manually creating threads, we would use:
# threading.Thread(...)
import threading


# Import ThreadPoolExecutor from Python's concurrent.futures module.
#
# ThreadPoolExecutor is a high-level API for multithreading.
#
# Instead of manually creating, starting, joining, and destroying threads,
# ThreadPoolExecutor automatically:
#
# ✔ Creates worker threads
# ✔ Assigns tasks to available threads
# ✔ Waits for completion
# ✔ Cleans up all threads
#
# This is the recommended way of performing multithreading in Python.
from concurrent.futures import ThreadPoolExecutor


# ------------------------------------------------------------------
# Function executed by each thread.
#
# Every worker thread will execute this function independently.
#
# The function expects one dictionary as input.
#
# Example input:
# {
#     "src": "table-1",
#     "dest": "table-1"
# }
# ------------------------------------------------------------------
def transformation(input):

    # Extract source table name.
    src = input['src']

    # Extract destination table name.
    dest = input['dest']

    # Simulate reading data from the source.
    print(f"Reading from {src}")

    # Simulate performing some transformation.
    print(f"Transforming.....")

    # Simulate writing transformed data.
    print(f"Writing data to {dest}")

    # Return the status after processing.
    #
    # Every thread returns its own result independently.
    return f"Done {src} to {dest}"


# ------------------------------------------------------------------
# List containing multiple transformation jobs.
#
# Each dictionary represents one independent task.
#
# Since these tasks do not depend on each other,
# they are perfect candidates for multithreading.
# ------------------------------------------------------------------
array = [

    # Task 1
    {
        "src": "table-1",
        "dest": "table-1"
    },

    # Task 2
    {
        "src": "table-2",
        "dest": "table-2"
    },

    # Task 3
    {
        "src": "table-3",
        "dest": "table-3"
    }
]


# ------------------------------------------------------------------
# Create a ThreadPoolExecutor.
#
# max_workers=3 means:
#
# At most 3 threads can execute simultaneously.
#
# Internally:
#
# Thread-1
# Thread-2
# Thread-3
#
# will be created and reused.
#
# The "with" statement automatically:
#
# 1. Creates the thread pool.
# 2. Executes all tasks.
# 3. Waits for every thread to finish.
# 4. Closes the thread pool safely.
# ------------------------------------------------------------------
with ThreadPoolExecutor(max_workers=3) as executor:

    # --------------------------------------------------------------
    # executor.map() works similarly to Python's built-in map().
    #
    # Syntax:
    #
    # executor.map(function, iterable)
    #
    # Here:
    #
    # Function  -> transformation
    # Iterable  -> array
    #
    # The executor automatically assigns one element of the array
    # to one available worker thread.
    #
    # Internally, something similar happens:
    #
    # Thread-1 → transformation(array[0])
    # Thread-2 → transformation(array[1])
    # Thread-3 → transformation(array[2])
    #
    # Since max_workers=3 and there are exactly 3 tasks,
    # all three tasks can run concurrently.
    #
    # If there were 10 tasks:
    #
    # Thread-1 → Task1 → Task4 → Task7 ...
    # Thread-2 → Task2 → Task5 → Task8 ...
    # Thread-3 → Task3 → Task6 → Task9 ...
    #
    # Threads are reused automatically until all tasks finish.
    #
    # executor.map() returns an iterator containing the return values
    # from each function call.
    #
    # IMPORTANT:
    # Even though execution happens concurrently,
    # the returned results preserve the ORIGINAL ORDER
    # of the input iterable.
    # --------------------------------------------------------------
    my_futures = executor.map(transformation, array)


# ------------------------------------------------------------------
# Convert the iterator into a list.
#
# This collects all returned values from every thread.
#
# Since transformation() returns:
#
# "Done table-x to table-x"
#
# the final list becomes:
#
# [
#   "Done table-1 to table-1",
#   "Done table-2 to table-2",
#   "Done table-3 to table-3"
# ]
#
# NOTE:
# The print statements inside transformation()
# may appear in any order because multiple threads
# execute simultaneously.
#
# However,
#
# list(my_futures)
#
# always preserves the input order.
# ------------------------------------------------------------------
print(f"The returned values are {list(my_futures)}")