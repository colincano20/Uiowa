// DO NOT REMOVE PACKAGE LINE
// Without this line the autograder will not run correctly
// You can comment it while you work on the problem
// When everything works - uncomment and submit!
package com.gradescope.lab6;

/* Header
   Lab 6
   Authors:
*/

public class MatchBrackets {

  /* Tests if brackets in the given expression are properly matched.
     Matching brackets are characters '(' and ')',
     characters '[' and ']', and characters '{' and '}'.
     See examples below.
     */
  public static boolean bracketsMatch(String expression) {
    // HINT: a Stack of Characters will be helpful
    Stack<Character> s = new ArrayStack<>();

    // HINT: the String method charAt gets the character at a position in the String
    for (int i = 0; i < expression.length(); i++) {
        char c = expression.charAt(i);
        if (c == '(' || c == '[' || c == '{') {
          s.push(c);
        }
      if (c == ')' || c == ']' || c == '}') {
          if (s.isEmpty()) return false;
          switch (c) {
            case ')':
              if (s.top() == '(') {
                s.pop();
              }
              else return false;
              break;
            case ']':
              if (s.top() == '[') {
                s.pop();
              }
              else return false;
              break;
            case '}':
              if (s.top() == '{') {
                s.pop();
              }
              else return false;
              break;
          }
      }
    }

    return s.isEmpty();
  }

}
