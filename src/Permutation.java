/**
 * @author doquocanh
 */

import java.util.Arrays;

// Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
// In other words, one of the first string's permutations is the substring of the second string.
//        --------------------------------------------
//        Example 1:
//        Input:s1 = "ab" s2 = "eidbaooo"
//        Output:True
//        Explanation: s2 contains one permutation of s1 ("ba").
//        --------------------------------------------
//        Example 2:
//        Input:s1= "ab" s2 = "eidboaoo"
//        Output: False
//        --------------------------------------------
//        Note:
//        The input strings only contain lower case letters.
//        The length of both given strings is in range [1, 10,000].

class Permutation {

    /**
     * Naive approach: check for every permutation
     * @param s1
     * @param s2
     * @return
     */
    public static boolean dummyCheckInclusion(String s1, String s2) {
        // Get all the permutation of s1
        return permutations("", s1, s2);
    }

    private static boolean permutations(String prefix, String suffix, String target) {
        if (suffix.isEmpty()) {
            if (target.contains(prefix)) {
                return true;
            }
        } else {
            for (int i = 0; i < suffix.length(); i++) {
                boolean found = permutations(prefix + suffix.charAt(i), suffix.substring(0, i) + suffix.substring(i + 1), target);
                if (found) {
                    return true;
                }
            }
        }
        return false;
    }

    /**
     * For each substring of length s1 of s2, check if the character frequency is the same as s1
     * @param s1
     * @param s2
     * @return
     */
    public static boolean checkInclusion(String s1, String s2) {

        if (s1.length() > s2.length()) {
            return false;
        }

        // Assume the input strings contain only lower case letters [a-z] <-> [97-123] in ASCII
        int[] aux1 = generateFrequencyArray(s1);

        for (int i = 0; i <= s2.length() - s1.length(); i++) {
            String temp = s2.substring(i, i + s1.length());
            int[] aux = generateFrequencyArray(temp);
            if (Arrays.equals(aux1, aux)) {
                return true;
            }
        }
        return false;
    }

    private static int[] generateFrequencyArray(String s) {
        int[] aux = new int[26];
        for (int i = 0; i < s.length(); i++) {
            int ind = asciiToIndex((int) s.charAt(i));
            aux[ind]++;
        }

        return aux;
    }

    private static int asciiToIndex(int asciiValue) {
        return asciiValue % 97;
    }

    public static void main(String[] args) {
        System.out.println(Permutation.checkInclusion("adc", "dcda"));
        System.out.println(Permutation.checkInclusion("ab", "eidboaoo"));
    }
}