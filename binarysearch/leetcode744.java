package binarysearch;
//  744. Find Smallest Letter Greater Than Target

// You are given an array of characters letters that is sorted in non-decreasing order, 
// and a character target. There are at least two different characters in letters.

// Return the smallest character in letters that is lexicographically greater than target. 
// If such a character does not exist, return the first character in letters.


// Example 1:

// Input: letters = ["c","f","j"], target = "a"
// Output: "c"
// Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
// Example 2:

// Input: letters = ["c","f","j"], target = "c"
// Output: "f"
// Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
// Example 3:

// Input: letters = ["x","x","y","y"], target = "z"
// Output: "x"
// Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].


class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int s = 0, e = letters.length-1;
        while(s <= e ){
            int mid = (s+e)/2;
            if(letters[mid] <= target) {
                s = mid +1;
    
            }else {
                e = mid-1;
            }
            
        }
        if (s < letters.length){
            return letters[s];
        }
        else {
            return letters[0];
            }
    }
    public static void main(String[] args) {
        Solution sol = new Solution();
        char ans = sol.nextGreatestLetter(new char[]{'x','x','y','y'},'z');
        System.out.println(ans);

    }
}