package practice.SlidingWindow;

import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Deque;

public class KSizedSubarrayMaximum {
    public ArrayList<Integer> maxOfSubarrays(int[] arr, int k) {
        // code here
        ArrayList<Integer> ans = new ArrayList<>();
        Deque<Integer> max = new ArrayDeque<>();
        int n = arr.length;
        int i = 0, j = 0;
        while (j < n) {
            while (!max.isEmpty() && max.peekLast() < arr[j]) {
                max.pollLast();
            }

            max.addLast(arr[j]);

            if (j - i + 1 == k) {
                int largest = max.peekFirst();
                ans.add(largest);
                if (arr[i] == largest) {
                    max.pollFirst();
                }
                i++;

            }
            j++;

        }

        return ans;

    }

    public static void main(String[] args) {
        KSizedSubarrayMaximum obj = new KSizedSubarrayMaximum();
        System.out.println(Arrays.toString(obj.maxOfSubarrays(new int[] { 1, 2, 3, 1, 4, 5, 2, 3, 6 }, 3).toArray()));
    }

}
