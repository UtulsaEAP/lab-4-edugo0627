"""
Complete the following python code to reverse the string entered by the user.

Name: Emma J. Verdugo
Lab Time: @2pm
"""

def reverse_string():
    # YOUR CODE HERE
   input_string = input()
   while input_string != "Done" and  input_string != "done" and  input_string != "d":
       re_string = ""
       for char in input_string:
           re_string = char + re_string
       print(re_string)
       input_string = input()
       

if __name__ == "__main__":
    reverse_string()