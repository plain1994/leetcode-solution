package WindowSum;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by tom on 2/11/17.
 */
public class Solution {
    public List<Integer> GetSum(List<Integer> A, int k) {
        ArrayList<Integer> result  = new ArrayList<>();
        if (A == null || A.size() == 0 || k <= 0) return result;
        int count = 0;
        for (int i = 0; i < A.size(); i++) {
            count++;
            if (count >= k) {
                int sum = 0;
                for (int j = i; j >= i - k + 1; j--) {
                    sum += A.get(j);
                }
                result.add(sum);
            }
        }
        return result;
    }

    public int[] SumOfWindow(int[] array, int k) {
        if (array == null || array.length < k || k <= 0)    return null;
        int[] rvalue = new int[array.length - k + 1];
        for (int i = 0; i < k; i++)
            rvalue[0] += array[i];
        for (int i = 1; i < rvalue.length; i++) {
            rvalue[i] = rvalue[i-1] - array[i-1] + array[i+k-1];
        }
        return rvalue;
    }


    public static void main(String[] args){
        List<Integer> numlist = new ArrayList<Integer>();
        numlist.add(1);
        numlist.add(2);
        numlist.add(3);
        numlist.add(4);
        numlist.add(5);
        numlist.add(6);
        numlist.add(7);
        numlist.add(8);
        numlist.add(9);

        Solution newclass = new Solution();
        List<Integer> relist = newclass.GetSum(numlist, 3);

        for (int i = 0; i < relist.size(); i++){
            System.out.println(relist.get(i));
        }



        int[] numlist2 = {1,2,3,4,5,6,7,8,9};
        Solution newclass2 = new Solution();
        int[] relist2 = newclass2.SumOfWindow(numlist2, 3);

        for (int i = 0; i < relist.size(); i++){
            System.out.println(relist.get(i));
        }
    }
}
