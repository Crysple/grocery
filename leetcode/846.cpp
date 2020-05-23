class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        if (hand.size() % W != 0) return false;
        int groups = hand.size() / W;
        map<int, int> cnt;
        for(int i: hand) cnt[i] += 1;
        for(auto& p: cnt){
            while (p.second > 0){
                for (int i = 0; i < W; ++i){
                    if (cnt[p.first + i] <= 0) return false;
                    cnt[p.first + i] -= 1;
                }
                groups -= 1;
            }
        }
        return groups == 0;
        // Original Answer: O(nlogm)
        // if (hand.size() % W != 0) return false;
        // int groups = hand.size() / W;
        // unordered_map<int, int> counter;
        // for(int i: hand) counter[i] += 1;
        // set<int> handset(hand.begin(), hand.end());
        // hand.clear();
        // hand.insert(hand.begin(), handset.begin(), handset.end());
        // int start = 0, next = 0;
        // //for_each(hand.begin(), hand.end(), [&](int i){cout<<i<<' '<<counter[i]<<endl;});
        // while (groups--){
        //     counter[hand[start]] -= 1;
        //     next = counter[hand[start]]?start:start+1;
        //     if (start + W > hand.size()) return false;
        //     for (int j = start+1; j < start + W; ++j){
        //         if (counter[hand[j]] <= 0 || hand[j] - hand[j-1] - 1) return false;
        //         counter[hand[j]] -= 1;
        //         if (j == next && counter[hand[j]] == 0) next += 1;
        //     }
        //     start = next;
        // }
        // return true;
    }
};
