# XOR Linked List

## Description

An XOR Linked List is a memory-efficient version of a Doubly Linked List that uses only one address field for each node, effectively reducing memory usage. This is achieved by using the bit-wise XOR operation to store the addresses of the previous and next nodes in a single field. 

## Problem Statement

Given a stream of data of size N for the linked list, your task is to complete the following functions:

1. **insert(data)**: This function inserts the given data at the beginning of the linked list.
2. **getList()**: This function returns the linked list as a list.

### Note:
A utility function `XOR(Node* a, Node* b)` is provided to get the bit-wise XOR of two Node pointers. Use this function to perform the XOR operation on the pointers when managing the linked list.

The driver code prints the returned list twice, once in forward order and once in reverse order.

## Examples

#### Example 1:
- **Input:** 
  - LinkedList: 9<->5<->4<->7<->3<->10
- **Output:** 
  - Forward: 10 3 7 4 5 9
  - Backward: 9 5 4 7 3 10

#### Example 2:
- **Input:** 
  - LinkedList: 58<->96<->31
- **Output:** 
  - Forward: 31 96 58
  - Backward: 58 96 31

## Complexity Analysis

- **Expected Time Complexity**: O(n) for inserting all nodes.
- **Expected Auxiliary Space**: O(1) since we are not using any additional data structures for storing the nodes.

## Constraints
- The number of nodes must be between 1 and 100,000.
- The data of nodes must also be between 1 and 100,000.

## Implementation

You can find the implementation of the `insert()` and `getList()` functions in the provided code files.

## Usage

To use the XOR Linked List:

1. Create an instance of the linked list.
2. Call the `insert(data)` method to add elements to the list.
3. Use the `getList()` method to retrieve the list and print it.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

