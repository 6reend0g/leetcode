#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() < 2)
            return nums.size();
        sort(nums.begin(),nums.end());
        vector<int> conseq = {nums[0]};
        int max = 0;
        for(auto a = 1;a < nums.size();a++){
            if (nums[a] == conseq.back() + 1 || (conseq[0] == 0 && conseq.size() == 1 && nums[a] == conseq.back() + 1) || conseq.empty())
                conseq.push_back(nums[a]);
            else if (nums[a] == conseq.back())
                ;
            else{
                conseq.clear();
                conseq.push_back(nums[a]);
            }
            if (conseq.size() > max)
                max = conseq.size();
        }
        return max ;
    }
};

int main(){
    Solution *s = new Solution;
    vector<int> vec = {100,4,200,1,3,2};
    int si = s->longestConsecutive(vec);
    cout << si ;
}