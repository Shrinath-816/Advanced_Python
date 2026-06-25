# Import the 'llms' class from the file named 'firstClass.py'.
# This allows us to inherit all the properties (variables) and
# methods (functions) defined inside the llms class.
from firstClass import llms


# ------------------------------------------------------------------
# Define a new class named 'chatbot'.
#
# The syntax:
# class chatbot(llms):
#
# means that 'chatbot' is inheriting from the 'llms' class.
#
# This is called Inheritance in Object-Oriented Programming (OOP).
#
# Inheritance allows the child class (chatbot) to reuse all the
# methods and variables of the parent class (llms) without
# writing them again.
#
# Parent Class (Base Class)  -> llms
# Child Class (Derived Class)-> chatbot
# ------------------------------------------------------------------
class chatbot(llms):

    # ---------------------- Constructor ----------------------
    # This constructor initializes objects of the chatbot class.
    #
    # Parameters:
    # model -> stores which LLM is being used
    # query -> user query that will be passed to the parent class
    def __init__(self, model, query):

        # Create a new instance variable named 'model'.
        # This variable belongs only to chatbot objects.
        self.model = model

        # Call the constructor of the parent class (llms).
        #
        # Why?
        # Because the parent constructor initializes self.query.
        #
        # Without calling it,
        # self.query would never be created.
        #
        # This is equivalent to:
        # self.query = query
        #
        # but using the parent constructor avoids rewriting code.
        llms.__init__(self, query)

        # A more Pythonic way is:
        # super().__init__(query)

    # ---------------------- Child Class Method ----------------------
    # This method is unique to the chatbot class.
    def showme(self):

        # NOTE:
        # Since the string is enclosed inside normal quotes,
        # {self.model} will NOT be replaced by its value.
        #
        # Output will literally be:
        # I am calling {self.model}.
        #
        # To insert the variable's value, use an f-string:
        #
        # print(f"I am calling {self.model}.")
        print("I am calling {self.model}.")

        # NOTE:
        # This line contains an error.
        #
        # openai() is an instance method.
        # Instance methods require an object (self).
        #
        # Calling:
        # llms.openai()
        #
        # is equivalent to calling a function without passing
        # the required 'self' parameter.
        #
        # It should be either:
        #
        # self.openai()
        #
        # OR
        #
        # llms.openai(self)
        #
        # Both tell Python which object should be used.
        llms.openai()


# ------------------------------------------------------------------
# Create an object of the chatbot class.
#
# During object creation:
#
# chatbot("openai", "Hey, I am Ansh Lamba")
#
# Python automatically calls:
#
# chatbot.__init__(
#     self,
#     "openai",
#     "Hey, I am Ansh Lamba"
# )
#
# After initialization:
#
# self.model = "openai"
# self.query = "Hey, I am Ansh Lamba"
# ------------------------------------------------------------------
obj_inherit = chatbot("openai", "Hey, I am Ansh Lamba")


# ------------------------------------------------------------------
# Even though chatbot does not define an openai() method,
# it inherits the openai() method from the llms class.
#
# Therefore Python searches:
#
# 1. chatbot class
# 2. Parent class (llms)
#
# It finds openai() inside llms and executes it.
#
# Since openai() only prints a message and does not return anything,
# it automatically returns None.
#
# Therefore:
#
# print(obj_inherit.openai())
#
# will first print:
# I am openai. You asked Hey, I am Ansh Lamba
#
# and then print:
# None
# ------------------------------------------------------------------
print(obj_inherit.openai())