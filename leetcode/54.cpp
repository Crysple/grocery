class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        if (matrix.size() == 0) return res;
        int n = matrix.size(), m = matrix[0].size();
        int i = 0, j = 0;
        while (i < n - i - 1 && i < m - i - 1){
            res.insert(res.end(), matrix[i].begin()+i, matrix[i].end()-i);
            int end = n - i - 1;
            for (int j = i + 1; j < end; ++j) res.push_back(matrix[j][m-i-1]);
            res.insert(res.end(), matrix[end].rbegin()+i, matrix[end].rend()-i);
            for (int j = end - 1; j > i; --j) res.push_back(matrix[j][i]);
            i += 1;
        }
        if (i == n - i - 1)
            res.insert(res.end(), matrix[i].begin()+i, matrix[i].end()-i);
        else if (i == m - i - 1){
            for (int j = i; j < n - i; ++j) res.push_back(matrix[j][i]);
        }
        return res;
    }
};
