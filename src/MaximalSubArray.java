// Given an array of integers (positive/zero/negative), write a function that calculates
// the maximum sum of any continuous sub-array of the input array
// Ex. [1, 2, 3, 4] = 1 + 2 + 3 + 4 = 10
// [2, 3, -1, -3] = 2 + 3 = 5
// [-1, 5, 100, -1000] = 5 + 100 = 105
// [-1, -2, -3, -4] = 0
// [1000, 2000, -1, 10000] = 1000 + 2000 + -1 + 10000

public class MaximalSubArray {

    public static int maximalSubArray(int[] a) {
        int curSumSoFar = 0;
        int maxSumSoFar = 0;

        for (int i = 0; i < a.length; i++) {
            curSumSoFar = Math.max(0, curSumSoFar + a[i]);
            maxSumSoFar = Math.max(maxSumSoFar, curSumSoFar);
        }

        return maxSumSoFar;
    }

    public static void main(String[] args) {
        int[] a = {1,2,3,4};
        int[] b = {2,3,-1,-3};
        int[] c = {-1,5,100,-1000};
        int[] d = {-1,-2,-3,-4};
        int[] e = {1000,2000,-1,10000};
        int[] f = {2,1,-3,-2,-4,-1,0,3};

        System.out.println(MaximalSubArray.maximalSubArray(a));
        System.out.println(MaximalSubArray.maximalSubArray(b));
        System.out.println(MaximalSubArray.maximalSubArray(c));
        System.out.println(MaximalSubArray.maximalSubArray(d));
        System.out.println(MaximalSubArray.maximalSubArray(e));
        System.out.println(MaximalSubArray.maximalSubArray(f));
    }
}
