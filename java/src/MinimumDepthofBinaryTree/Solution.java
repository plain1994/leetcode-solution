package MinimumDepthofBinaryTree;

/**
 * Created by tom on 2/8/17.
 *
 Given a binary tree, find its minimum depth.

 The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
 */

/**
 * Definition for a binary tree node.
 */
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
  }

public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) return 0;
        if (root.left != null && root.right == null){
            return minDepth(root.left) + 1;
        }
        if (root.left == null && root.right != null){
            return minDepth(root.right) + 1;
        }
        return Math.min(minDepth(root.left) + 1, minDepth(root.right) + 1);
    }
    public static void main(String[] args){
        Solution newclass = new Solution();
        TreeNode treenode1 = new TreeNode(0);
        TreeNode treenode2 = new TreeNode(2);
        TreeNode treenode3 = new TreeNode(3);
        TreeNode treenode4 = new TreeNode(4);
        TreeNode treenode5 = new TreeNode(5);

        treenode1.left = treenode2;
        treenode1.right = treenode3;
        treenode2.left = treenode4;
        treenode2.right = treenode5;


        System.out.println(newclass.minDepth(treenode1));
    }
}
