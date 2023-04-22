/*
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
*/

class Solution {

    public void rotate(int[][] matrix) {
        //length of matrix
        int n = matrix.length;

        /*
        Step 1: Transpose the matrix by swapping the elements
        along its diagonal, iterate through upper triangular matrix
        and swap each element with its corresponding element
        in the lower triangular matrix
        */

        // iterate through the upper triangular matrix
        // (i.e., the elements above the diagonal)
        for(int i = 0; i < n; i++){
            for(int j = i + 1; j < n; j ++){
                //first save the current (i,j) element of the matrix
                int temp = matrix[i][j];
                //swap each element with its corresponding elements
                //in the lower matrix (elements below the diagonal)
                matrix[i][j] = matrix[j][i];
                //now update the new (j,i) spot with the saved element
                matrix[j][i] = temp;
            }
        }

        /*
        Step 2: Reverse each row of the resulting matrix to get
        the desired rotated image.
        */

        //iterate through each row of the transposed matrix 
        for(int i = 0; i < n; i++){
            //the upper limit is n/2 because we only need to swap the
            //elements up to the middle element of each row
            //because the other half has already been swapped in step 1
            for(int j = 0; j < n / 2; j++){
                // save current (i,j) element of the matrix
                int temp = matrix[i][j];
                //swap the elements of the row in reverse order (n=length)
                matrix[i][j] = matrix[i][n - j - 1];
                //this reverses each row of the matrix
                //to get our desired rotation
                //update the new (i, n-j-1) spot with the saved element
                matrix[i][n - j - 1] = temp;
            }
        }

    }
}
