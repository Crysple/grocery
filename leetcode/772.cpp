class Solution {
/* BNF
Expr ::= [+/-] <Term> {"+"|"-" <Term>}
Term ::= Factor {"*"|"/" <Factor>}
Factor ::= {'-'} ( Number | (' Expr ')' )
Number ::= Digit[Digit]
*/
private:
    string input;
    int idx;
    char lookahead(){
        while (input[idx] == ' ') ++idx;
        return input[idx];
    }
    char getchar(){
        return input[idx++];
    }
    long expr(){
        long res = 0;
        if (lookahead() != '+' && lookahead() != '-'){
            res += term();
        }
        while (lookahead() == '+' || lookahead() == '-'){
            //cout << res<<endl;
            if (getchar() == '+') res += term();
            else res -= term();
            //cout <<res<<endl;
        }
        return res;
    }
    long term(){
        //cout<<"term "<<lookahead()<<endl;
        long res = factor();
        while (lookahead() == '*' || lookahead() == '/'){
            if (getchar() == '*') res *= factor();
            else res /= factor();
        }
        return res;
    }
    long factor(){
        //cout<<"factor "<<lookahead()<<endl;
        long res = 1;
        if (lookahead() == '-'){
            res = -1;
            getchar();
        }
        if (lookahead() == '('){
            getchar();
            res *= expr();
            getchar(); // discard ) symbol
        }
        else if (lookahead()>='0' && lookahead()<='9')
            res *= number();
        return res;
    }
    long number(){
        //cout<<"number "<<lookahead()<<endl;
        long res = 0;
        while (lookahead()>='0' and lookahead()<='9'){
            res = res * 10 + (getchar()-'0');
        }
        return res;
    }
public:
    int calculate(string s) {
        input = s;
        return expr();
    }
};
