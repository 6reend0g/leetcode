import copy
class Solution(object):
    def __init__(self):
        self.hash_map = dict()
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        origin_strs = copy.deepcopy(strs)
        summary = ''
        for x in range(0,len(strs)):
            strs[x] = sorted(strs[x])
            for y in range(0,len(strs[x])):
                summary = summary + str(ord(strs[x][y]))
            self.appendNode(summary,origin_strs[x])
            summary = ''
        
        
        rtype = list(self.hash_map.values())
        return rtype
            
    def appendNode(self,summary,string):
        if not self.hash_map.get(summary,False):
            self.hash_map.setdefault(summary,[string])
        else :
             self.hash_map[summary].append(string)

strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
s = Solution()
rt = s.groupAnagrams(strs)
print(rt)
