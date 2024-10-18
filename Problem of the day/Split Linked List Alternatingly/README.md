# Split Linked List Alternatingly

## Problem Statement

Given the head of a singly linked list, the task is to split the linked list into two smaller lists. The sublists should be made from alternating elements from the original list. The order of elements in the sublists should respect the order of elements in the original list.

### Examples:

1. **Input:** LinkedList = 0->1->0->1->0->1
   - **Output:** 0->0->0 , 1->1->1
   - **Explanation:** After forming two sublists of the given list as required, we have two lists as: 0->0->0 and 1->1->1.

2. **Input:** LinkedList = 2->5->8->9->6
   - **Output:** 2->8->6 , 5->9
   - **Explanation:** After forming two sublists of the given list as required, we have two lists as: 2->8->6 and 5->9.

3. **Input:** LinkedList = 7
   - **Output:** 7 , <empty linked list>
   - **Explanation:** With only one element, the first sublist contains the single element, and the second sublist is empty.

### Constraints:
- 1 <= number of nodes <= 100
- 1 <= node->data <= 10^4

## Solution

### Approach:
- Use a flag to alternate between appending nodes to two new lists.
- Traverse the original linked list, appending each node alternatively to one of the two new lists based on the flag.
- Toggle the flag after appending each node.