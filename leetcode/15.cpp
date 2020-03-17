class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int> > sol;
        sort(nums.begin(), nums.end());
        int N = nums.size();
        for(int i = 0; i < N - 2; ++i){
            if(nums[i] + nums[i+1] + nums[i+2] > 0) break;
            if(i > 0 && nums[i] == nums[i-1]) continue;
            for(int j = i + 1, k = N - 1; j < k;){
                if (j > i + 1 && nums[j] == nums[j-1]) ++j;
                else if (nums[j] + nums[k] < -nums[i]) ++j;
                else if (nums[j] + nums[k] > -nums[i]) --k;
                else{
                    sol.push_back({nums[i], nums[j], nums[k]});
                    ++j;
                    --k;
                }
            }
        }
        
        return sol;
    }
};
