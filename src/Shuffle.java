import java.util.Random;

public class Shuffle {

    /**
     * Randomly shuffle all the elements in an array
     * @param a
     */
    public static void shuffle(int[] a) {
        Random random = new Random();
        for (int i = 0; i < a.length; i++) {
            int r = i + random.nextInt(a.length - i);
            int temp = a[i];
            a[i] = a[r];
            a[r] = temp;
        }
    }

    public static void main(String[] args) {
        int[] a = {1,2,3,4,5,6,7,8,9,10};
        Shuffle.shuffle(a);
        for (int e : a) {
            System.out.print(e + " ");
        }
    }
}
