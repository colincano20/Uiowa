### **What is a Linked List?**

A linked list consists of nodes, where each node contains:

- **Data** – The actual value stored.
- **A pointer (reference) to the next node** – This links nodes together.

Here’s a simple visual representation:
```css
[10] → [20] → [30] → null
```

Each **box** (node) contains a value and a pointer to the next node.
Unlike arrays, linked lists don’t require a fixed size, making them useful for dynamic memory allocation.

![[Pasted image 20250213105701.png]]

![[Pasted image 20250213105817.png]]
For all lists a, 
1. a.size >= 0 
2. a.tail.next == null 
3. a.head == null && a.tail == null iff a.size == 0 
4. a.head == a.tail if size == 1 
5. a.head != a.tail iff size > 1