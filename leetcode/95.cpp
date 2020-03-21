/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
private:
    unordered_map<int, vector<TreeNode*>* > tree_cache;
    int N;
    inline int hash(int l, int r) {return l-1 + r*N;}
    vector<TreeNode*> join(int root_value, const vector<TreeNode*>& left_subtrees, const vector<TreeNode*>& right_subtrees){
        vector<TreeNode*> trees;
        for (auto ltree: left_subtrees){
            for (auto rtree: right_subtrees){
                auto root = new TreeNode(root_value);
                root->left = ltree;
                root->right = rtree;
                trees.push_back(root);
            }
        }
        return trees;
    }
    vector<TreeNode*> rangeToBSTs(int begin, int end){
        if (tree_cache.count(hash(begin, end))) return *tree_cache[hash(begin, end)];
        vector<TreeNode*> generated_trees, left_subtrees{nullptr}, right_subtrees{nullptr};
        vector<TreeNode*>* trees = new vector<TreeNode*>;
        for (int root_value = begin; root_value <= end; ++root_value){
            if (root_value != begin)
                left_subtrees = rangeToBSTs(begin, root_value-1);
            if (root_value != end)
                right_subtrees = rangeToBSTs(root_value+1, end);
            generated_trees = this->join(root_value, left_subtrees, right_subtrees);
            trees->insert(trees->end(), generated_trees.begin(), generated_trees.end());
            left_subtrees = right_subtrees = {nullptr};
        }
        
        this->tree_cache[hash(begin, end)] = trees;
        return *trees;
    }
public:
    vector<TreeNode*> generateTrees(int n) {
        this->tree_cache.clear();
        this->N = n;
        return rangeToBSTs(1, n);
    }
};
