public class arrayUpAverage {
    public static void main(String[] args) {
        double[] numbers = {2.0, 1.5, 2.3, 4.4, 5.6};
        double[] aux = new double[2];

        double avg = avg(numbers, 0);

        System.out.println(avg);

        //aux = upAvgDown(numbers, aux, 0, 0, 0);

        //String cadena = java.util.Arrays.toString(aux);
        //System.err.println(cadena);

    }
    public static double[] upAvgDown(double[] arr, double[] aux, int i, double countDown, double countUp){

        if (i >= arr.length) {
            aux[0] = countDown;
            aux[1] = countUp;
            return aux;
        }
        
        return arr;
    }

    public static double avg(double[] arr, int i){
        
        if (i >= arr.length-1) {
            return arr[i];
        }
        
        return avg(arr, i+1)/arr.length;
    }
}
