class Solution {
/*
BNF:
Expr ::= Digit | Ternary
Ternary ::= [F|T] ? Expr : Expr
*/
private:
    string input;
    int idx = 0;
    char lookahead(int offset = 0){
        return input[idx+offset];
    }
    char getchar(){
        return input[idx++];
    }
    char expr(){
        if (lookahead(1) == '?') return ternary();
        else return digit();
    }
    char ternary(){
        char cond = getchar();
        getchar(); // discard `?`
        char res[2];
        res[0] = expr();
        getchar(); //discard `:`
        res[1] = expr();
        return res[cond != 'T'];
    }
    char digit(){
        return getchar();
    }
public:
    string parseTernary(string expression) {
        input = expression;
        return string(1, expr());
    }
};
