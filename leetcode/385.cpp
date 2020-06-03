/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Constructor initializes an empty nested list.
 *     NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     NestedInteger(int value);
 *
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Set this NestedInteger to hold a single integer.
 *     void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     void add(const NestedInteger &ni);
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class Solution {
/* BNF
Expr ::= Number | List
List ::= \[ [Expr] {, Expr}\]
Number ::= Digit {Digit}
*/
private:
    string input;
    int idx;
    char lookahead(){
        return input[idx];
    }
    char getchar(){
        return input[idx++];
    }
    inline bool isdigit(char c){return c >= '0' && c <= '9';}
    NestedInteger expr(){
        NestedInteger res;
        if (isdigit(lookahead()) || lookahead() == '-')
            return number();
        else
            return list();
    }
    NestedInteger list(){
        getchar(); // discard [
        NestedInteger res;
        if (lookahead() != ']')
            res.add(expr());
        while (lookahead() != ']'){
            getchar(); // discard `,`
            res.add(expr());
        }
        getchar(); // discard ]
        return res;
    }
    NestedInteger number(){
        NestedInteger res;
        int n = 0, sign = 1;
        if (lookahead() == '-'){
            sign = -1;
            getchar();
        }
        while (isdigit(lookahead())) n = n * 10 + getchar() - '0';
        res.setInteger(n*sign);
        return res;
    }
public:
    NestedInteger deserialize(string s) {
        input = s;
        return expr();
    }
};
