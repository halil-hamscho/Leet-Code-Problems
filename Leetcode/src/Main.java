public class Main {
    // static means that the method belongs to the Main class and not an object of the main class
    // void means that this method does not have a re
    public static void main(String[] args) {
        // Multi Dimensional Arrays
        int [][] nums_2 = { {1,2,3,4}, {5,6,7,8} };
        // Using the for-each loop
//        for (int[] row : nums_2) {
//            for(int num_1 : row){
//                System.out.println(num_1);
//            }
//        }
        // using indexing
        for (int i = 0; i < nums_2.length; ++i) {
            System.out.println("Current Row: " + i);
            for (int j = 0; j < nums_2[i].length; ++j) {
                System.out.println(nums_2[i][j]);
            }
        }
    }
}