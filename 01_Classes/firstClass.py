# Define a class named 'llms'.
# A class is a blueprint or template used to create objects.
# It groups together data (variables) and behavior (methods/functions)
# related to a particular entity.
class llms:

    # ---------------------- Class Variable ----------------------
    # This is a class variable.
    # Class variables are shared among all objects created from this class.
    # Every object will have access to the same value unless it is overridden.
    #
    # Example:
    # obj1.token_size -> 100
    # obj2.token_size -> 100
    #
    # This is useful when a value should remain common across every object.
    token_size = 100

    # ---------------------- Constructor ----------------------
    # The __init__() method is called automatically whenever
    # a new object of this class is created.
    #
    # 'self' refers to the current object being created.
    # 'query' is the value passed while creating the object.
    #
    # Example:
    # obj = llms("Hello")
    #
    # Here,
    # self -> obj
    # query -> "Hello"
    def __init__(self, query):

        # Store the value received in the constructor
        # inside the object as an instance variable.
        #
        # Instance variables are unique for every object.
        #
        # Example:
        # obj1.query = "Hello"
        # obj2.query = "How are you?"
        #
        # Each object maintains its own copy.
        self.query = query

    # ---------------------- Instance Method ----------------------
    # This method belongs to every object of the class.
    # It can access all instance variables using 'self'.
    def openai(self):

        # Access the object's query using self.query.
        # The f-string inserts the value dynamically into the string.
        print(f"I am openai. You asked {self.query}")

    # Another instance method.
    # Currently, it simply prints a fixed message.
    def claude(self):
        print("I am claude")

    # Another instance method.
    def llama(self):
        print("I am llama")


# ------------------------------------------------------------------
# __name__ is a special built-in Python variable.
#
# When this file is executed directly,
# __name__ becomes "__main__".
#
# When this file is imported into another Python file,
# __name__ becomes the module's filename instead.
#
# This condition ensures that the below code runs
# only when this file is executed directly.
# ------------------------------------------------------------------
if __name__ == "__main__":

    # ---------------------- Object Creation ----------------------
    # Create an object named 'obj' from the llms class.
    #
    # Python internally performs something similar to:
    #
    # obj = llms.__new__(llms)
    # obj.__init__("Ansh is Ansh")
    #
    # The constructor (__init__) stores
    # "Ansh is Ansh" inside obj.query.
    obj = llms("Ansh is Ansh")

    # ---------------------- Method Call ----------------------
    # Call the openai() method using the object.
    #
    # Internally, Python converts:
    # obj.openai()
    #
    # into:
    # llms.openai(obj)
    #
    # Therefore, 'self' automatically refers to obj.
    #
    # The method prints:
    # I am openai. You asked Ansh is Ansh
    #
    # Note:
    # openai() does NOT return anything explicitly.
    # Every Python function without a return statement
    # automatically returns None.
    #
    # Therefore:
    # print(obj.openai())
    #
    # First prints:
    # I am openai. You asked Ansh is Ansh
    #
    # Then prints:
    # None
    print(obj.openai())