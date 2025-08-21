package binarysearch;

class Solution {
    public int binSearch(int[] arr , int target) {
        int start = 0;
        int end = arr.length-1;

        while(start <= end ) {
            int mid = (start + end) /2;
            if(arr[mid] == target) {
                return mid;
            }else if(arr[mid] < target) {
                start = mid +1;
            }else {
                end = mid-1;
            } 
        }

        return  -1 ;
    }

    public int ceil(int[] arr, int num) {
        int start  = 0, end = arr.length-1;
        int mid = (start+ end)/2;
        while(start <= end) {
            if(arr[mid] == num) {
                return mid;
            }else if(num > arr[mid]) {
                start  = mid +1;

            }else {
                end = mid -1;
            }
        }
        return start;
    }
    
    public static void main(String[] args) {
        Solution sol = new Solution();
        int ans = sol.binSearch(new int[]{1,2,3,4,5,6,7,8,9},10);
        System.out.println(ans);

    }
}