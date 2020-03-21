class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int, int > prefix_sum{{0, 1}};
        int sum = 0, n_subarrays = 0;
        for (int i = 0; i < nums.size(); ++i){
            sum += nums[i];
            if (prefix_sum.count(sum - k))
                n_subarrays += prefix_sum[sum - k];
            ++prefix_sum[sum];
        }
        return n_subarrays;
    }
};
