class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() < 3) return nums.size();
        int lo = 2, pre = nums[1], prepre = nums[0];
        for (int hi = 2; hi < nums.size(); ++hi){
            bool is_dup = nums[hi] == pre && nums[hi] == prepre;
            prepre = pre, pre = nums[hi];
            if (!is_dup){
                nums[lo++] = nums[hi];
            }
        }
        return lo;
    }
};
