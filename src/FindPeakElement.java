public class FindPeakElement {

    /**
     * Using a variant of binary search tree to search for a peak.
     * time complexity O(log(n))
     * space complexity O(1)
     *
     * @param nums input array with distinct integers
     * @return the index of a peak
     */
    public static int findPeakElement(int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        int mid;
        // the peak is basically the point when increasing sub-array meet the decreasing sub-array
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] > nums[mid + 1])
                right = mid; // we are looking for a an decreasing trend but found increasing one
            else left = mid + 1; // found the decreasing trend, start looking in the left side to find increasing trend
        }

        return left;
    }

    public static void main(String[] args) {
        int[] nums = {3, 5, 2, 7, 8, 10, 1};
        System.out.print("Peak element = " + FindPeakElement.findPeakElement(nums));
    }
}
