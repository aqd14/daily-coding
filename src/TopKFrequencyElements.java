// Given a non-empty array of integers, return the k most frequent elements.
//
//        For example,
//        Given [1,1,1,2,2,3] and k = 2, return [1,2].
//
//        Note:
//        You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
//        Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class TopKFrequencyElements {
    public List<Integer> topKFrequent(int[] nums, int k) {
        ArrayList<Integer> results = new ArrayList<>();
        HashMap<Integer, Integer> maps = new HashMap<>(); // mapping between a number and its occurrence;

        int maxFrequency = 0;
        for (int i = 0; i < nums.length; i++) {
            if (maps.containsKey(nums[i])) {
                maps.put(nums[i], maps.get(nums[i]) + 1);
                maxFrequency = Math.max(maxFrequency, maps.get(nums[i]));
            } else {
                maps.put(nums[i], 0);
            }
        }

        // A multi-layer bucket contains numbers and associated frequency
        // buckets[i] contains a list of number with i occurences
        ArrayList<Integer>[] buckets = (ArrayList<Integer>[]) new ArrayList[maxFrequency + 1];
        for (int i = 0; i <= maxFrequency; i++) {
            buckets[i] = new ArrayList<>();
        }

        for (int key : maps.keySet()) {
            int frequency = maps.get(key);
            buckets[frequency].add(key);
        }

        for (int fr = maxFrequency; fr >= 0; fr--) {
            for (int num : buckets[fr]) {
                results.add(num);
                if (results.size() == k) {
                    return results;
                }
            }
        }

        return results;
    }
}
