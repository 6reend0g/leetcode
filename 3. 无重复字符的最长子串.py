class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        elif len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        subs = s[0]
        maxlen = 1
        cnt = 0
        x = 1
        while(True):
            # print(subs,s[x])
            if subs.find(s[x]) >= 0:
                if cnt < len(s) - 1:
                    cnt = cnt + 1
                    x = cnt
                subs = s[x]
            else:
                subs = subs + s[x]
            print(subs,s[x])
            if len(subs) > maxlen:
                maxlen = len(subs)
            if x == len(s) - 1:
                cnt = cnt + 1
                x = cnt
                if cnt == len(s):
                    break
                subs = s[x]
                continue
            x = x + 1
            
        print(maxlen)
        return maxlen


s = "aab"
sol = Solution()
sol.lengthOfLongestSubstring(s)