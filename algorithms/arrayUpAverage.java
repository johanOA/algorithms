public class arrayUpAverage {
    public static void main(String[] args) {
        double[] numbers = {2.0, 1.5, 2.3, 4.4, 5.6};
        double[] aux = new double[2];

        double avgD = avg(numbers, 0);


        aux = upAvgDown(numbers, aux, avgD, 0, 0, 0);

        String cadena = java.util.Arrays.toString(aux);
        System.err.println(cadena);

    }
    public static double[] upAvgDown(double[] arr, double[] aux, double avg, int i, double countDown, double countUp){

        if (i >= arr.length) {
            aux[0] = countDown;
            aux[1] = countUp;
            return aux;
        }

        if (arr[i]<avg) {
            countDown = countDown + 1;
        } else {
            countUp = countUp + 1;
        }
        
        return upAvgDown(arr, aux, avg, i+1, countDown, countUp);
    }

    public static double avg(double[] arr, int i){
        
        if (i >= arr.length-1) {
            return arr[i]/arr.length;
        }
        
        return arr[i]/arr.length +  avg(arr, i+1);
    }
}
