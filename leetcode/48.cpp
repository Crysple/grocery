class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int bound = 0, N = matrix.size();
        for (int i = 0; i < N; ++i){
            bound = N - i - 1;
            for (int j = i; j < bound; ++j){
                swap(matrix[i][j], matrix[j][bound]);
                swap(matrix[i][j], matrix[bound][N-j-1]);
                swap(matrix[i][j], matrix[N-j-1][N-bound-1]);
            }
        }
    }
};
