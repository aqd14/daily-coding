/**
 * Find the kth largest element in an unsorted array.
 * Note that it is the kth largest element in the sorted order, not the kth distinct element.
 * For example,
 * Given [3,2,1,5,6,4] and k = 2, return 5.
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 */

public class kthLargestElementArray {

    /**
     * Using the idea of quickselect algorithm.
     * time complexity O(n) in average. O(n^2) in the worst case. Might avoid using a clever way to select pivot
     * space complexity O(1)
     *
     * @param nums
     * @param k
     * @return
     */
    public static int findKthLargest(int[] nums, int k) {
        k = nums.length - k; // the expected index in the partitioned array
        int low = 0;
        int high = nums.length - 1;
        int index;

        while (low <= high) {
            index = partition(nums, low, high);
            if (index == k) {
                return nums[index];
            } else if (index < k) {
                low = index + 1;
            } else {
                high = index - 1;
            }
        }

        return -1;
    }

    private static int partition(int[] nums, int low, int high) {
        int pivot = nums[low];
        int start = low;
        int end = high + 1;

        while (true) {
            while (nums[++start] < pivot) {
                if (start == high) break;
            }

            while (nums[--end] > pivot) {
                if (end == low) break;
            }

            if (start >= end) {
                break;
            }

            swap(nums, start, end);
        }

        swap(nums, low, end);
        return end;
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = {1};
        System.out.print("element = " + kthLargestElementArray.findKthLargest(nums, 2));
    }
}
