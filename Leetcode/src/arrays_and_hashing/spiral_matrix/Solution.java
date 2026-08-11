package arrays_and_hashing.spiral_matrix;


/*
difference between int[], ArrayList<Integer> and List<Integer>

int[] (primitive array)
is a fixed size array that stores primitive int values
most basic collection type for storing integers
once it is created, its size cannot change
you need to create a new array and copy the elements
- USE only when you know the size of the collection in advance, memory and performance efficiency

ArrayList<Integer> (Dynamic Array)
Dynamic array from the java collections framework
resizable array that stores Integer objects (the object wrapper for the primitive int)
numbers.add();

List<Integer> (Interface)
is an interface from the Java collections framework.
defines the behavior of a list but does not provide concrete implementation
.add()
.remove()
.get()
ArrayList<Integer> and LinkedList<Integer> and other classes implement the List interface
 */

/*

move right row, col + 1
move left row, col - 1
move up row - 1, col
move down row + 1, col
 */

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        // Result List
        List<Integer> result = new ArrayList<>();

        // Total Number of Rows and Cols
        int rows = matrix.length;
        int cols = matrix[0].length;

        // Set up Pointer Variables
        int row = 0;
        int col = -1;

        // Initial Direction from left to right
        int direction = 1;

        // Will be utilizing a single pointer direction
        while (rows > 0 && cols > 0) {
            System.out.printf("Current Row (%d) and Col (%d)%n", row, col);
            // Move Horizontally
            // Left (direction + 1)
            // Right (direction - 1)

            // Increment col pointer to move horizontal
            for(int i = 0; i < cols; i++) {
                col += direction;
                System.out.printf("Col (%d)%n", col);
                result.add(matrix[row][col]);
                System.out.println("Result" + result);
            }
            rows--;

            // We are at the end of the col, now move down
            // Top to bottom (direction + 1)
            // Bottom to top (direction - 1)
            for(int i = 0; i < rows; i++) {
                row += direction;
                System.out.printf("Row (%d)%n", row);
                result.add(matrix[row][col]);
                System.out.println("Result" + result);
            }
            cols--;

            // Flip the direction
            direction *= -1;
        }
        return result;
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[][] matrix = {  {1,2,3},
                            {4,5,6},
                            {7,8,9}};
        System.out.println(sol.spiralOrder(matrix));
    }
}
