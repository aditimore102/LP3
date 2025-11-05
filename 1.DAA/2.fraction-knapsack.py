class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def fractionalKnapsack(W, arr):
    steps = 0  # step counter

    # Step 1: Sort items by profit/weight ratio (descending)
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    steps += len(arr) * 2  # approx. comparisons + calculations

    finalvalue = 0.0

    # Step 2: Pick items into the knapsack
    for item in arr:
        steps += 1  # counting each item check
        if item.weight <= W:
            W -= item.weight
            finalvalue += item.profit
            steps += 2  # subtraction + addition
        else:
            finalvalue += item.profit * W / item.weight
            steps += 3  # multiply, divide, add
            break

    print("\nTotal steps required:", steps)
    return finalvalue


if __name__ == "__main__":
    # User input section
    n = int(input("Enter number of items: "))
    arr = []

    for i in range(n):
        profit = float(input(f"Enter profit of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        arr.append(Item(profit, weight))

    W = float(input("Enter capacity of knapsack: "))

    # Compute maximum value
    max_val = fractionalKnapsack(W, arr)
    print("\nMaximum value in Knapsack =", max_val)

#fractional Knapsack Problem — Theory
🔹 Problem Definition

The Fractional Knapsack Problem is a greedy algorithm problem in optimization.
You are given:

A set of n items, each with:

value (vᵢ)

weight (wᵢ)

A knapsack that can hold a maximum weight W.

You need to:

Maximize the total value in the knapsack

You can take fractions of items (i.e., you can break items).
Time complexity:O(nlog n)
Space complexity:0(1) , or  if sorting O(1)

Graph drawn by : no. of item and steps requried to solve 