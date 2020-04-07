class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int dp[10001][1001] = {0}, ans = 0;
        for (int i = 0; i < A.size(); ++i){
            for (int j = 0; j < B.size(); ++j){
                if (A[i] == B[j]){
                    if (i == 0 or j == 0) dp[i][j] = 1;
                    else dp[i][j] = dp[i-1][j-1] + 1;
                    ans = max(dp[i][j], ans);
                }
            }
        }
        return ans;
    }
};
