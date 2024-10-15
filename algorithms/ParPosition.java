public class ParPosition {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5,6,7,8,9};
        
        int[] aux = new int[((arr.length)/2)+1];
        
        aux = position(arr, 0, aux);
        String cadena = java.util.Arrays.toString(aux);

        System.err.println(cadena);
    }

    public static int[] position(int[] arr, int i, int[] aux){
        
        if (i >= arr.length) {
            return aux;
        }
        aux[i/2] = arr[i];

        return position(arr, i+2, aux);
    }
}