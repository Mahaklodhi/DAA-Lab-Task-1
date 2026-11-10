# DAA-Lab-Task-1

## Part 1: Array and Sorting

Input: [8, 3, 15, 6, 2]

Output:

Largest number = 15

Total comparisons = 4

Sorted array = [2, 3, 6, 8, 15]

### Dry Run

First, I take 8 as the largest number. Then I compare each number with it. When I get 15, I update the largest number to 15.

After that, I sort the array using Bubble Sort.

Time Complexity = O(n²)

## Part 2: Stack and Queue

Input: Task1, Task2, Task3, Task4, Task5

### Stack Output

Task5, Task4, Task3, Task2, Task1

### Queue Output

Task1, Task2, Task3, Task4, Task5

### Explanation

Stack follows LIFO, which means the last task added comes out first.

Queue follows FIFO, which means the first task added comes out first.

A printer uses Queue because tasks are printed in the order they arrive.

## Part 3: Tree

### Tree Structure

Math
  Algebra
  Geometry

Science
  Physics
  Chemistry

### Level Order Traversal

Math, Science, Algebra, Geometry, Physics, Chemistry

### Explanation

First, Math and Science are visited. Then their child nodes are visited one by one.

Queue is used for level order traversal.

Time Complexity = O(n)

## Part 4: Time Complexity

### Single Loop

The loop runs from 1 to 5.

Total runs = 5

For n = 20, total runs = 20.

### Nested Loop

Both loops run 5 times.

Total prints = 25

For n = 10, total runs = 100.

### Explanation

A single loop has O(n) time complexity.

A nested loop has O(n²) time complexity.

## Conclusion

In this lab, I learned about arrays, sorting, stack, queue, trees and time complexity.

## How to Run

Use these commands to run the programs.

```bash
python part1_trace.py
python part2_stack_queue.py
python part3_tree.py
python part4_complexity.py
```
