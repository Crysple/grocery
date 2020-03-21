class Solution {
private:
    int subarraySum(vector<int>& nums, int k) {
        // for_each(nums.begin(), nums.end(), [](int i){cout<<i<<' ';});
        // cout<<endl;
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
    vector<int> getPrefixSum(vector<int>& nums){
        vector<int> prefix_sum {0};
        for(int i=0; i<nums.size(); ++i){
            prefix_sum.push_back(prefix_sum[prefix_sum.size()-1] + nums[i]);
        }
        return prefix_sum;
    }
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0) return 0;
        int n_submatrix = 0;
        vector<vector<int> > prefix_sums;
        vector<int> vertical_arr;
        for (auto& arr: matrix){
            prefix_sums.push_back(getPrefixSum(arr));
        }
        for (int i = 0; i < matrix[0].size(); ++i){
            for (int j = 0; j <= i; ++j){
                vertical_arr.clear();
                for (int k = 0; k < matrix.size(); ++k){
                    vertical_arr.push_back(prefix_sums[k][i+1] - prefix_sums[k][j]);
                }
                n_submatrix += subarraySum(vertical_arr, target);
            }
        }
        return n_submatrix;
    }
};
