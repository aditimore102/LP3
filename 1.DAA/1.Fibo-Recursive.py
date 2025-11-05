COUNT=0
def recur_fibo(n):  
    global COUNT
    COUNT +=1
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  

ip = int(input("How many terms? "))  
if ip <= 0:
    print("Plese enter a positive integer")  
else:  
    print("Fibonacci sequence:")  
    for i in range(ip):
        print(recur_fibo(i))

print("Steps reqired using Counter ", COUNT)

Iterative Approach – Explanation

Instead of using recursion (which calls itself repeatedly), the iterative approach uses a simple loop.
This avoids repeated calculations and extra memory use.
🔹 Time Complexity: O(n)
Space Complexity: O(1)