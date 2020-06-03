/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
private:
    void concatenate(Node* src, Node* dst){
        src->next = dst;
        dst->prev = src;
    }
    Node* _flatten(Node* head) {
        // return its tail
        Node *pos = head, *child_tail = nullptr, *tail = nullptr;
        while (pos){
            while (pos && !pos->child) {tail = pos; pos = pos->next;}
            if (pos && pos->child){
                tail = child_tail = _flatten(pos->child);
                if (pos->next){
                    concatenate(child_tail, pos->next);
                }
                concatenate(pos, pos->child);
                pos->child = nullptr;
            }
        }
        return tail;
    }
public:
    Node* flatten(Node* head) {
        _flatten(head);
        return head;
    }
};
