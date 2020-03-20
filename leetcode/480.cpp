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
            
            if (nums[i] >= *median){
                window.insert(nums[i]);
                if (nums[i-k] <= *median){
                    ++median;
                }
                window.erase(window.lower_bound(nums[i-k]));
            } else{
                window.insert(nums[i]);
                auto to_remove = window.lower_bound(nums[i-k]);
                if (nums[i-k] > *median) --median;
                else if (nums[i-k] == *median){ //3 4 2 --> 4 2 3  // 2 3 4 -> 2 3(m) 3 4
                    // OmO (O!=m!=O) --> --median and remove to_remove
                    // OmO (O!=m==O) [median == to_remove] --> --median and remove to_remove
                    // OmO (O==m!=O) [median != to_remove] --> just remove to_remove
                    if (median == to_remove){
                        --median; //s2
                    }
                }
                window.erase(to_remove);
            }
        }
        return sliding_medians;
    }
};
