package RemoveDuplicatesfromSortedArrayII;

/**
 * Created by tom on 10/10/16.
 * Follow up for "Remove Duplicates":
 What if duplicates are allowed at most twice?

 For example,
 Given sorted array nums = [1,1,1,2,2,3],

 Your function should return length = 5, with the first five
 elements of nums being 1, 1, 2, 2 and 3.
 It doesn't matter what you leave beyond the new length.

 解法较为简单，在Remove Duplicates from Sorted Array 1代的基础上加入
 boolean类型的flag来判断是否是第一次重复。具体逻辑是：
 遍历，每次判断中，如果相等且flag为false，记录到结果，flag变为true
 如果不想等，记录到结果，flag变为false。
 */
public class Solution {
    public int removeDuplicates(int[] nums){
        int n = nums.length;
        int j = 0;
        boolean flag = false;
        for(int i = 1; i < n; i++){
            if(nums[i] == nums[j] && flag == false){
                j++;
                nums[j] = nums[i];
                flag =true;
            }else if(nums[i] != nums[j]){
                j++;
                nums[j] = nums[i];
                flag = false;
            }
        }
        return j+1;

    }
    public static void main(String[] args){
        Solution newclass = new Solution();

        int[] testnums = {1,1,2};
        System.out.println(newclass.removeDuplicates(testnums));
        int n = testnums.length;
        for (int i = 0; i < n; i++){
            System.out.print(testnums[i]+",");
        }

        int[] testnums1 = {1,1,1};
        System.out.println(newclass.removeDuplicates(testnums1));
        int n1 = testnums1.length;
        for (int i = 0; i < n1; i++){
            System.out.print(testnums1[i]+",");
        }

        int[] testnums2 = {1,1,1,1};
        System.out.println(newclass.removeDuplicates(testnums2));
        int n2 = testnums2.length;
        for (int i = 0; i < n2; i++){
            System.out.print(testnums2[i]+",");
        }
    }
}
