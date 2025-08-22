package binarysearch;

class Solution {
    public int binSearch(int[] arr , int target,boolean flag) {
        int s = 0, e = arr.length-1;
        int ans = -1;
        while(s <= e){
            int mid = (s+e)/2;
            if(arr[mid] == target){
                ans = mid;
                if (flag) {
                e = mid-1;

                }else {
                    s = mid +1;
                }
            }else if(arr[mid] > target){
                e = mid-1;
            }else{
                s = mid+1;
            }
        }
        return ans;
        }


        public int[] test(int[] arr , int target) {
            int a = binSearch(arr,target,true);
            int b = binSearch(arr,target,false);
            int[] ans = new int[2];
            ans[0] = a;
            ans[1] = b;
            return ans;
        }
    public static void main(String[] args) {
        Solution sol = new Solution();

        int[] result = sol.test(new int[]{3,7,7,8,8,10}, 8);
        System.out.println(result);
    }
        
}
