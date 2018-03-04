/**
 * Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
 * Formally the function should:
 * Return true if there exists i, j, k
 * such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
 * Your algorithm should run in O(n) time complexity and O(1) space complexity.
 * Examples:
 * Given [1, 2, 3, 4, 5],
 * return true.
 * Given [5, 4, 3, 2, 1],
 * return false.
 */
public class IncreasingTripletSubsequent {

    /**
     * Keep track a the latest smallest number and second smallest number.
     * time complexity O(n)
     * space complexity O(1)
     *
     * @param nums
     * @return
     */
    public static boolean increasingTriplet(int[] nums) {

        if (nums.length < 3) return false;

        int first = Integer.MAX_VALUE - 1, second = Integer.MAX_VALUE;
        int low = -1, mid = -1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] <= first) {
                low = i;
                first = nums[i];
            } else if (nums[i] <= second) {
                mid = i;
                second = nums[i];
            } else {
                System.out.println(low + "-" + mid + "-" + i);
                System.out.println(nums[low] + "-" + nums[mid] + "-" + nums[i]);
                return true;
            }
        }

        return false;
    }
//        int low = 0, high = nums.length-1;
//        int mid = low+1;
//        while (low < high && mid < high) {
//            if (nums[low] < nums[mid] && nums[mid] < nums[high]) {
//                System.out.println(low + "-" + mid + "-" + high);
//                System.out.println(nums[low] + "-" + nums[mid] + "-" + nums[high]);
//                return true;
//            }
//
//            while (mid < high && nums[mid] < nums[low]) {
//                low = mid;
//                mid++;
//            }
//
//            while (high > mid && nums[high] < nums[high-1]) {
//                high--;
//            }
//
//            mid++;
//        }
//
//        return false;
//    }

    public static void main(String[] args) {
        int[] nums = {123, 100, 45, 23, 65, 4, 3, 3, 6, 7, 6, 8, 5, 8};
        System.out.print(IncreasingTripletSubsequent.increasingTriplet(nums));
    }
}
