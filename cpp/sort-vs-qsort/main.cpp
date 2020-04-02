//
//  main.cpp
//  cpppg
//
//  Created by zejunlin on 3/18/20.
//  Copyright © 2020 Danny. All rights reserved.
//

#include <chrono>
#include <iostream>
#include <functional>
#include <string>
#include <stdlib.h>
#include <random>
#include <vector>
using namespace std;

const int N = 1000000;
const long long SEED = chrono::steady_clock::now().time_since_epoch().count();
mt19937 RNG(SEED);
//const int N = 10;


/* Utils Functions */
vector<int> generate_permutation(const int N){
    vector<int> permutation(N);
    for (int i = 0; i < N; i++)
        permutation[i] = i;

    shuffle(permutation.begin(), permutation.end(), RNG);

    return permutation;
}

string generate_random_string(int len){
    static const string alphanum =
    "0123456789"
    "!@#$%^&*"
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "abcdefghijklmnopqrstuvwxyz";
    static uniform_int_distribution<> distribution(0, int(alphanum.size()-1));
    string random_string = "";
    while (len--) random_string += alphanum[distribution(RNG)];
    
    return random_string;
}

vector<string> generate_random_strings(int num, pair<int, int> len_range){
    vector<string> random_strings;
    static uniform_int_distribution<> distribution(len_range.first, len_range.second);
    while (num--){
        int len = distribution(RNG);
        random_strings.push_back(generate_random_string(len));
    }
    return random_strings;
}

vector<const char*> strings_to_cstrings(const vector<string>& strings){
    vector<const char*> cstrings;
    for(const string& s:strings) cstrings.push_back(s.c_str());
    return cstrings;
}

template<typename T>
void print(T arr, string title=""){
    if (title != "") cout<<title<<endl;
    for(auto v: arr) cout<<v<<'\t';
    cout<<endl;
}


/* Testing Functions */

double execute_and_log(function<void()> func){
    chrono::time_point<std::chrono::system_clock> start, end;
    start = chrono::system_clock::now();
    func();
    end =chrono::system_clock::now();
    chrono::duration<double> elapsed_seconds = end - start;
    cout << "---- Elapsed time: " << elapsed_seconds.count() << "s\n";
    
    return elapsed_seconds.count();
}

void test_function(vector<function<void()> > funcs, string test_what){
    cout << "Start testing " + test_what + ":" << endl;
    double elapsed_seconds = 0;
    for(auto func: funcs){
        elapsed_seconds += execute_and_log(func);
    }
    cout << "---- Mean time: " << elapsed_seconds/double(funcs.size()) << endl << endl;
}

/* Comparison Functions taking void pointers as arguments*/
template<typename T>
int pless(const void * a, const void * b){return (*(T*)a<*(T*)b)?-1:1;};

template<typename T>
int pgreater(const void * a, const void * b){return (*(T*)a<*(T*)b)?1:-1;};

template<typename Value_type, typename Cmp_type>
function<void()> pack_qsort(vector<Value_type>& arr, Cmp_type cmp){
    return bind(qsort, arr.data(), arr.size(), sizeof(Value_type), cmp);
}

template<typename Arr_type, typename Cmp_type>
void test_qsort_once(Arr_type& arr, Cmp_type cmp_pair, string content, bool debug=false){
    Arr_type arr_dup(arr);
    /* Actual Sorting Functions */
    auto qsort_asc = pack_qsort(arr, cmp_pair.first);
    auto qsort_desc = pack_qsort(arr_dup, cmp_pair.second);
    
    /* Testing */
    if(debug) print(arr, "------Original-----");
    string title = "qsort "+to_string(arr.size())+" "+content;
    test_function({qsort_asc, qsort_desc}, title);
    if(debug) print(arr);
    if(debug) print(arr_dup);
    cout<<endl;
}

void test_qsorts(vector<int> int_arr, vector<string> str_arr, vector<const char*> cstr_arr, bool debug=false){
    /* wrap strcmp */
    auto lstrcmp = [](const void * a, const void * b){return strcmp(*(char**)a, *(char**)b);};
    auto lstrcmp_rev = [](const void * a, const void * b){return strcmp(*(char**)b, *(char**)a);};
    
    /* Testing*/
    test_qsort_once(int_arr, make_pair(pless<int>, pgreater<int>), "Integers", debug);
    test_qsort_once(str_arr, make_pair(pless<string>, pgreater<string>), "Strings", debug);
    test_qsort_once(cstr_arr, make_pair(lstrcmp, lstrcmp_rev), "CStrings", debug);

}

template<typename Arr_type, typename Cmp_type>
void test_sort_once(Arr_type& arr, Cmp_type cmp_pair, string content, bool debug=false){
    Arr_type arr_dup(arr);
    /* Actual Sorting Functions */
    auto sort_asc = [&](){sort(arr.begin(), arr.end(), cmp_pair.first);};
    auto sort_desc = [&](){sort(arr_dup.begin(), arr_dup.end(), cmp_pair.second);};

    /* Testing */
    if(debug) print(arr, "------Original-----");
    string title = "sort "+to_string(arr.size())+" "+content;
    test_function({sort_asc, sort_desc}, title);
    if(debug) print(arr);
    if(debug) print(arr_dup);
    cout<<endl;
}

void test_sorts(vector<int> int_arr, vector<string> str_arr, vector<const char*> cstr_arr, bool debug=false){
    /* wrap strcmp */
    auto sstrcmp = [](const char *a, const char *b){return strcmp(a, b)<0;};
    auto sstrcmp_rev = [](const char *a, const char *b){return strcmp(a, b)>0;};
    
    /* Testing */
    test_sort_once(int_arr, make_pair(less<int>(), greater<int>()), "Integers", debug);
    test_sort_once(str_arr, make_pair(less<string>(), greater<string>()), "Strings", debug);
    test_sort_once(cstr_arr, make_pair(sstrcmp, sstrcmp_rev), "CStrings", debug);

}

int main(int argc, const char * argv[]) {
    vector<int> int_arr = generate_permutation(N);
    vector<string> str_arr = generate_random_strings(N, {8, 31});
    vector<const char*> cstr_arr = strings_to_cstrings(str_arr);

    test_qsorts(int_arr, str_arr, cstr_arr, false);
    test_sorts(int_arr, str_arr, cstr_arr, false);
}
