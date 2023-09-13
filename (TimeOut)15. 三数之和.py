class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = dict()
        st = set()
        for x in range(0,len(nums)):
            if nums[x] in d:    
                d[nums[x]] =  d[nums[x]] + 1
            else:
                d[nums[x]] = 1
        print(f"dict:{d}")
        for k,v in d.items():
            print(f"key:{k}")
            if v > 3:
                temp = 3
            else:
                temp = v
            if temp == 3:
                fir = k * temp
                if fir == 0:
                    print(f"3:{k,k,k}")
                    st.add((k,k,k))
                temp = temp - 1
            if temp == 2:
                fir = k * temp
                if -fir in d and fir != 0:
                    print(f"2:{k,k,-fir}")
                    lt= [k,k,-fir]
                    tp = tuple(sorted(lt))
                    st.add(tp)
                temp = temp - 1
            if temp == 1:
                fir = k * temp
                dc = d.copy()
                dc.pop(fir)
                
                # for kx ,vx in dc.items():
                #     for ky,vy in dc.items():
                #         if kx == ky and vx == vy == 2:
                #             if (2 * kx) == -fir:
                #                 lt= [kx,ky,fir]
                #                 tp = tuple(sorted(lt))
                #                 st.add(tp)
                #                 print(f"1:{kx,ky,fir}")
                #         elif kx != ky:
                #             if kx + ky == -fir:
                #                 lt= [kx,ky,fir]
                #                 tp = tuple(sorted(lt))
                #                 st.add(tp)
                #                 print(f"1:{kx,ky,fir}")
        rtype = list(st)
        for x in range(0,len(rtype)):
            rtype[x] = list(rtype[x])
        print(f"rtype:{rtype}")
        return rtype



s = Solution()
s.threeSum([1,0,-1,0])