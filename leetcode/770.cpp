class Solution {
/* BNF
Expr ::= [+/-] <Term> {+|- <Term>}
Term ::= Factor {* <Factor>}
Factor ::= {-} ( Var | Number | ( \( Expr \) )

Result stored as unordered_map:
    - string -> coff
    - value -> value as coff
*/
private:
    vector<string> tokens;
    int idx = 0;
    unordered_map<string, int> variables;
    /* Helper Functions */
    vector<string> split(const string& str, set<char> delimiters, bool withdel=true){
        vector<string> tokens;
        string token = "";
        for(char c: str){
            if (delimiters.find(c) != delimiters.end()){
                if (token != "") tokens.push_back(token);
                if (c != ' ' && c != '\0' && withdel) tokens.push_back(string(1, c));
                token = "";
            }
            else token += c;
        }
        if (token != "") tokens.push_back(token);
        //for_each(tokens.begin(),tokens.end(),[](string& t){cout<<t<<endl;});
        return tokens;
    }
    void split_and_sort(string& s){
        vector<string> vars = split(s, set<char>{'*'}, false);
        sort(vars.begin(), vars.end());
        s = vars[0];
        for (int i = 1; i < vars.size(); ++i) s += "*" + vars[i];
    }
    unordered_map<string, int> multiply(const unordered_map<string, int>& a, const unordered_map<string, int>& b){
        unordered_map<string, int> res;
        for (auto& i: a){
            for (auto& j: b){
                string term = i.first + "*" + j.first;
                if (term == "*"){ // both are number
                    res[""] += i.second * j.second;
                } else{ // have variables
                    split_and_sort(term);
                    res[term] += i.second * j.second;
                }
            }
        }
        return res;
    }

    /* Parsing Functions */
    string lookahead(int offset=0){
        return tokens[idx+offset];
    }

    string gettoken(){
        //cout<<tokens[idx]<<endl;
        return tokens[idx++];
    }
    inline bool isdigit(char c){ return c >= '0' && c <= '9';}
    
    unordered_map<string, int> expr(){
        unordered_map<string, int> res;
        int sign = 1;
        if (lookahead()[0] != '+' && lookahead()[0] != '-')
            res = term();

        while (lookahead()[0] == '+' || lookahead()[0] == '-'){
            sign = gettoken()[0]=='+'?1:-1;
            for (auto&& k: term()){
                res[k.first] += sign * k.second;
            }
        }
        return res;
    }
    unordered_map<string, int> term(){
        unordered_map<string, int> res = factor();
        while (lookahead()[0] == '*'){
            gettoken(); // discard *
            res = multiply(res, factor());
        }
        return res;
    }
    unordered_map<string, int> factor(){
        unordered_map<string, int> res;
        int sign = 1;
        string token = gettoken();
        if (token[0] == '-'){
            sign = -1;
            token = gettoken();
        }
        if (token[0] == '('){
            res = expr();
            for (auto& t: res) t.second = sign * t.second;
            gettoken(); // discard ) symbol
        }
        else if (isdigit(token[0])) // a number
            res[""] = sign * stoi(token);
        else{ // a variable
            if (variables.find(token) != variables.end())
                res[""] = sign * variables[token];
            else res[token] = sign;
        }
        return res;
    }
    void store_variables(const vector<string>& evalvars, const vector<int>& evalints){
        for (int i = 0; i < evalvars.size(); ++i)
            variables[evalvars[i]] += evalints[i];
    }
    static inline bool cmp(const string& a, const string& b){
        int da = count(a.begin(), a.end(), '*');
        int db = count(b.begin(), b.end(), '*');
        if (da != db) return da > db;
        return a < b;
    }
public:
    vector<string> basicCalculatorIV(string expression, vector<string>& evalvars, vector<int>& evalints) {
        store_variables(evalvars, evalints);
        tokens = split(expression, set<char>{'-', '+', '*', '(', ')', ' ', '\0'});
        tokens.push_back("$"); // guard for end of input
        auto res = expr();

        vector<string> ans;
        vector<string> keys;

        // sort keys according to term degree and alphabet
        for (auto& k: res) keys.push_back(k.first);
        sort(keys.begin(), keys.end(), cmp);

        string value = ""; // store numeric value if there is any
        for (auto& k: keys){
            if (res[k] == 0) continue;
            if (k == "") value = to_string(res[""]);
            else ans.push_back(to_string(res[k]) + "*" + k);
        }
        if (value != "") ans.push_back(value);
        return ans;
    }
};
