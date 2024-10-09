class Node:
    def __init__(self, data):
        self.data = data
        self.npx = 0  # XOR of next and previous node addresses

def XOR(a, b):
    return a ^ b if a and b else a if a else b  # XOR operation on addresses

def insert(head, data):
    new_node = Node(data)
    
    if head is None:
        head = new_node
    else:
        # The new node's npx is XOR of None (0) and current head's address
        new_node.npx = id(head)  # XOR with the address of the current head
        # Update the head's npx to reflect the new node
        head.npx = XOR(new_node.npx, head.npx)  # Update head's npx with new node
        head = new_node  # Move head to the new node
    
    return head

def getList(head):
    def get_node_by_id(node_id, node_map):
        if node_id == 0:
            return None
        for node in node_map:
            if id(node) == node_id:
                return node
        return None

    # Traverse forward
    prev_id = 0
    current = head
    node_map = []  # To store the nodes for simulating memory addresses
    forward_result = []
    while current:
        node_map.append(current)
        forward_result.append(current.data)  # Store data for forward traversal
        next_id = XOR(prev_id, current.npx)
        prev_id = id(current)
        current = get_node_by_id(next_id, node_map)
    
    # Traverse backward using the last node in the node_map
    prev_id = 0
    current = node_map[-1] if node_map else None
    backward_result = []
    while current:
        backward_result.append(current.data)  # Store data for backward traversal
        next_id = XOR(prev_id, current.npx)
        prev_id = id(current)
        current = get_node_by_id(next_id, node_map)
    
    # Return both the forward and backward traversals as lists
    return forward_result, backward_result

# Test the implementation
head = None
# Insert elements into the XOR linked list
elements = [6]  # Example with the number 6
for element in elements:
    head = insert(head, element)

# Get the forward and backward traversal lists
forward_traversal, backward_traversal = getList(head)

# Print each element individually (without square brackets)
for item in forward_traversal:
    print(item)

for item in backward_traversal:
    print(item)