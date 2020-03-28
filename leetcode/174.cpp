class Solution {
public:
    int calculateMinimumHP(vector<vector<int>>& dungeon) {
        if (!dungeon.size()) return 0;
        int N = dungeon.size(), M = dungeon[0].size();
        dungeon.back().back() = max(0, -dungeon.back().back());
        for (int i = N-1; i >= 0; --i){
            for (int j = M-1; j >= 0; --j){
                if (i!=N-1 && j!=M-1)
                    dungeon[i][j] = min(dungeon[i+1][j], dungeon[i][j+1])-dungeon[i][j];
                else if (i!=N-1)
                    dungeon[i][j] = dungeon[i+1][j]-dungeon[i][j];
                else if (j!=M-1)
                    dungeon[i][j] = dungeon[i][j+1]-dungeon[i][j];
                dungeon[i][j] = max(dungeon[i][j], 0);
            }
        }
        return dungeon[0][0] + 1;
    }
};
