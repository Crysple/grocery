
class Solution {
private:
    void pair_adde(pair<int, int>& a, const pair<int, int>& b, int i){
        if (i == 1)
            a.first += b.first;
        else
            a.second += b.second;
    }
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        if (!grid.size()) return 0;
        int N = grid.size(), M = grid[0].size();
        vector<vector<pair<int, int> > > dp(N, vector<pair<int, int> >(M, make_pair(0, 0)));
        for (int i = 0; i < N; ++i){
            for (int j = 0; j < M; ++j){
                if (grid[i][j] == 'W') continue;
                if (i) pair_adde(dp[i][j], dp[i-1][j], 1);
                if (j) pair_adde(dp[i][j], dp[i][j-1], 0);
                if (grid[i][j] == 'E'){
                    dp[i][j].first += 1;
                    dp[i][j].second += 1;
                }
            }
        }
        int ans = 0;
        pair<int, int> tmp;
        for (int i = N-1; i >= 0; --i){
            for (int j = M-1; j >= 0; --j){
                if (grid[i][j] == 'W') continue;
                tmp = dp[i][j];
                dp[i][j] = {0, 0};
                if (i-N+1!=0) pair_adde(dp[i][j], dp[i+1][j], 1);
                if (j-M+1!=0) pair_adde(dp[i][j], dp[i][j+1], 0);
                if (grid[i][j] == 'E'){
                    dp[i][j].first += 1;
                    dp[i][j].second += 1;
                }
                else{
                    pair_adde(tmp,  dp[i][j], 0);
                    pair_adde(tmp,  dp[i][j], 1);
                    ans = max(ans, tmp.first+tmp.second-(grid[i][j]=='E'?2:0));
                }
            }
        }
        return ans;
    }
};
