class UnionFind:
    def __init__(self):
        # Use dictionaries to dynamically store parent and size
        self.parent = {}  # Maps each node to its parent
        self.size = {}  # Maps each node to the size of its set
        self.num_sets = 0  # Total number of disjoint sets

    def find(self, x):
        # Iterative implementation of find with path compression
        root = x

    def union(self, x, y):
        # Union the sets containing x and y by attaching rootX's tree under rootY

    def connected(self, x, y):
        # Check if x and y belong to the same set

    def get_num_of_sets(self):
        # Return the current number of disjoint sets

    def get_size_of_set(self, x):
        # Return the size of the set containing x

    def add(self, x):
        #
        
        
uf = UnionFind()  # Initialize an empty Union-Find structure

# Add initial nodes
for i in range(8):  # Add nodes 0 to 7
    uf.add(i)
    
uf.union(1, 2)
uf.union(5, 2)
uf.union(6, 7)
uf.union(7, 2)

uf.union(0, 4)
uf.union(4, 3)

# Display the parent dictionary after all operations
print("Parent dictionary:", uf.parent)


# Test cases to verify correctness
print("Test Cases:")
assert uf.connected(1, 5), "Error: 1 and 5 should be connected."
assert uf.connected(6, 2), "Error: 6 and 2 should be connected."
assert uf.connected(0, 4), "Error: 0 and 4 should be connected."
assert not uf.connected(1, 0), "Error: 1 and 0 should not be connected."
assert uf.get_size_of_set(1) == 5, "Error: The size of the set containing 1 should be 5."
assert uf.get_size_of_set(0) == 3, "Error: The size of the set containing 0 should be 3."
assert uf.get_num_of_sets() == 2, "Error: There should be 2 disjoint sets."

# Test case: Adding an existing node should do nothing
initial_parent = uf.parent.copy()
initial_size = uf.size.copy()
initial_num_sets = uf.num_sets

uf.add(2)  # Node 2 already exists
assert uf.parent == initial_parent, "Error: Adding an existing node modified the parent dictionary."
assert uf.size == initial_size, "Error: Adding an existing node modified the size dictionary."
assert uf.num_sets == initial_num_sets, "Error: Adding an existing node modified the number of sets."

print("All tests passed, including existing node test!")
