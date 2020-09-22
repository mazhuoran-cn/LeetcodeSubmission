/*
 * @lc app=leetcode.cn id=1528 lang=java
 *
 * [1588] 有奇数长度子数组的和
 */

// @lc code=start
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int res = 0;
        for (int i = 1; i <= arr.length; i++) {
            if(i%2==1) {
                for (int j = 0; j < arr.length - i + 1; j++) {
                    for (int k = j; k < j + i; k++) {
                        res += arr[k];
                    }
                }
            }
        }
        return res;
    }
}// @lc code=end
