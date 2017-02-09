package ValidParentheses;

/**
 * Created by tom on 2/8/17.
 *
 *
 Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

 The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

 */
import java.util.Stack;

public class Solution {
    public boolean isValid(String s) {
        if (s == null || s.length() == 0){return true;}
        Stack<Character> stack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++){
            if (stack.empty()) {stack.push(s.charAt(i));}
            else if ((stack.peek() == '(' && s.charAt(i) == ')') ||(stack.peek() == '[' && s.charAt(i) == ']') || (stack.peek() == '{' && s.charAt(i) == '}')){
                stack.pop();
            }else{
                stack.push(s.charAt(i));
            }
        }
        return stack.empty();
    }

    public static void main(String[] args){
        Solution newclass = new Solution();
        System.out.println(newclass.isValid("()"));
        System.out.println(newclass.isValid("(sdadas"));
    }
}
