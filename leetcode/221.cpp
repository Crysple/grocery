class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.size() == 0)
            return 0;
        vector<int> dp(matrix[0].size(), 0);
        int prev = 0, tmp=0, ans = 0;
        for (int i = 0; i < matrix.size(); ++i){
            for (int j = 0; j < matrix[i].size(); ++j){
                tmp = dp[j];
                if (i && j){
                    if (matrix[i][j] == '1')
                        dp[j] = min(min(dp[j], dp[j-1]), prev) + 1;
                    else
                        dp[j] = 0;
                }
                else dp[j] = matrix[i][j] - '0';
                prev = tmp;
                ans = max(ans, dp[j]);
            }
            cout<<endl;
        }
        return ans*ans;
    }
};
