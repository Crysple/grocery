class Solution {
/* Try BNF
Expr ::= Let | Addmult | Term 
Let ::= '(' {Var Expr} Expr ')'
Addmult ::= '(' ('add'|'mult') Expr Expr ')'
Term ::= ({'-'} Number) | Var
Number ::= digit {digit}
Var :: char {char|digit}

But for let statement:
Cuz Expr => Var, you cannot decide whether there's another {Var Expr} or not without LL(2)
But if next == '(', then it's definitely expr()
*/
private:
    vector<string> tokens;
    int idx = 0;
    map<string, vector<int>> variables;
    vector<string> split_string(const string& str){
        vector<string> tokens;
        string token = "";
        for(char c: str){
            if (c == ')' || c == '('){
                if (token != "")
                    tokens.push_back(token);
                tokens.push_back(string(1, c));
                token = "";
            }
            else if (c == ' ' || c == '\0'){
                if (token != "")
                    tokens.push_back(token);
                token = "";
            }
            else token += c;
        }
        return tokens;
    }
    string lookahead(int offset=0){
        return tokens[idx+offset];
    }
    string gettoken(){
        //cout<<tokens[idx]<<endl;
        return tokens[idx++];
    }
    inline bool isnumber(const string& s){ return (s[0] >= '0' && s[0] <= '9') || s[0] == '-';}
    int expr(){
        int res = 0;
        if (lookahead() == "(") {
            if (lookahead(1) == "let") res = let();
            else if (lookahead(1) == "add" || lookahead(1) == "mult") res = addmult();
            else throw "Error";
        }
        else{
            res = term();
        }
        return res;
    }
    int let(){
        gettoken(), gettoken(); //discard `(`, `let`
        int res = 0;
        string token;
        vector<string> var_name;
        while (true){
            token = lookahead();
            if (token[0] == '('){ // must be a expression
                res = expr();
                break;
            }
            if (isnumber(token)){ // a number
                cout<<"---"<<token<<endl;
                res = stoi(token);
                break;
            }
            // then it should be a variable -- token
            token = gettoken();
            if (lookahead()[0] == ')'){
                res = variables[token].back();
                break;
            }
            else{
                var_name.push_back(token);
                variables[token].push_back(expr());
            }
        }
        gettoken(); // discard )
        for (string& var: var_name){
            variables[var].pop_back();
        }
        return res;
    }
    int addmult(){
        gettoken(); // discard (
        string op = gettoken();
        int operand1 = expr(), operand2 = expr();
        gettoken(); //discard ')'
        return op=="add"?operand1+operand2:operand1*operand2;
    }
    int term(){
        int res = 0;
        if (isnumber(lookahead())){
            res = number();
        }
        else res = var();
        return res;
    }
    int number(){
        return stoi(gettoken());
    }
    int var(){
        return variables[gettoken()].back();
    }
public:
    int evaluate(string expression) {
        tokens = split_string(expression);
        return expr();
    }
};
