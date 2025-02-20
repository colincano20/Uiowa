
---
### The toString method
Tells Java how to convert an object into a String  
```java
Point p1 = new Point(7, 2);  
System.out.println("p1: " + p1); // abbreviates:  
System.out.println("p1: " + p1.toString());  
```

Possible user-provided definition for Point  
```java
// Returns a String representing this Point  
public String toString() {  
	return "(" + x + ", " + y + ")";  
}  
```
Every class has a default toString method that converts instances to  
```
className@objectsAddress (Ex: Point@9e8c34)
```

### Getting Input from the Console

**Scanner: an instance of class Scanner that can read input from many sources  
 - Communicates with System.in (the dual of *System.out*)  
- Can also read from files (Ch. 6), web sites, databases, strings, ...  

```
import java.util.Scanner; // so you can use scanners  
```

**Constructing a Scanner object to read console input:  

```java
Scanner name = new Scanner(System.in); 
```

| Method       | Description                                       |
| ------------ | ------------------------------------------------- |
| nextInt()    | reads an int from (the user) input and returns it |
| nextDouble() | reads a double from input                         |
| next()       | reads a one-word String from input                |
| nextLine()   | reads a one-line String from input                |
### Input Tokens
Def: A unit of user input, as read by a Scanner object  
-  tokens are separated by whitespace (spaces, tabs, new lines)  
- how many tokens appear on the following line of input?  
```
	23 John Smith 42.0 "Hello world" $2.50 " 19"  
```

It is an error to input a token with a different type than the requested one  
```java
Scanner console = new Scanner(System.in);  
System.out.print("What is your age? ");  
int age = console.nextInt();  
```
Output:  
```
What is your age? Apple  
java.util.InputMismatchException  
	at java.util.Scanner.next(Unknown Source)  
	at java.util.Scanner.nextInt(Unknown Source)
```

### Using hasNext methods  

• **Avoiding type mismatches:  

```java
Scanner console = new Scanner(System.in);  
System.out.print("What is your favorite number");  
if (console.hasNextInt()) {  
int n = console.nextInt(); // will not crash!  
System.out.println("The number is" + n);  
} else {  
System.out.println("You didn't type an integer.");  
}  
```

• **Avoiding reading past the end of a file:  

```java
Scanner input = new Scanner(new File("example.txt"));  
if (input.hasNext()) {  
String token = input.next(); // will not crash!  
System.out.println("next token is " + token);  
}
```



