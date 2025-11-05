COUNT = 0
ip = int(input("Enter Number of Terms: "))
a, b = 0, 1

if ip <= 0:
    print("Invalid Input")
    quit()

for i in range(ip):
    if i == 0 or i == 1:
        print(i)
        COUNT += 1
    else:
        nth = a + b
        a = b
        b = nth
        print(nth)
        COUNT += 4

print("Steps required using Counter:", COUNT)

     
#a   b  nth
#0   1   1
#1   1   2
#1   2   3
#2   3   5

Iterative Fibonacci Series – Theory

The Fibonacci series is a sequence where each term is the sum of the two preceding ones:
F(n) = F(n−1) + F(n−2)
with F(0) = 0, F(1) = 1.

In the iterative approach, we compute Fibonacci numbers using a loop rather than recursion.
We keep track of only the last two numbers and update them until we reach n.

Time Complexity

O(n) — one loop runs from 2 to n.

Space Complexity

O(1) — only a few variables (a, b) are used, no recursion stack.