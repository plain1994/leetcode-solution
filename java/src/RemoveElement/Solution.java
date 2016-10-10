package RemoveElement;

/**
 * Created by tom on 10/09/16.
 *
 * Given an array and a value, remove all instances of that value in place and return the new length.
 The order of elements can be changed. It doesn't matter what you leave beyond the new length.

 解法较为简单，遍历数组进行比较，不相同的存到原数组前面。
 */
public class Solution{
    public int removeElement(int[] nums, int val){
        int i = 0;
        int n = nums.length;
        for(int j = 0; j < n; j++){
            if(nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }

    public static void main(String[] args){
        Solution newclass = new Solution();
        int[] testnums = {3,2,2,3};
        System.out.println(newclass.removeElement(testnums,3));
    }
}
