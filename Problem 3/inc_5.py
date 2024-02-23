"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Emma J. Verdugo
Lab Time: @2pm
"""

def inc_5():
    # Write your code here
    num_1 = int(input())
    num_2 = int(input())
    
    if num_2<num_1:
        print ("Second integer can't be less than the first. ")
    else:
        while num_1 <= num_2:
            print(num_1, end=" ")
            num_1+=5
        print()
        
if __name__ == "__main__":
    inc_5()