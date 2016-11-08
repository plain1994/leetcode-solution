package PascalTriangle;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by tom on 10/11/16.
 * Given numRows, generate the first numRows of Pascal's triangle.

 For example, given numRows = 5,
 Return

 [
 [1],
 [1,1],
 [1,2,1],
 [1,3,3,1],
 [1,4,6,4,1]
 ]

 解法根据生成规律：
 A[i][j] = A[i-1][j-1] + A[i-1][j]
 第k层有k个元素
 每层第一个以及最后一个元素值为1
 */
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> rst = new ArrayList<List<Integer>>();
        if (numRows == 0){
            return rst;
        }
        List<Integer> first = new ArrayList<Integer>();
        first.add(0, 1);
        rst.add(first);

        for(int i = 1; i < numRows; i++){
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(1);
            for(int j = 1; j < i; j++){
                int tmp2 = rst.get(i-1).get(j-1) + rst.get(i-1).get(j);
                tmp.add(tmp2);
            }
            if(i >= 1){
                tmp.add(1);
            }
            rst.add(tmp);
        }
        return rst;
    }
    public static void main(String[] args){
        Solution newclass = new Solution();
        System.out.println(newclass.generate(3));
    }
}
