/*
 * @lc app=leetcode.cn id=1528 lang=java
 *
 * [1528] 重新排列字符串
 */

// @lc code=start
class Solution {
    public String restoreString(String s, int[] indices) {
        char[] ss = s.toCharArray();
        for (int i = 0; i < indices.length; i++) {
            while (indices[i] != i) {
                char tmp = ss[i];
                ss[i] = ss[indices[i]];
                ss[indices[i]] = tmp;

                int tmpInt = indices[i];
                indices[i] = indices[indices[i]];
                indices[tmpInt] = tmpInt;
            }
        }
        String res = new String(ss);
        return res;
    }
}
// @lc code=end

