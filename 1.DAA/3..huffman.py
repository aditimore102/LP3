import heapq

# Node class for Huffman Tree
class Node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        self.freq = freq 
        self.symbol = symbol 
        self.left = left 
        self.right = right 
        self.huff = '' 

    def __lt__(self, nxt): 
        return self.freq < nxt.freq 

# Function to print Huffman codes
def printNodes(node, val=''): 
    newVal = val + str(node.huff) 
    if node.left: 
        printNodes(node.left, newVal) 
    if node.right: 
        printNodes(node.right, newVal) 
    if not node.left and not node.right: 
        print(f"{node.symbol} -> {newVal}") 

# --- USER INPUT ---
n = int(input("Enter number of characters: "))

chars = []
freq = []

for i in range(n):
    ch = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of '{ch}': "))
    chars.append(ch)
    freq.append(f)

# Build Huffman Tree
nodes = []
steps = 0

# Step 1: Push all nodes to heap
for j in range(len(chars)): 
    heapq.heappush(nodes, Node(freq[j], chars[j])) 
    steps += 1  # count as one step per insertion

# Step 2: Combine nodes until one tree remains
while len(nodes) > 1: 
    left = heapq.heappop(nodes) 
    right = heapq.heappop(nodes) 

    left.huff = 0
    right.huff = 1

    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right) 
    heapq.heappush(nodes, newNode) 

    steps += 1  # count one step per merge

# Output Huffman codes
print("\nHuffman Codes:")
printNodes(nodes[0]) 

print("\nTotal steps required:", steps)

#Huffman Coding is a greedy algorithm that builds an optimal binary tree for data compression with
Time Complexity = O(n log n) and Space Complexity = O(n).
Huffman Coding is a data compression technique that reduces the size of data without losing information.
It gives shorter binary codes to characters that occur more often, and longer codes to those that occur less often.

🔹 How It Works

List all characters and their frequencies.

Put them into a min-heap (smallest frequency on top).

Pick the two smallest nodes and combine them into a new node (sum of their frequencies).

Repeat until there is only one node left — this becomes the root of the Huffman Tree.

Assign 0 to every left edge and 1 to every right edge.

Read the codes from root to each character — that’s the Huffman code.

Graph drawn by: no.of item and step requried by program