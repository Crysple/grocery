class Solution {
public:
    vector<double> medianSlidingWindow(vector<int>& nums, int k) {
        multiset<long> window(nums.begin(), nums.begin()+k);
        vector<double> sliding_medians;
        auto median = window.begin();
        advance(median, k/2-(k&1^1));// when k is even, median is the former
        for(int i = k;; ++i){
            if (k&1) sliding_medians.push_back(*median);
            else sliding_medians.push_back((*median + *(next(median,1)))/2.0);
            // for_each(window.begin(), window.end(), [](int i){cout<<i<<' ';});
            // cout<<endl<<*median<<endl;
            if (i == int(nums.size())) break;
            
            window.insert(nums[i]);
            auto to_remove = window.lower_bound(nums[i-k]);
            if (nums[i] >= *median){
                if (nums[i-k] <= *median){
                    ++median;
                }
            }
            else if (nums[i-k] > *median || (nums[i-k] == *median && median == to_remove)){
                    --median;
            }
            window.erase(to_remove);
        }
        return sliding_medians;
    }
};
