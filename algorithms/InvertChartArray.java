public class InvertChartArray {
    public static void main(String[] args) {
        String[] arr = {"Maria", "Ramon", "Martha"};
        String[] aux = new String[arr.length];
        aux = invertChars(0, arr, aux);
        String string = java.util.Arrays.toString(aux);
        System.err.println(string);
    }
    public static String[] invertChars(int i, String[] arr, String[] aux){
        if (i >= arr.length) {
            return aux;
        }
        char[] aux2 = arr[i].toCharArray();
        char[] aux3 = new char[aux2.length];
        aux[i] = invert(0, aux2, aux3);

        return invertChars(i+1, arr, aux);
    }
    public static String invert(int i, char[] arrWord, char[] aux) {
        if (i >= arrWord.length) {
            String invert = new String(aux);
            return invert;
        }
        aux[i] = arrWord[arrWord.length-1-i];
        return invert(i+1, arrWord, aux);
    }
}
