public class SearchLongChar {
    public static void main(String[] args) {
        String[][] arr = {{"Maria", "Jose", "Gato", "Perro"},
                          {"Pato", "Ragdoll", "Game", "Of"},
                          {"Trones", "Jul", "John", "Mac"},
                          {"Lenovo", "Acer", "Apple", "Esternocleidomastoideo"}};
        String moreLong = "";
        moreLong = searchLong(0, 0, arr, moreLong);
        System.err.println(moreLong);
        
    }
    public static String searchLong(int i, int j, String[][] arr, String moreLong){
        if (i >= arr.length) {
            return moreLong;   
        }
        if (j >= arr.length) {
            return searchLong(i+1, 0, arr, moreLong);
        }
        if (moreLong.length() < arr[i][j].length()) {
            moreLong = arr[i][j];
        }

        return searchLong(i, j+1, arr, moreLong);
    }
}
