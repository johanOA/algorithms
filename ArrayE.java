public class ArrayE {
    public static void main(String[] args) {
        String[] nombre = {"Ana", "Martin", "Pedro", "jose", "Aep"};
        boolean[] aux = new boolean[nombre.length];

        aux = isArrEBool(nombre, aux, 0, 0);

        String cadena = java.util.Arrays.toString(aux);
        System.err.println(cadena);
    }
    public static boolean[] isArrEBool(String[] arr, boolean[] aux, int i, int j ){
        
        if (i >= arr.length) {
            return aux;
        }

        if (arr[i].length()%2 == 0) {
            j = arr[i].length()/2;
        } else {
            j = (arr[i].length()/2)+1;
        }

        if (arr[i].charAt(j-1) == 'e') {
            aux[i] = true;
        } else {
            aux[i] = false;
        }

        return isArrEBool(arr, aux, i+1, 0);
    }
}
