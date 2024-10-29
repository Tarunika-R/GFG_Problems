# Parenthesis Checker

## Problem Statement

You are given a string `s` representing an expression containing various types of brackets: `{}`, `()`, and `[]`. Your task is to determine whether the brackets in the expression are balanced. A balanced expression is one where every opening bracket has a corresponding closing bracket in the correct order.

## Examples

1. **Input:** `s = "{([])}"`
   - **Output:** `true`
   - **Explanation:** Same colored brackets can form balanced pairs, with 0 number of unbalanced brackets.

2. **Input:** `s = "()"`
   - **Output:** `true`
   - **Explanation:** Same bracket can form balanced pairs, and here only 1 type of bracket is present and in a balanced way.

3. **Input:** `s = "([]"`
   - **Output:** `false`
   - **Explanation:** Square bracket is balanced but the small bracket is not balanced. Hence, the output will be unbalanced.

## Constraints

- \(1 \leq \text{s.size()} \leq 10^6\)
- \(s[i] \in \{ '{', '}', '(', ')', '[', ']' \}\)