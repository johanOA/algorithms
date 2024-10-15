public class ejemplo {
    public static void main(String[] args) {
        String p = "[.?";
        boolean r = metodo(p, 0, 1);
        System.err.println(r);
    }
    public static boolean metodo(String palabra, int i, int j){
        char[] aux = palabra.toCharArray();
        if (j>=aux.length) {
            return metodo(palabra, i+1, 0);
        }
        if (i>=aux.length) {
            return false;
        }
        if (aux[i] == aux[j]) {
            return true;
        }
        return metodo(palabra, i, j+1);
    }
}
