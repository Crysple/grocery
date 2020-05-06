/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        auto cmp = [](const ListNode* a, const ListNode* b){return a->val > b->val;};
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp) > queue(cmp);
        for(ListNode* node: lists){
            if (node)
                queue.push(node);
        }
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;
        while (!queue.empty()){
            auto item = queue.top();
            queue.pop();
            tail->next = item;
            tail = item;
            if (tail->next) queue.push(tail->next);
        }
        tail = dummy->next;
        delete dummy;
        return tail;
    }
};
