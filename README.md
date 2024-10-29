# Divide-and-Conquer Algorithms: Quick Sort and Merge Sort

## Overview
This repository contains an analysis and implementation of two fundamental divide-and-conquer algorithms: **Quick Sort** and **Merge Sort**. The objective of this project is to deepen the understanding of these algorithms through theoretical analysis, practical implementation, and performance comparison.

## Contents
- [1. Algorithms](#1-algorithms)
  - [Quick Sort](#quick-sort)
  - [Merge Sort](#merge-sort)
- [2. Performance Comparison](#2-performance-comparison)
- [3. Usage](#3-usage)
- [4. Conclusion](#4-conclusion)
- [5. References](#5-references)

## 1. Algorithms

### Quick Sort
Quick Sort is a recursive sorting algorithm that works by selecting a 'pivot' element and partitioning the array into two sub-arrays based on the pivot. The key steps are:
1. Choose a pivot element.
2. Partition the array into elements less than and greater than the pivot.
3. Recursively apply Quick Sort to the sub-arrays.
4. Combine the sorted sub-arrays with the pivot.

**Time Complexity Analysis:**
- Best Case: Ω(n log n)
- Average Case: Θ(n log n)
- Worst Case: O(n²)

### Merge Sort
Merge Sort is a recursive sorting algorithm that divides the array into halves, sorts each half, and then merges them back together. The key steps are:
1. Divide the array into two halves.
2. Recursively sort each half.
3. Merge the sorted halves.

**Time Complexity Analysis:**
- Best Case: Ω(n log n)
- Average Case: Θ(n log n)
- Worst Case: O(n log n)

## 2. Performance Comparison
The performance of both sorting algorithms is compared using different datasets, including sorted, reverse sorted, and random data. The following metrics are recorded:
- Execution time
- Memory usage

### Results
| Dataset Size | Algorithm   | Execution Time (s) | Memory Usage (MiB) |
|--------------|-------------|---------------------|---------------------|
| 100          | Quick Sort  | 0.432067            | 25.828125           |
| 100          | Merge Sort  | 0.391466            | 25.828125           |
| 1000         | Quick Sort  | 0.389513            | 25.859375           |
| 1000         | Merge Sort  | 0.387793            | 25.859375           |
| 5000         | Quick Sort  | 0.191514            | 26.109375           |
| 5000         | Merge Sort  | 0.193700            | 26.1875             |
| 10000        | Quick Sort  | 0.210713            | 26.734375           |
| 10000        | Merge Sort  | 0.224165            | 26.859375           |

These results indicate that Quick Sort tends to be slightly faster than Merge Sort on larger datasets, with marginally lower memory usage.

## 3. Usage
To run the algorithms and perform the performance comparison, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/maggie-2/MSCS532_Assignment2.git
2. Navigate to the project directory
   ```bash
   cd MSCS532_Assignment2
3. Install the necessary dependencies:
```bash
pip3 install memory_profiler
```
4. Run the Python script:
   ```bash
   python3 Divide_and_Conquer.py
## 4. Conclusion
This project highlights the efficiency and practical implications of Quick Sort and Merge Sort in various real-world applications. The analysis and performance comparison provide insights into the strengths and weaknesses of each algorithm.
## 5. References

