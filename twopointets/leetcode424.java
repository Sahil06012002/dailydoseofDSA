package twopointets;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.HashMap;

// You are given a string s and an integer k. You can choose any character 
// of the string and change it to any other uppercase English character. You can 
// perform this operation at most k times.

// Return the length of the longest substring containing the same letter you 
// can get after performing the above operations.

 

// Example 1:

// Input: s = "ABAB", k = 2
// Output: 4
// Explanation: Replace the two 'A's with two 'B's or vice versa.


public class leetcode424 {

    public int characterReplacement(String s, int k) {
        int count = 0,i=0,j=0;
        int[] freq = new int[26];
        Arrays.fill(freq, 0);
        int maxF = 0;


        while(i<s.length() && j<s.length()) {
            freq[s.charAt(j)-'A']++;
            maxF = Math.max(maxF, freq[s.charAt(j)-'A']);
            while((j-i+1)-maxF > k){
                freq[s.charAt(i)-'A']-=1;
                i++;
            }
            count = Math.max(count,(j-i+1));
            j++;
        }
        return count;
        
    }


    public int characterReplacement1(String s, int k) {
        HashMap<Character, Integer> freqs = new HashMap<>();
        int res = 0, i = 0, maxFreq = 0;

        for (int j = 0; j < s.length(); j++) {
            char c = s.charAt(j);
            freqs.put(c, freqs.getOrDefault(c, 0) + 1);
            maxFreq = Math.max(maxFreq, freqs.get(c));

            while ((j - i + 1) - maxFreq > k) {
                char left = s.charAt(i);
                freqs.put(left, freqs.get(left) - 1);
                i++;
            }

            res = Math.max(res, j - i + 1);
        }

        return res;
    }



    public static void main(String[] args) {
        
        
    }
    
}
