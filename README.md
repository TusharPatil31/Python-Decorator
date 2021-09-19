# Python-Decorator

DESCRIPTION

Implement a Python decorator that should take whatever the decorated function returns, and write it to a file in a new line. For the sake of this problem, let us assume that the decorated functions always return a string. The decorator should be named log_message and should write to the file /tmp/decorator_logs.txt.

Objective: To develop a Python decorator

Domain:  Web Development

Steps to perform:            

Implement the following design
@log_message

def a_function_that_returns_a_string():

      return "A string"

@log_message

def a_function_that_returns_a_string_with_newline(s):

      return "{}\n".format(s)

@log_message

def a_function_that_returns_another_string(string=""):

            return "Another string"
