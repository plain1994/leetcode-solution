package PlusOne;

/**
 * Created by tom on 10/10/16.
 * Given a non-negative number represented as an array of digits, plus one to the number.

 The digits are stored such that the most significant digit is at the head of the list.
 ？Java的数组不能insert吗？
 */
public class Solution {
    public int[] plusOne(int[] digits){
        int i = digits.length - 1;
        int carry = 1;
        int number = 0;

        while(i >= 0 && carry == 1){
            number = digits[i] + 1;
            digits[i] = number % 10;
            carry = number / 10;
            i -= 1;
        }
        if(carry == 0){
            return digits;
        }
        int[] res = new int[digits.length+1];
        res[0] = 1;
        for(int j = 1; j < res.length; j++){
            res[j] = digits[j-1];
        }
        return res;
    }

    public static void main(String[] args){
        Solution newclass = new Solution();
        int[] testnums = {1,1,2};
        System.out.println(newclass.plusOne(testnums));
        int n = testnums.length;
        for (int i = 0; i < n; i++){
            System.out.print(testnums[i]+",");
        }
    }
}
