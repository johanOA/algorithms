public class SumBorderArray {
    public static void main(String[] args) {
        int[][] arr = {{01,02,03,04,05,06},
                       {10,11,12,13,14,15},
                       {20,21,21,23,24,25},
                       {30,31,32,34,35,36}};
        int aux = sumBorder(0, 0, arr, 0);
        System.err.println(aux);
        
    }
    public static int sumBorder(int i, int j, int[][] arr, int sum){

        
        if (i == 0 || i == arr.length-1) {
            
            if (i == arr.length-1 && j >= arr[0].length) {
                return sumBorder(1, 0, arr, sum);
            }

            if (j >= arr[0].length) {
                return sumBorder(arr.length-1, 0, arr, sum);   
            }

            sum = sum + arr[i][j];
            return sumBorder(i, j+1, arr, sum);   
        }

        if (i >= arr.length-2 && j == arr[0].length-1) {
            return sum;
        }

        if (i >= arr.length-2) {
            return sumBorder(1, arr[0].length-1, arr, sum);
        }
        
        sum = sum + arr[i][j];
        return sumBorder(i+1, j, arr, sum);
    }
}
