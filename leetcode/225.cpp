class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
        qs = {queue<int>(), queue<int>()};
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        qs[1-turn].push(x);
        while (!qs[turn].empty()){
            qs[1-turn].push(qs[turn].front());
            qs[turn].pop();
        }
        turn = 1 - turn;
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int tmp = qs[turn].front();
        qs[turn].pop();
        return tmp;
    }
    
    /** Get the top element. */
    int top() {
        return qs[turn].front();
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return qs[0].size() + qs[1].size() == 0;
    }
private:
    vector<queue<int> > qs;
    int turn = 0;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
