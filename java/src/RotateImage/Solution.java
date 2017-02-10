package RotateImage;

/**
 * Created by tom on 2/10/17.
 *
 You are given an n x n 2D matrix representing an image.

 Rotate the image by 90 degrees (clockwise).

 Follow up:
 Could you do this in-place?

 做矩阵旋转时，其实可以把矩阵分为四块。
 考虑左上四分之一块。然后对其每一个元素进行更换。

 有些时候长度为奇数时，j的取值范围从0到(l+1)/2，这样可以保证所有元素都能更换。

 */
public class Solution {
    public void rotate(int[][] matrix) {
        int l = matrix.length;

        for (int i = 0; i < l / 2; i++){
            for (int j = 0; j < (l + 1) / 2; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[l-1-j][i];
                matrix[l-1-j][i] = matrix[l-1-i][l-1-j];
                matrix[l-1-i][l-1-j] = matrix[j][l-1-i];
                matrix[j][l-1-i] = tmp;
            }
        }
    }

    public static void main(String[] args){
        int[][] matrix = new int[3][3];

        int[][] matix2 = {{1,1,1,1},{2,2,2,2},{3,3,3,3},{4,4,4,4}};

        for (int i = 0; i < matix2.length; i++){
            for (int j = 0; j < matix2[0].length; j++){
                System.out.print(matix2[i][j]);
            }
            System.out.println();
        }
        System.out.println();

        Solution newclass = new Solution();
        newclass.rotate(matix2);

        for (int i = 0; i < matix2.length; i++){
            for (int j = 0; j < matix2[0].length; j++){
                System.out.print(matix2[i][j]);
            }
            System.out.println();
        }

    }
}
