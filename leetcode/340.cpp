class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        if (k <= 0) return 0;
        this->capacity = k;
        int ans = 0, start = -1;
        for(int i = 0; i < s.size(); ++i){
            if (kit.size() == k && kit.find(s[i]) == kit.end()){
                start = this->put(s[i], i);
            }
            else this->put(s[i], i);
            //cout<<s[i]<<' '<< char(this->cache.back().first)<< this->cache.back().second << ' ' << start <<endl;
            ans = max(ans, i - start);
        }
        return ans;
    }
    
    int get(int key) {
        auto it = kit.find(key);
        if (it == kit.end()) return -1;
        auto it2kv = it->second;
        cache.insert(cache.begin(), make_pair(key, it2kv->second));
        cache.erase(it2kv);
        it->second = cache.begin();
        return cache.front().second;
    }
    
    int put(int key, int value) {
        auto it = kit.find(key);
        int res = -1;
        if (it != kit.end()){ //already there, then move to head and set value, update key2iterator
            it->second->second = value;
            cache.insert(cache.begin(), *(it->second));
            cache.erase(it->second);
            kit[key] = cache.begin();
        }
        else{
            if (cache.size() >= this->capacity){ // full, remove the last one, update kit(first)
                kit.erase(cache.back().first);
                res = cache.back().second;
                cache.pop_back();
            }
            cache.insert(cache.begin(), make_pair(key, value));
            kit[key] = cache.begin();
        }
        return res;
    }
private:
    int capacity;
    typedef int KEY;
    typedef int VALUE;
    set<VALUE> val;
    list<pair<KEY, VALUE>> cache;
    typedef list<pair<KEY, VALUE>>::iterator CIT;
    //unordered_map<KEY, VALUE> kv;
    unordered_map<KEY, CIT> kit;
};

