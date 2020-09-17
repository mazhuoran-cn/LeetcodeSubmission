import java.util.HashMap;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=3 lang=java
 *
 * [3] 无重复字符的最长子串
 */
// asdfqwetdsfgasdfasdf
// @lc code=start
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int res = 0;
        int tail = 0;
        int head = 0;
        int length = s.length();
        for(head=0; head<length; head++){
            char c = s.charAt(head);
            if(map.containsKey(c) && map.get(c) >= tail){
                int len = head - tail;
                tail = map.get(c) + 1;
                res = (len > res) ? len : res;
            }
            map.put(c, head);
        }
        res = (head-tail>res)? head-tail : res;
        return res;
    }
}
// @lc code=end
