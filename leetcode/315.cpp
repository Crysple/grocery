class Solution {
private:
    struct Node{
        int l, r, mid, cnt;
        Node *lnode, *rnode;
        Node(int _l, int _r):l(_l), r(_r), mid(l+(r-l)/2), cnt(0), lnode(nullptr), rnode(nullptr){};
    };
    Node* build_tree(int l, int r){
        // build tree for interval [l, r)
        if (l >= r) return nullptr;
        if (l == r - 1) return new Node(l, r);
        Node* root = new Node(l, r);
        root->lnode = build_tree(l, root->mid);
        root->rnode = build_tree(root->mid, r);
        return root;
    }
    void update(Node* root, int pos){
        if (root->l == root->r - 1) root->cnt += 1;
        else {
            if (pos < root->mid) update(root->lnode, pos);
            else update(root->rnode, pos);
            root->cnt = root->lnode->cnt + root->rnode->cnt;
        }
    }
    int query(Node* root, int l, int r){
        if (l>=r) return 0;
        if(l<=root->l && r>=root->r) return root->cnt;
        else{
            int ans = 0;
            if (l < root->mid) ans += query(root->lnode, l, r);
            if (r > root->mid) ans += query(root->rnode, l, r);
            return ans;
        }
    }
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> compressed_num, sorted_nums(nums.begin(), nums.end());
        sort(sorted_nums.begin(), sorted_nums.end());
        reverse(nums.begin(), nums.end());
        for(int n: nums){
            compressed_num.push_back(lower_bound(sorted_nums.begin(), sorted_nums.end(), n)-sorted_nums.begin()+1);
        }
        // for i, count number of num[j] < nums[i] & j < i;
        Node* root = build_tree(0, nums.size()+1);
        vector<int> ans;
        for(int n: compressed_num){
            ans.push_back(query(root, 0, n));
            update(root, n);
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
