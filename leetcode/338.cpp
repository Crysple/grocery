class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans {0};
        int pos = 1;
        for (int i = 1; i <= num; ++i){
            if (!(i&(i-1))){
                ans.push_back(1);
                pos = 1;
            }
            else{
                ans.push_back(1 + ans[pos++]);
            }
        }
        return ans;
    }
};
// 1,   10, 11,     100, 101, 110, 111,       1000, 1001, 1010, 1011, 1100, 1101, 1110, 1111   10000
// 1,   1,  1+1,      1,   2,   2,   3,         1.    1+1   1+1   1+2   1+1   1+2   1+2   1+3

/*
1

2
3 -> 1

4
5 -> 1
6 -> 2
7 -> 3

8
9 -> 1
10 -> 2

*/
