public class SearchMenor {
    public static void main(String[] args) {
        int[][] arr = {{1,2,3,4},{4,5,6,7},{8,9,10,11},{12,13,14,16,20}};
        int aux = arr[0][0];
        
    }
    public static int searchMatriz(int i, int j, int aux, int[][] arr){
        if (i >= arr.length-1) {
            return aux;
        }
        if (j >= arr.length-1) {
            return searchMatriz(i+1, 0, aux, arr);
        }
        
        return 0;
    }
}
