class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> value2index;
        int n = 0;
        for (int i = 0; i < int(nums.size()); ++i){
            n = nums[i];
            if (value2index.count(target-n) == 1) return {i, value2index[target-n]};
            value2index[n] = i;
        }
        return {-1, -1};
    }
};
