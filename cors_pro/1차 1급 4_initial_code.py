#You may use import as below.
#import math

def solution(num):
    # Write code here.
    answer = 0
    num += 1
    strnum = str(num)
    
    strnum = strnum.replace("0", "1")

    answer = int("".join(strnum))
    
    return answer


#The following is code to output testcase.
num = 9949999
ret = solution(num)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret, ".")