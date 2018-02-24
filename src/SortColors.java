//Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
//
//        Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
//
//        Note:
//        You are not suppose to use the library's sort function for this problem.

public class SortColors {
    // 1st approach: Using counting sort

    private static int[] countingSort(int[] nums, int k) {
        int[] count = new int[k];

        for (int num : nums) {
            count[num]++;
        }

        int numLength, startingIndex = 0;
        for (int i = 0; i < k; i++) {
            numLength = count[i];
            count[i] = startingIndex;
            startingIndex += numLength;
        }

        int[] output = new int[nums.length];
        for (int num : nums) {
            output[count[num]] = num;
            count[num]++;
        }

        return output;
    }

    // Divide the array into 3 partitions, separated by some indexes
    // 1. 0 -> begin-1: contains only 0's
    // 2. begin -> end: contains only 1's
    // 3. end+1 -> nums.length-1: contains only 2's
    public static void sortColors(int[] nums) {
        int beg = 0, end = nums.length - 1;
        for (int i = 0; i <= end && beg <= end; ) {
            if (nums[i] == 0) {
                swap(nums, beg, i);
                i++;
                beg++;
            } else if (nums[i] == 2) {
                swap(nums, end, i);
                end--;
            } else {
                i++;
            }
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 0, 2, 1, 0, 0, 1, 2, 0, 1};
        SortColors.sortColors(nums);
        for (int num : nums) {
            System.out.print(num + " ");
        }
    }
}
