package RotateMatrix;

/**
 * Created by tom on 2/10/17.
 *
 把一个m*n的矩阵旋转90度，给一个flag规定是向左转还是向右转
 */
public class Solution {
    public int[][] rotate(int[][] matrix, int flag){
        int m = matrix.length;
        int n = matrix[0].length;

        int[][] rvalue = new int[n][m];

        //transpose
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                rvalue[i][j] = matrix[j][i];
            }
        }

        if (flag == 1){ //clock wise
            for (int i = 0; i < n; i++){
                for (int j = 0; j < m / 2; j++){
                    int tmp = rvalue[i][j];
                    rvalue[i][j] = rvalue[i][m-j-1];
                    rvalue[i][m-j-1] = tmp;
                    /*
                    rvalue[i][j] ^= rvalue[i][m-j-1];
                    rvalue[i][m-j-1] ^= rvalue[i][j];
                    rvalue[i][j] ^= rvalue[i][m-j-1];
                    */
                }
            }
        }else{
            for (int i = 0; i < n / 2; i++){
                for (int j = 0; j < m; j++){
                    rvalue[i][j] ^= rvalue[n-i-1][j];
                    rvalue[n-i-1][j] ^= rvalue[i][j];
                    rvalue[i][j] ^= rvalue[n-i-1][j];
                }
            }
        }

        return rvalue;
    }
    public static void main(String[] args){
        int[][] matix2 = {{1,2,3},{4,5,6},{7,8,9},{10,11,12}};


        for (int i = 0; i < matix2.length; i++){
            for (int j = 0; j < matix2[0].length; j++){
                System.out.print(matix2[i][j]);
            }
            System.out.println();
        }
        System.out.println();

        Solution newclass = new Solution();

        int[][] rematrix = newclass.rotate(matix2, 1);

        for (int i = 0; i < rematrix.length; i++){
            for (int j = 0; j < rematrix[0].length; j++){
                System.out.print(rematrix[i][j]);
            }
            System.out.println();
        }
    }
}
