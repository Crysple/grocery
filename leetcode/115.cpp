class Solution {
public:
    int numDistinct(string s, string t) {
        if (s.size() < t.size()) return 0;
        if (t.size() == 0) return 1;
        vector<long> dp(t.size());
        for (size_t j = 0; j < s.size(); ++j){
            for (size_t i = t.size()-1;; --i){
                if (t[i] == s[j])
                    dp[i] += (i>0)?dp[i-1]:1;
                if (i == 0) break;
            }
        }
        return dp.back();
    }
};
