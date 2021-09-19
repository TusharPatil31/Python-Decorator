def log_message(decFunc):                      #decoFunc is the function passed to decorator
    def foo(*args,**kwargs):
        res = decFunc(*args,**kwargs)          #get the return value (string) from passed function
        with open('LogFile.txt','a') as f:     #open a new file in append mode to write
            f.write(res+"\n")                  #write every string in new line
        return res                             #return output
    return foo                                 #return decorator function

@log_message
def a_function_that_returns_a_string():
    return "A string"

@log_message
def a_function_that_returns_a_string_with_newline(s):
    return "{}\n".format(s)

@log_message
def a_function_that_returns_another_string(string=""):
    return "Another string"

a_function_that_returns_a_string()
a_function_that_returns_a_string_with_newline("Hey there!")
a_function_that_returns_another_string()