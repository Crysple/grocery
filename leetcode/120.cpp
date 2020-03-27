class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        int pre = 0;
        for(size_t i=1; i < triangle.size(); ++i){
            for(size_t j=0; j < triangle[i].size(); ++j){
                if (j != triangle[i].size()-1) pre = triangle[i-1][j];
                else pre = triangle[i-1][j-1];
                if (j != 0) pre = min(pre, triangle[i-1][j-1]);
                //if (j < triangle[i-1].size()-1) pre = min(pre, triangle[i-1][j+1]);
                triangle[i][j] += pre;
                if (i == triangle.size()-1 && j > 0)
                    triangle[i][j] = min(triangle[i][j], triangle[i][j-1]);
            }
        }
        return *(triangle.rbegin()->rbegin());
    }
};
