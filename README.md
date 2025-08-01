# Sudoku Block Validator

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Course](https://img.shields.io/badge/MOOC.fi-Python%20Programming-lightgrey)
![Points](https://img.shields.io/badge/Points-1%2F1-success)

A Python function that validates 3×3 blocks in a Sudoku grid, ensuring each number 1-9 appears at most once per block. This solution demonstrates 2D array block traversal, debugging techniques, and code refactoring for improved maintainability.

---

## 📖 Problem Description

Write a function named `block_correct(sudoku: list, row_no: int, column_no: int)` that validates a 3×3 block starting from the given row and column coordinates. The function checks whether the block follows Sudoku rules: each number 1-9 appears at most once.

### Important Notes
- **Flexible positioning**: Unlike standard Sudoku, this function can check ANY 3×3 block starting from ANY coordinates
- **Standard Sudoku blocks** start at: (0,0), (0,3), (0,6), (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)
- **This implementation** allows checking blocks from any position for testing purposes

### Example Blocks
- `block_correct(sudoku, 0, 0)` checks:
  ```
  9 0 0
  2 0 0  
  0 2 0
  ```
  **Result: False** (duplicate 2)

- `block_correct(sudoku, 1, 2)` checks:
  ```
  0 2 5
  0 3 0
  4 0 0
  ```
  **Result: True** (no duplicates)

---

## 💻 Final Solution

```python
def block_correct(sudoku: list, row_num: int, col_num: int):
    block = []
    for row in range(row_num, row_num + 3):
        for column in range(col_num, col_num + 3):
            number = sudoku[row][column]
            if number > 0 and number in block:
                return False
            block.append(number)
    return True

if __name__ == "__main__":
    sudoku = [
        [9, 0, 0, 0, 8, 0, 3, 0, 0],
        [2, 0, 0, 2, 5, 0, 7, 0, 0],
        [0, 2, 0, 3, 0, 0, 0, 0, 4],
        [2, 9, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 7, 3, 0, 5, 6, 0],
        [7, 0, 5, 0, 6, 0, 4, 0, 0],
        [0, 0, 7, 8, 0, 3, 9, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 3],
        [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    print(block_correct(sudoku, 0, 0))  # False
    print(block_correct(sudoku, 1, 2))  # True
```

**Output:**
```
False
True
```

---

## 🐛 Original Solution & The Bug Hunt

### **Initial Approach (Had Issues)**
```python
def block_correct(sudoku: list, col_num: int, row_num: int):
    block = []
    for row in sudoku[col_num : col_num + 3]:
        for num in row[row_num : row_num + 3]:
            if num > 0 and num in block:
                return False
            block.append(num)
    return True
```

### **The Problem**
- **Parameter Confusion**: Mixed up `col_num` and `row_num` usage
- **Slicing Issues**: Incorrectly sectioned off quadrants
- **Maintainability**: Hard to understand and debug

### **Debugging Process**
1. **Hard-coded Testing**: Manually input coordinates and printed corresponding sections
2. **Trial and Error**: Tested different coordinate combinations
3. **Print Debugging**: Visualized which blocks were actually being checked
4. **Pattern Recognition**: Figured out the correct indexing pattern

---

## 🔧 Development Journey & Problem-Solving

### **Initial Challenges**
- **Coordinate Confusion**: Mixing up row/column parameter order
- **Block Extraction**: Difficulty visualizing 3×3 block boundaries
- **Indexing Logic**: Incorrect slicing led to wrong block sections

### **Debugging Strategy**
```python
# Debug approach used during development
def debug_block_extraction(sudoku, row_num, col_num):
    print(f"Checking block starting at ({row_num}, {col_num}):")
    for r in range(row_num, row_num + 3):
        for c in range(col_num, col_num + 3):
            print(sudoku[r][c], end=" ")
        print()  # New line after each row
```

### **Key Insights from Debugging**
1. **Visual Debugging**: Printing actual block contents revealed indexing errors
2. **Parameter Order**: Realized the importance of consistent parameter naming
3. **Range Logic**: `range(start, start + 3)` is clearer than slicing for this use case

---

## 🛠 Algorithm Explanation

The final solution uses **nested range loops** for clear, maintainable block traversal:

1. **Outer Loop**: Iterate through 3 rows starting from `row_num`
2. **Inner Loop**: Iterate through 3 columns starting from `col_num`
3. **Extract Element**: Get `sudoku[row][column]` for each position
4. **Duplicate Check**: If number > 0 and already seen, return `False`
5. **Track Numbers**: Add each number to tracking list
6. **Success**: Return `True` if no duplicates found

**Time Complexity:** O(1) - Always checks exactly 9 elements  
**Space Complexity:** O(1) - Block list never exceeds 9 elements

---

## 🧪 Test Cases

```python
# Test case 1: Standard Sudoku blocks
sudoku1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(block_correct(sudoku1, 0, 0))  # True - valid complete block

# Test case 2: Block with duplicates
sudoku2 = [[1, 2, 1], [4, 5, 6], [7, 8, 9]]
print(block_correct(sudoku2, 0, 0))  # False - duplicate 1

# Test case 3: Block with zeros
sudoku3 = [[1, 0, 0], [0, 5, 0], [0, 0, 9]]
print(block_correct(sudoku3, 0, 0))  # True - zeros don't count

# Test case 4: Non-standard position
sudoku4 = [[0, 1, 2, 3], [0, 4, 5, 6], [0, 7, 8, 9], [0, 0, 0, 0]]
print(block_correct(sudoku4, 0, 1))  # True - checking middle block
```

---

## ✨ Code Refactoring Insights

### **Why Refactor?**
The original solution worked but had **maintainability issues**:
- **Parameter misuse**: Confusing variable names
- **Complex slicing**: Hard to understand block extraction logic
- **Debugging difficulty**: Unclear what coordinates map to which blocks

### **Improvements in Final Version**
1. **Clear Parameters**: `row_num` and `col_num` match their usage
2. **Explicit Loops**: `range()` loops are more readable than slicing
3. **Direct Indexing**: `sudoku[row][column]` is clearer than nested slicing
4. **Better Variable Names**: `number` is more descriptive than `num`

### **Maintainability Benefits**
- **Easier Debugging**: Can easily print `(row, column)` coordinates
- **Clear Logic Flow**: Nested loops mirror the 2D structure
- **Flexible Testing**: Easy to test different block positions

---

## 🎯 Sudoku Context

### **Standard Sudoku Blocks**
In a real Sudoku game, there are 9 fixed 3×3 blocks:
```
Block positions:
(0,0) (0,3) (0,6)
(3,0) (3,3) (3,6)  
(6,0) (6,3) (6,6)
```

### **This Implementation's Flexibility**
- Can validate **any** 3×3 block starting from **any** position
- Useful for testing and educational purposes
- Foundation for complete Sudoku validation systems

---

## 🔍 Alternative Approach

While the current implementation is clear, here's the original slicing approach (fixed):

### Corrected Slicing Version:
```python
def block_correct_slicing(sudoku: list, row_num: int, col_num: int):
    block = []
    for row in sudoku[row_num:row_num + 3]:
        for num in row[col_num:col_num + 3]:
            if num > 0 and num in block:
                return False
            block.append(num)
    return True
```

---

## 📚 Key Learning Outcomes

* **2D Array Block Processing**: Understanding how to extract rectangular sections
* **Debugging Techniques**: Using print statements and hard-coded inputs to find bugs
* **Code Refactoring**: Improving maintainability while preserving functionality
* **Parameter Management**: Importance of clear, consistent parameter naming
* **Problem Decomposition**: Breaking complex 2D problems into manageable steps
* **Visual Debugging**: Using printed output to understand algorithm behavior

---

## 💡 Developer Reflection

*"This challenge taught me the value of refactoring for maintainability. Sometimes a working solution isn't enough - clean, understandable code is essential for debugging and future development. Taking time to rewrite the solution with clearer logic paid off in the long run."*

---

## 🎓 Course

This project was completed as part of the **MOOC.fi Python Programming course**.
