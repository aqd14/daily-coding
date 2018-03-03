/**
 * S and T are strings composed of lowercase letters. In S, no letter occurs more than once.
 * <p>
 * S was sorted in some custom order previously. We want to permute the characters of T
 * so that they match the order that S was sorted. More specifically, if x occurs before y in S,
 * then x should occur before y in the returned string.
 * <p>
 * Return any permutation of T (as a string) that satisfies this property.
 * <p>
 * <p>
 * Example :
 * Input:
 * S = "cba"
 * T = "abcd"
 * Output: "cbad"
 * Explanation:
 * "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b", and "a".
 * Since "d" does not appear in S, it can be at any position in T. "dcba", "cdba", "cbda" are also valid outputs.'
 * <p>
 * Note:
 * <p>
 * S has length at most 26, and no character is repeated in S.
 * T has length at most 200.
 * S and T consist of lowercase letters only.
 */

public class CustomSortString {

    public static String customSortString(String S, String T) {
        char[] sChars = S.toCharArray();
        char[] tChars = T.toCharArray();

        int[] ranks = new int[26];
        int rank = 1;
        for (char c : sChars) ranks[c - 'a'] = rank++;

        int[] occurrences = new int[26];
        for (char c : tChars) occurrences[c - 'a']++;

        int curPos = 0;
        int temp;
        for (char c : sChars) {
            temp = occurrences[c - 'a'];
            occurrences[c - 'a'] = curPos;
            curPos += temp;
        }
        // now cusPos hold the last position of all characters in S

        char[] customSort = new char[tChars.length];
        for (char c : tChars) {
            int index = c - 'a';
            if (ranks[index] == 0) { // the characters that don't belong to S. Add them into last position
                customSort[curPos++] = c;
            } else {
                customSort[occurrences[index]] = c;
                occurrences[index]++;
            }
        }

        return new String(customSort);
    }

    public static void main(String[] args) {
        String S = "cba";
        String T = "abcd";

        String custom = CustomSortString.customSortString(S, T);
        System.out.println(custom);
    }
}
