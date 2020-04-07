class Solution {
public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int K) {
        if (matrix.size() == 0) return 0;
        vector<int> sorted_arr;
        for (auto& arr: matrix)
            for (size_t i = 1; i < arr.size(); ++i)
                arr[i] += arr[i-1];
        int csum = 0, maxsum = - INT_MAX;
        for (int i = 0; i < matrix[0].size(); ++i){
            for (int j = -1; j < i; ++j){
                csum = 0;
                sorted_arr.clear();
                sorted_arr.push_back(0);
                for (int k = 0; k < matrix.size(); ++k){
                    csum += matrix[k][i] - (j<0?0:matrix[k][j]);
                    auto it = lower_bound(sorted_arr.begin(), sorted_arr.end(), csum-K);
                    if (it != sorted_arr.end()) maxsum = max(maxsum, csum-*it);
                    sorted_arr.insert(lower_bound(sorted_arr.begin(), sorted_arr.end(), csum), csum);
                }
            }
        }
        return maxsum;
    }
};
