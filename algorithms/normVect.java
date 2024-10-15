public class normVect {
    public static void main(String[] args) {
        
        int[] a = {1,2,3};
        double n = nrmVect(a, 0);
        System.out.println(n);
    }
    public static double nrmVect(int[] a,int i) {
        if (i >= a.length - 1) {
            return a[i] * a[i];
        }
        return (0.5*(a[i] * a[i] + nrmVect(a, i+1)));
    }
}
