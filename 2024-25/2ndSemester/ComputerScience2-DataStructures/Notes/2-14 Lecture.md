
#### Recursion

```java
class SinglyLinkedList() {  
	private Node head;  
	public int size() {  
		int s = sizeHelper(this.head);  
		return s;  
	}  
	private int sizeHelper(Node c) {  
		int s;  
		if (c == null) s = 0  
		else s = 1 + sizeHelper(c.next);  
		return s //output 2 for [7,4]
```

For all lists a,  
1. a.size >= 0  
2. a.tail.next == null  
3. a.head == null && a.tail == null iff a.size == 0  
4. a.head == a.tail if size == 1  
5. a.head != a.tail iff size > 1


### Assert
Evaluates Boolean expression by looking at current value. If it is false, it throws an exception(runtime error)

**Syntax:
```java
assert condition; //AssertionError is thrown
assert condition : message; //`AssertionError` is thrown with the given message.
```

**Example:**
```java
public class AssertionExample {
    public static void main(String[] args) {
        int x = -1;
        assert x >= 0 : "x must be non-negative, but found " + x;
        System.out.println("x is: " + x);
    }
}
```

- Runtime can be expensive
- Use as a debug feature.
- Assert statements slow down program so they are ignored by default


### Invariant:
A Boolean expression whose value is always true at certain points in the code, such as before and after a method runs.


