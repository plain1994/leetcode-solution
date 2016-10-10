package RemoveDuplicatesfromSortedArray;

/**
 * Created by tom on 10/10/16.
 * Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

 Do not allocate extra space for another array, you must do this in place with constant memory.

 For example,
 Given input array nums = [1,1,2],

 Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
 解法很简单，用i遍历数组，用j存储不相同的元素，每次比较ij是否相同，
 不相同的话存入j，并给j坐标加一。
 */
public class Solution {
    public int removeDuplicates(int[] nums){
        int n = nums.length;
        int j = 0;
        for(int i = 1; i < n; i++){
            if(nums[i] != nums[j]){
                j++;
                nums[j] = nums[i];
            }
        }
        return j+1;

    }
    public static void main(String[] args){
        Solution newclass = new Solution();
        int[] testnums = {1,1,2};
        System.out.println(newclass.removeDuplicates(testnums));
    }
}
