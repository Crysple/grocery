class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        vector<unordered_map<string, int> > need_steps(2);
        for (string& ddd: deadends){
            if (ddd == "0000") return -1;
            need_steps[0][ddd] = need_steps[1][ddd] = -1;
        }
        if (target == "0000") return 0;
        need_steps[0]["0000"] = 0;
        need_steps[1][target] = 0;
        vector<queue<string> > q(2);
        q[0].push("0000");
        q[1].push(target);
        vector<int> offset {-1, 1};
        string curr;
        int cnt;
        while (!q[0].empty() && !q[1].empty()){
            for (int qid = 0; qid < 2; ++qid){
                curr = q[qid].front();
                cnt = need_steps[qid][curr];
                q[qid].pop();
                //cout<<curr<<' '<<cnt<<endl;
                for (int i = 0; i < 4; ++i){
                    for (int d: offset){
                        curr[i] = (curr[i] - '0' + d + 10) % 10 + '0';
                        // if it's not already visited in current queue and not a deadend
                        if (need_steps[qid].find(curr) == need_steps[qid].end()){
                            if (need_steps[qid^1].find(curr) != need_steps[qid^1].end()
                                    && need_steps[qid^1][curr] != -1){
                                // if it has been searched in another queue, return total steps
                                return cnt + 1 + need_steps[qid^1][curr];
                            }
                            need_steps[qid][curr] = cnt + 1;
                            q[qid].push(curr);
                        }
                        curr[i] = (curr[i] - '0' - d + 10) % 10 + '0';
                    }
                }
            }
        }
        return -1;
    }
};
