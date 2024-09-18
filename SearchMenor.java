public class SearchMenor {
    public static void main(String[] args) {
        int[][] arr = {{10,20,30,40},{40,50,60,70},{80,110,10,11},{12,13,14,16,20}};
        int aux = arr[0][0];
        int result = searchMatriz(0, 0, aux, arr);

        System.err.println(result);

    }
    public static int searchMatriz(int i, int j, int aux, int[][] arr){
        if (i >= arr.length-1) {
            return aux;
        }
        if (j >= arr.length-1) {
            return searchMatriz(i+1, 0, aux, arr);
        }
        if (arr[i][j]<= aux) {
            aux = arr[i][j];
        }
        
        return searchMatriz(i, j+1, aux, arr);
    }
}
