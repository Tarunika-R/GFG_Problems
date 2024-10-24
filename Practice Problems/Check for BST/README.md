# Check for BST

## Problem Statement

Given the root of a binary tree, the task is to check whether it is a Binary Search Tree (BST) or not. A BST is defined by the following properties:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

**Note:** BSTs cannot contain duplicate nodes.

## Examples

1. **Input:**
   2
  / \
 1   3
      \
       5
**Output:** `true`
- **Explanation:** The left subtree of every node contains smaller keys, and the right subtree of every node contains greater keys. Hence, the tree is a BST.

---

2. **Input:**
   2
    \
     7
      \
       6
        \
         9
**Output:** `false`
- **Explanation:** Since the node with value 7 has right subtree nodes with keys less than 7, this is not a BST.

---

3. **Input:**
   10
  /  \
 5    20
     /  \
    9   25
**Output:** `false`
- **Explanation:** The node with value 9 is present in the right subtree of 10, but it is smaller than 10.

## Constraints

- \(1 \leq \text{Number of nodes} \leq 10^5\)
- \(1 \leq \text{Data of a node} \leq 10^5\)

## Expected Time Complexity

- \(O(n)\), where \(n\) is the number of nodes in the given tree.

## Expected Auxiliary Space

- \(O(\text{Height of the tree})\)