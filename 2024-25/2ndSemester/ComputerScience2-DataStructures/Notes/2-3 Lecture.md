
---
### **Objects

```java
className objectName = new className(parameter, ... , prameter); // constructor
Point p = new Print(7.5,4.2);
Point o = new Print();

//calling object method
objectName.methodname(parameter)
p.translate(2.1,-2.5);
doubld d = p.distance(o);
```

![[Pasted image 20250203095302.png]]most important or sum


Field aka Instance variable: A variable inside a class C  
- Each instance o of C has its own value for each field, which is part of o's state
Declaration syntax:
```java
typeName fieldName;
```
	
```java
public class PointMain {  
	main(String args) {   
		Point p1 = new Point();  
		p1.x = 7;  
		p1.y = 2.6;  
		Point p2 = new Point();  
		p2.x = 4;  
		p2.y = 3;
- ```

![[Pasted image 20250203095703.png]]


instance/object method: method associated to class instances, defining their behavior

Declaration syntax:
```java
public typeName methodName(parameters){
	statements;
}
```
### Accessor Methods
**Purpose**: Allow clients to examine an object's state.

- **Examples**: `distance`, `distanceFromOrigin`
- **Return Type**: Always has a non-void return type

### Mutator Methods
**Purpose**: Allow clients to modify an object's state.

- **Examples**: `setLocation`, `translate`
- **Return Type**: Usually has a void return type

### The *this* Keyword
*this*: Used to refer to the implicit parameter *inside* the class(A variable that refers to the object on which a method is called)
Syntax:
 ```java
 this.fieldName     //To refer to a field:
 this.methodName(parameters) //to call a method:
 this(parameters) //to call a constructor from another:
```

### Public vs Private
- any class, field, or method with the public access modifier is visible from anywhere, even from classes that belong to a different package  
 -  a field or method with the protected access modifier can only be accessed within its package  
- a field or method with the private access modifier can only be accessed within its class

|                         | Private | [none] | Protected | Public |
| ----------------------- | ------- | ------ | --------- | ------ |
| Same class or subclass  | Yes     | Yes    | Yes       | Yes    |
| Package                 | No      | No     | Yes       | Yes    |
| Out-of-package subclass | No      | Yes    | Yes       | Yes    |
| World                   | No      | No     | No        | Yes    |

### Constructors:

Def: Creates a new instance and initializes its state  
Syntax:  
```java
public typeName(parameters) {  
	statements;  
```
}  
• runs when the client uses the new keyword  
• no return type is specified; it implicitly returns the new object being created  
• if a class has no constructors, Java gives it a default constructor with no  
parameters that initializes all fields to their default value

