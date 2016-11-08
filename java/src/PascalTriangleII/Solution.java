package PascalTriangleII;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by tom on 11/8/16.
 * Given numRows, generate the first numRows of Pascal's triangle.

 Given an index k, return the kth row of the Pascal's triangle.

 For example, given k = 3,
 Return [1,3,3,1].

 Note:
 Could you optimize your algorithm to use only O(k) extra space?


 解法根据生成规律：
 A[i][j] = A[i-1][j-1] + A[i-1][j]
 第k层有k个元素
 每层第一个以及最后一个元素值为1
 */

public class Solution {
    public List<Integer> getRow(int rowIndex) {
        rowIndex++;
        List<Integer> rst = new ArrayList<Integer>();
        if (rowIndex == 0){
            return rst;
        }

        rst.add(1);

        for(int i = 1; i < rowIndex; ++i){
            List<Integer> tmp = new ArrayList<Integer>();
            tmp.add(1);
            for (int j = 1; j < i; j++){
                int numsum = rst.get(j-1)+ rst.get(j);
                tmp.add(numsum);
            }
            if (i >= 1){
                tmp.add(1);
            }
            rst = tmp;
        }
        return rst;
    }
    public static void main(String[] args){
        Solution newclass = new Solution();
        System.out.println(newclass.getRow(5));
    }
}

