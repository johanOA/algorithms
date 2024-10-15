//Un número N es perfecto si la suma de sus divisores (excluido el propio N) 
//es N. Por ejemplo 28 es perfecto, pues sus divisores  (excluido el 28) son 
//1,2,4,7 y 14 su suma da 28. Escriba un método que indique si N es perfecto.
public class PerfectNumber {
    public static void main(String[] args) {
        int n = 12;
        System.err.println(perfectNumber(n, n-1, 0));

    }

    public static boolean perfectNumber(int n, int m, int aux) {
        
        if (m == 0) {
            return aux == n;
        }
        if (n%m==0) {
            aux = m + aux;
        }
        return perfectNumber(n, m-1, aux);
    }
}
