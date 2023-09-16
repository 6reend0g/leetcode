#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        
        for (int i = 0; i < nums.size(); ++i) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue; // Skip duplicates
            }
            
            int j = i + 1;
            int k = nums.size() - 1;
            
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                
                if (sum == 0) {
                    result.push_back({nums[i], nums[j], nums[k]});
                    
                    while (j < k && nums[j] == nums[j + 1]) {
                        j++; // Skip duplicates
                    }
                    while (j < k && nums[k] == nums[k - 1]) {
                        k--; // Skip duplicates
                    }
                    
                    j++;
                    k--;
                } else if (sum < 0) {
                    j++;
                } else {
                    k--;
                }
            }
        }
        
        return result;
    }
};
