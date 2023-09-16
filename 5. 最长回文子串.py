class Solution:
    def longestPalindrome(self, s: str) -> str:
        begin = 0
        flag = 0
        end = len(s) -1
        pd = s
        maxpd = 0
        rtype = ""
        while(end != -1):
            if pd[begin] == pd[end]:
                begin = begin + 1
                end= end - 1
                if end <= begin:
                    if len(pd) > maxpd:
                        maxpd = len(pd)
                        rtype = pd
                    flag = flag + 1
                    begin = 0
                    pd = s[flag:]
                    end = len(pd) -1
            else:
                begin = 0
                pd = pd[:-1]
                end = len(pd) - 1
                if end <= begin:
                    flag = flag + 1
                    begin = 0
                    pd = s[flag:]
                    end = len(pd) -1
        return rtype
S = Solution()
r = S.longestPalindrome("aacabdkacaa")
print(r)