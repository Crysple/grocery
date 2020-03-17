class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int closest = accumulate(nums.begin(), nums.begin()+3, 0);
        sort(nums.begin(), nums.end());
        int N = nums.size();
        for(int i = 0; i < N - 2; ++i){
            if(i > 0 && nums[i] == nums[i-1]) continue;
            for(int j = i + 1, k = N - 1; j < k;){
                int sum = nums[i] + nums[j] + nums[k];
                if (abs(sum-target) < abs(closest-target))
                    closest = sum;
                if (sum > target) --k;
                else if (sum < target) ++j;
                else return target;
            }
        }
        
        return closest;
    }
};
