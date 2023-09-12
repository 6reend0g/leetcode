#include <vector>
#include  <iostream>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        size_t it1 = 0;
        size_t it2 = height.size() - 1;
        int rtype = 0;
        while(it1 < it2){
            int area = calArea(min(height[it1],height[it2]),it2 - it1);
            if (area > rtype)
                rtype = area;
            if (height[it1] < height[it2])
                it1 ++;
            else
                it2 --;
        }
        return rtype;
    }
    int calArea(int h,int bot){
        return h * bot;
    }
};

int main(){
    vector<int> v = {2,3,4,5,18,17,6};
    Solution *s = new Solution();
    cout  << s -> maxArea(v);
}