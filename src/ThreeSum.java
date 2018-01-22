/**
 * Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
 * Find all unique triplets in the array which gives the sum of zero.
 * Note: The solution set must not contain duplicate triplets.
 * For example, given array S = [-1, 0, 1, 2, -1, -4],
 * A solution set is:
 * [
 *    [-1, 0, 1],
 *    [-1, -1, 2]
 * ]
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class ThreeSum {

    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        ArrayList<Integer> cache = new ArrayList<>(Arrays.asList(-1, -1, -1));
        ArrayList<List<Integer>> finalSet = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            // ignore all successfully added triplet
            while (i > 0 && i < nums.length && nums[i] == nums[i-1]) i++;
            // start new run
            int beg = i + 1;
            int end = nums.length - 1;
            while (beg < end) {
                int sum = nums[beg] + nums[end];
                if (nums[i] + sum == 0) {
                    // ignore all duplicate triplets
                    ArrayList<Integer> candidate = new ArrayList<>(Arrays.asList(nums[i], nums[beg], nums[end]));
                    if (!cache.equals(candidate)) {
                        finalSet.add(candidate);
                        cache = candidate;
                    }
                    while (beg < end && nums[beg] == nums[beg + 1]) beg++;
                    while (beg < end && nums[end] == nums[end - 1]) end--;
                    beg++;
                    end--;
                } else if (nums[i] + sum > 0) {
                    end--;
                } else {
                    beg++;
                }
            }
        }
        return finalSet;
    }

    public List<List<Integer>> threeSumHash(int[] nums) {
        Arrays.sort(nums);

        HashMap<List<Integer>, Integer> cache = new HashMap<>(); // keep track of added triplet
        ArrayList<List<Integer>> finalSet = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            int beg = i+1;
            int end = nums.length-1;
            while (beg < end) {
                int sum = nums[beg]+nums[end];
                if (nums[i] + sum == 0) {
                    // Using hash function will run slower more time
                    List<Integer> candidate = Arrays.asList(nums[i], nums[beg++], nums[end--]);
                    if (!cache.containsKey(candidate)) {
                        finalSet.add(candidate);
                        cache.put(candidate, finalSet.size());
                    }
                } else if (nums[i] + sum > 0) {
                    end--;
                } else {
                    beg++;
                }
            }
        }
        return finalSet;
    }

    public static void main(String[] args) {
//        int[] nums = {-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6};
        int[] nums = {-1,0,1,2,-1,-4};

        ArrayList<List<Integer>> solutionSet = (ArrayList)new ThreeSum().threeSum(nums);
        System.out.print(solutionSet);
    }
}
