# C# Arrays

Arrays are used to store multiple variables of the same type in a single data structure.

## Single-Dimensional Arrays
```csharp
// Declaration and initialization
int[] numbers = new int[5];
numbers[0] = 10;

// Shorthand syntax
string[] fruits = { "Apple", "Banana", "Orange" };
```

## Multi-Dimensional Arrays
```csharp
// 2D Array (Rectangular)
int[,] matrix = new int[3, 3];
matrix[0, 0] = 1;

// Jagged Array (Array of arrays)
int[][] jagged = new int[3][];
jagged[0] = new int[4];
```

## Core Methods
- `Array.Sort(numbers)`: Sorts the array.
- `Array.Reverse(numbers)`: Reverses the array elements.
- `numbers.Length`: Total number of elements.

---
*For dynamic sizing, use **[Lists](csharp-basics.md#common-collections)**.*
