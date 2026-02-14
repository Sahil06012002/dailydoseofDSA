class Solution {
    public int binarySearch(int[] arr, int target) {
        int s = 0, e = arr.length;
        int mid = (s + e) / 2;
        while (s <= e) {
            if (arr[mid] == target) {
                return target;
            } else if (arr[mid] < target) {
                s = mid + 1;
            } else {
                e = mid - 1;
            }
        }
        return -1;
    }

    public int recursiveBinarySearch(int[] arr, int target, int s, int e) {
        int mid = (s + e) / 2;
        if (arr[(s + e) / 2] == target) {
            return (s + e) / 2;
        }
        if (arr[mid] < target) {
            recursiveBinarySearch(arr, target, mid + 1, e);
        }
        if (arr[mid] > target) {
            recursiveBinarySearch(arr, target, s, mid - 1);
        }
        return -1;
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        int ans = sol.binarySearch(new int[] { 1, 2, 3, 4, 5, 6, 7 }, 7);
        int recAns = sol.recursiveBinarySearch(new int[] { 1, 2, 3, 4, 5, 6, 7 }, 7, 0, 7);
        System.out.println(ans);
        System.out.println(recAns);

    }
}