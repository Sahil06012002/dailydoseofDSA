package twopointets;

import java.util.HashMap;
import java.util.Map;

// Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

// In other words, return true if one of s1's permutations is the substring of s2.

 

// Example 1:

// Input: s1 = "ab", s2 = "eidbaooo"
// Output: true
// Explanation: s2 contains one permutation of s1 ("ba").

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        HashMap<Character,Integer> map1 = new HashMap<>();
        HashMap<Character,Integer> map2 = new HashMap<>();
        int len1= s1.length();
        int len2= s2.length();
        boolean ans = true;
        if(len1 > len2){
            return false;
        }

        for(int i=0; i<s1.length();i++){
            map1.put(s1.charAt(i),map1.getOrDefault(s1.charAt(i),0)+1);
        }
        for(int i=0; i<=s2.length()-s1.length();i++){

            String sb = s2.substring(i, i+s1.length());
            ans = true;
            System.out.println("substring---> " +sb);
            // create all the sub-strings of s1 length from s2
            for(int j=0;j<sb.length();j++){
            map2.put(sb.charAt(j),map2.getOrDefault(sb.charAt(j),0)+1);
            }
            System.out.println("freq---->");
            for (Map.Entry<Character, Integer> entry : map2.entrySet()) {
                System.out.println(entry.getKey() + " -> " + entry.getValue());
            }
            System.out.println("---------");
            // check if both s1 and sb have have equal frequency of all characters
            for(int k=0;k<s1.length();k++){
            int count1 = map1.get(s1.charAt(k));
            int count2 = map2.getOrDefault(s1.charAt(k),0);
            if(count1 != count2){
                ans = false;
                break;
            }
            
            }
            // if ans is true means both s1 and sb had equal frequencies and we can say s2 has a permutation of s1
            // and return true else we clear the map for the next substring
            if(ans) break;
            else map2.clear();

        }
        
        return ans;

    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        boolean ans = sol.checkInclusion("ab", "eidbaooo");
        System.out.println(ans);
    }
}
