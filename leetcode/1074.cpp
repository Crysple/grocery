class Solution {
private:
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int n = matrix.size(), m = matrix[0].size(), ans = 0, presum = 0;
        unordered_multiset<int> sum_cnt;
        vector<int> row(m);
        for(int i = 0; i < n; ++i){
            //for(int col = 0; col < m; ++col) row[col] = matrix[i][col];
            row.assign(m, 0);
            for(int j = i; j < n; ++j){
                sum_cnt.clear();
                sum_cnt.insert(0);
                presum = 0;
                for(int col = 0; col < m; ++col){
                    row[col] += matrix[j][col];
                    presum += row[col];
                    ans += sum_cnt.count(presum-target);
                    sum_cnt.insert(presum);
                }
            }
        }
        return ans;
    }
};
