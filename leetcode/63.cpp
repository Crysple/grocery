class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        if (obstacleGrid[0][0]) return 0;
        vector<vector<long>> paths(obstacleGrid.size(), vector<long>(obstacleGrid[0].size(), 0));
        paths[0][0] = 1;
        for (size_t i = 0; i < obstacleGrid.size(); ++i){
            for (size_t j = 0; j < obstacleGrid[0].size(); ++j){
                if (obstacleGrid[i][j] == 1){
                    continue;
                }
                if (i != 0) paths[i][j] += paths[i-1][j];
                if (j != 0) paths[i][j] += paths[i][j-1];
            }
        }
        return paths[paths.size()-1][paths[0].size()-1];
    }
};
