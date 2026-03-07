# Go Pointers & Memory

Understanding how Go manages memory and references.

## Pointers
A pointer holds the memory address of a value.

```go
x := 10
p := &x         // p is a pointer to x
fmt.Println(*p) // Dereference: Prints 10

*p = 20         // Change value through pointer
fmt.Println(x)  // Prints 20
```

## No Pointer Arithmetic
Unlike C, Go does not allow pointer arithmetic (e.g., `p++`). This makes the language safer.

## When to use Pointers?
- **Modification**: When you need a function to modify its arguments.
- **Performance**: To avoid copying large structs (though Go is usually fast enough with copies).
- **Consistency**: Large structs or objects representing unique resources (like files or database connections).

## Heap vs Stack (Escaping)
The Go compiler automatically decides if a variable should live on the **stack** (fast, auto-cleaned) or the **heap** (slower, GC-cleaned).
- If a variable's address is shared outside of its scope, it "escapes to the heap".

## Zero Values
Pointers default to `nil`. Always check for `nil` before dereferencing to avoid panics.
