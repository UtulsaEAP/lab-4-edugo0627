"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Emma J. Verdugo
Lab Time: @2pm
"""

def norm():
    # Write your code here
    num = int(input())
    vals_entered =[]
    for i in range(0,num):
        next_num = input()
        vals_entered.append(float(next_num))
    #vals_entered = num.split(",")
    max_nm = max(vals_entered)
    
    
    
    for i in range(0,len(vals_entered)):
        #vals_entered[i]=float(vals_entered[i])
        vals_entered[i] /= float(max_nm)
        print(f"{vals_entered[i]:.2f}")
        
    # some_list = []
    # max_num = float('-inf')
    # for i in some_list:
    #     if i > max_num:
    #         max_num = i
        
    
    # for x in range(int(num)):
    #     val = (input())
    #     vals_entered.append(val)
    #     if (x == 0):
    #         max = val
    #     else:
    #         if val > max:
    #             max = val
                
    # for vals in vals_entered:
    #     your_value = num/max
    #     print(f'{your_value:.2f}')  
    # # ^ forget this, trying something different
    # # loop over range of list and input_list[i] = input_list[i]/mas(input_list)
    # #need user input list  input_list = list(input())
    
    # num_input = int(input())


    
if __name__ == "__main__":
    norm()