class Solution {
private:
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        if (matrix.size() == 0) return 0;
        int n_submatrix = 0;
        unordered_map<int, int> presum;
        for (auto& arr: matrix)
            for (size_t i = 1; i < arr.size(); ++i)
                arr[i] += arr[i-1];
        int csum = 0;
        for (int i = 0; i < matrix[0].size(); ++i){
            for (int j = -1; j < i; ++j){
                csum = 0;
                presum.clear();
                presum[0] = 1;
                for (int k = 0; k < matrix.size(); ++k){
                    csum += matrix[k][i] - (j<0?0:matrix[k][j]);
                    if (presum.count(csum-target)) n_submatrix += presum[csum-target];
                    presum[csum] += 1;
                }
            }
        }
        return n_submatrix;
    }
};
