class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def fractionalKnapsack(W, arr):
    steps = 0  # Step counter

    # Step 1: Sort items by profit/weight ratio (descending)
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    steps += len(arr) * 2  # Rough count for ratio calculations and comparisons

    finalvalue = 0.0
    print("\n--- Step-by-step selection ---")

    # Step 2: Process each item
    for i, item in enumerate(arr, start=1):
        steps += 1  # Counting each loop iteration

        if item.weight <= W:
            # Take the full item
            W -= item.weight
            finalvalue += item.profit
            steps += 2  # one subtraction, one addition
            print(f"Step {steps}: Took full item {i} (Profit={item.profit}, Weight={item.weight})")
        else:
            # Take fraction of the item
            fraction = W / item.weight
            finalvalue += item.profit * fraction
            steps += 3  # division, multiplication, addition
            print(f"Step {steps}: Took {fraction*100:.2f}% of item {i} (Profit={item.profit}, Weight={item.weight})")
            W = 0
            break  # knapsack is full

    print("\nTotal steps required:", steps)
    return finalvalue


if __name__ == "__main__":
    # --- USER INPUT SECTION ---
    n = int(input("Enter number of items: "))
    arr = []

    for i in range(n):
        profit = float(input(f"Enter profit of item {i+1}: "))
        weight = float(input(f"Enter weight of item {i+1}: "))
        arr.append(Item(profit, weight))

    W = float(input("Enter capacity of knapsack: "))

    # --- FUNCTION CALL ---
    max_val = fractionalKnapsack(W, arr)
    print("\nMaximum value in Knapsack =", max_val)


#THERORY -
The Fractional Knapsack Problem is a classic Greedy Algorithm problem in which the goal is to maximize the total profit/value that can be put into a knapsack of limited capacity.

Unlike the 0/1 Knapsack Problem, here we are allowed to take fractions of items instead of taking the whole item or leaving it.

Time complexity - O(n log n)
Space complexity - O(n)