class Solution {
public:
    bool isRectangleCover(vector<vector<int>>& rectangles) {
        unordered_map<int, unordered_map<int, bool>> corner;
        vector<pair<int, int>> corner_ids = {{0, 1}, {0, 3}, {2, 1}, {2, 3}};
        auto cover = rectangles[0];
        long area = 0;
        auto get_area = [](const vector<int>& rect){return (rect[2]-rect[0])*(rect[3]-rect[1]);};
        for(auto& rect: rectangles){
            for (auto [i, j]: corner_ids){
                if (corner[rect[i]][rect[j]]){
                    corner[rect[i]].erase(rect[j]);
                }
                else corner[rect[i]][rect[j]] = true;
            }
            cover[0] = min(cover[0], rect[0]);
            cover[1] = min(cover[1], rect[1]);
            cover[2] = max(cover[2], rect[2]);
            cover[3] = max(cover[3], rect[3]);
            area += get_area(rect);
        }
        
        if (area != get_area(cover)) return false;
        int n_corner = 0;
        for (auto it = corner.begin(); it != corner.end(); ++it){
            auto& inner_map = (*it).second;
            int x = (*it).first;
            if (inner_map.size() != 0){
                if (inner_map.size() != 2) return false;
                n_corner += 2;
                if(x != cover[0] && x != cover[2]) return false;
                if (inner_map.find(cover[1]) == inner_map.end()) return false;
                if (inner_map.find(cover[3]) == inner_map.end()) return false;
            }
        }
        return n_corner == 4;
    }
    // Swiping line: O(nlogn)
    // struct comp {
    //     bool operator () (const pair<int, int>& a, const pair<int, int>& b) const { return a.second <= b.first; }
    // };
    // bool isRectangleCover(vector<vector<int>>& rectangles) {
    //     multiset<pair<int, int>, comp> intervals;
    //     vector<vector<int>> lines;
    //     auto cover = rectangles[0];
    //     long area = 0;
    //     auto get_area = [](const vector<int>& rect){return (rect[2]-rect[0])*(rect[3]-rect[1]);};
    //     for(auto& rect: rectangles){
    //         // 1 for start, -1 for end -- end first
    //         lines.push_back({rect[0], 1, rect[1], rect[3]});
    //         lines.push_back({rect[2], -1, rect[1], rect[3]});
    //         cover[0] = min(cover[0], rect[0]);
    //         cover[1] = min(cover[1], rect[1]);
    //         cover[2] = max(cover[2], rect[2]);
    //         cover[3] = max(cover[3], rect[3]);
    //         area += get_area(rect);
    //     }
    //     if (area != get_area(cover)) return false;
    //     sort(lines.begin(), lines.end());
    //     for(auto& line: lines){
    //         //cout<<line[0]<<' '<<line[1]<<' '<<line[2]<<endl;
    //         auto it = intervals.find(make_pair(line[2], line[3]));
    //         if (line[1] == 1){
    //             if (it != intervals.end()) return false;
    //             intervals.insert(make_pair(line[2], line[3]));
    //         }
    //         else intervals.erase(it);
    //     }
    //     return true;
    // }
};
