# Go Data Structures

Efficiently managing collections of data in Go.

## Arrays
Fixed size, rarely used directly in Go.
```go
var a [5]int
a[2] = 100
```

## Slices (Dynamic Arrays)
The most common way to handle ordered data.
```go
// Creating a slice
nums := []int{1, 2, 3}

// Slicing an existing slice/array
sub := nums[1:3] // [2, 3]

// Appending (Crucial)
nums = append(nums, 4, 5)

// Copying
duplicate := make([]int, len(nums))
copy(duplicate, nums)
```

## Maps (Hash Tables)
Unordered key-value pairs.
```go
m := make(map[string]int)
m["Age"] = 25

// Check existence
val, ok := m["Age"]
if ok {
    fmt.Println(val)
}

// Deleting
delete(m, "Age")
```

## Range Iterator
```go
for key, value := range m {
    fmt.Printf("%s: %d\n", key, value)
}
```
