//
//  main.cpp
//  cpppg
//
//  Created by zejunlin on 2/18/20.
//  Copyright © 2020 Danny. All rights reserved.
//

#include <chrono>
#include <iostream>
#include <list>
#include <set>
#include <string>
#include <random>
#include <vector>
using namespace std;

struct BigStructure{
    int val;
    int arr[1000] = {0};
    BigStructure(const int v):val(v){}
    BigStructure():val(0){}
    bool operator < (const BigStructure& o) const {return val < o.val;}
};
struct Int{
    int val;
    Int(const int v):val(v){}
    Int():val(0){}
    bool operator < (const Int& o) const {return val < o.val;}
};

template<typename ValueType>
vector<ValueType> generate_permutation(const int N, const long long seed){
    mt19937 rng(seed);
    vector<int> permutation(N);
    for (int i = 0; i < N; i++)
        permutation[i] = i;

    shuffle(permutation.begin(), permutation.end(), rng);
    vector<ValueType> real_permutation(N);
    for (int i=0; i < N; i++) real_permutation[i] = ValueType(permutation[i]);

    return real_permutation;
}

vector<int> generate_remove_indices(const int N, unsigned seed){
    mt19937 generator(seed);
    vector<int> remove_indices;

    for(int i=N-1; i>=0; --i){
        uniform_int_distribution<> distribution(0,i);
        remove_indices.push_back(distribution(generator));
    }
    return remove_indices;
}

template<typename C>
int _test(const int N, C& container, long long seed){
    
    auto permutation = generate_permutation<typename C::value_type>(N, seed);
    auto remove_indices = generate_remove_indices(N, seed);

    // Using time point and system_clock
    std::chrono::time_point<std::chrono::system_clock> start, end;
    start = std::chrono::system_clock::now();

    for(auto& item: permutation){
        auto it = container.begin();
        while (it != container.end() && (*it) < item) ++it;
        container.insert(it, item);
    }
    /* Debug purpose
    for_each(container.begin(), container.end(), [](auto i){cout<<i.val<<' ';});
    cout<<endl;
     */
    
    for(int idx_to_remove: remove_indices){
        auto it = container.begin();
        while(idx_to_remove--) ++it;
        container.erase(it);
    }
    // End counting time
    end = std::chrono::system_clock::now();
    std::chrono::duration<double> elapsed_seconds = end - start;
    
    cout << "Elapsed time: " << elapsed_seconds.count() << "s\n";
    
    return elapsed_seconds.count();
}

template<typename C>
void test_type(const int N, vector<long long> seeds, string type){
    int elapsed_seconds = 0;
    printf("Begin testing %s (N = %dk):\n", type.c_str(), int(N/1000));
    for(auto seed: seeds){
        C container;
        elapsed_seconds += _test(N, container, seed);
        container.clear();
    }
    cout << "Mean time for type " << type << ":\t" << 1.0*elapsed_seconds/seeds.size() << " s" << endl << endl;
}

int main(int argc, const char * argv[]) {
    long long seed = chrono::steady_clock::now().time_since_epoch().count();
    vector<long long> seeds = {seed, seed/2, seed/4};
    const int K = 1000;
    vector<int> magnitude = {5, 10, 20};
    for_each(magnitude.begin(), magnitude.end(), [&K](int& i){i*=K;});
    for(int N: magnitude){
//        test_type<vector<BigStructure> >(N, seeds, "vector");
//        test_type<list<BigStructure> >(N, seeds, "list");
//        test_type<set<BigStructure> >(N, seeds, "set");
        test_type<vector<Int> >(N, seeds, "vector");
        test_type<list<Int> >(N, seeds, "list");
        test_type<set<Int> >(N, seeds, "set");
        
    }
    
    return 0;
}
