#include <iostream>
#include <cstdlib>
#include <concepts>
#include <ranges>
#include <vector>
using namespace std;

/* Concept Part */
// Basic Concep

template <class T>
concept Crementable = 
    requires(T x) {
    { x++ } -> std::convertible_to<T>;
    { ++x } -> std::same_as< std::add_lvalue_reference_t<std::remove_reference_t<T> > >;
    { x-- } -> std::convertible_to<T>;
    { --x } -> std::same_as< std::add_lvalue_reference_t<std::remove_reference_t<T> > >;
};


template <class Iterator>
concept RandomAccessIterator = Crementable<Iterator> && 
    requires(Iterator it, const int diff, const int idx){
        { it + diff } -> same_as< Iterator >;
        { diff + it } -> same_as< Iterator >;
        { it - diff } -> same_as< Iterator >;
        { it += diff } -> same_as< add_lvalue_reference_t<remove_reference_t<Iterator> > >;
        { it -= diff } -> same_as< add_lvalue_reference_t<remove_reference_t<Iterator> > >;
        { it[idx] } -> convertible_to<decltype(*(it+idx))>;
    };

// Function Concept
template <class Iterator, class Value>
concept Findable = Crementable<Iterator> && equality_comparable<Value> && equality_comparable<Iterator> && requires(Iterator it, Value v){
    { *it } -> same_as< add_lvalue_reference_t<remove_reference_t<Value> > >;
};

template <class Iterator, class UnaryPredicate>
concept Findifable = Crementable<Iterator> && equality_comparable<Iterator> && predicate<UnaryPredicate, typename Iterator::value_type>;

template <class Iterator, class Comp>
concept Sortable = RandomAccessIterator<Iterator> && totally_ordered<typename Iterator::value_type> && predicate<Comp, typename Iterator::value_type, typename Iterator::value_type>;



/* Function Part */
// def find
template<class InputIt, class Value>
constexpr InputIt my_find(InputIt first, InputIt last, const Value& value)
    requires Findable<InputIt, Value>
{
    for (; first != last; ++first) {
        if (*first == value) {
            return first;
        }
    }
    return last;
}

template<class Container, class Value>
constexpr typename Container::iterator my_find(Container& container, const Value& value)
    requires Findable<typename Container::iterator, Value> && ranges::range<Container>
{
    typename Container::iterator first = container.begin(), last = container.end();
    for (; first != last; ++first) {
        if (*first == value) {
            return first;
        }
    }
    return last;
}

// def find_if
template<class InputIterator, class UnaryPredicate>
InputIterator my_find_if (InputIterator first, InputIterator last, UnaryPredicate pred)
    requires Findifable<InputIterator, UnaryPredicate>
{
    while (first!=last) {
        if (pred(*first)) return first;
        ++first;
    }
    return last;
}


template<class Container, class UnaryPredicate>
typename Container::iterator my_find_if (Container& container, UnaryPredicate pred)
    requires Findifable<typename Container::iterator, UnaryPredicate> && ranges::range<Container>
{
    typename Container::iterator first = container.begin(), last = container.end();
    while (first!=last) {
        if (pred(*first)) return first;
        ++first;
    }
    return last;
}

// def sort
template <class Iterator, class Comp=decltype(less<typename Iterator::value_type>())>
void my_sort (Iterator first, Iterator last, Comp cmp=less<typename Iterator::value_type>())
    requires Sortable<Iterator, Comp>
{
    sort(first, last, cmp);
}

template <class Container, class Comp=decltype(less<typename Container::value_type>())>
void my_sort (Container& container, Comp cmp=less<typename Container::value_type>())
    requires Sortable<typename Container::iterator, Comp> && ranges::range<Container>
{
    sort(container.begin(), container.end(), cmp);
}

/* test code */
void print(const vector<int>& v){
    for_each(v.begin(), v.end(), [](int i){cout<<i<<' ';});
    cout<<endl;
}
void test_my_sort(){
    vector<int> v = {3,2,4};
    my_sort(v.begin(), v.end()); //sort
    print(v);
    my_sort(v, greater<int>()); //reverse
    print(v);
    my_sort(v); //sort again
    print(v);
    my_sort(v.begin(), v.end(), greater<int>()); //reverse again
    print(v);
    
}

void test_my_find(){
    vector<int> v = {3,2,4};
    auto it = my_find(v.begin(), v.end(), 4);
    cout<< *it <<endl;
    it = my_find(v, 2);
    cout<< *it <<endl;
    /* Complier error, concept not satisfied */
    // Exp 1
    //int fake_it = 3;
    //auto it = myfind(fake_it, fake_it, 2);
    
    // Exp 2
    //vector<char> c = {'2','3','4'};
    //auto it = myfind(c.begin(), c.end(), 2);
}

void test_my_find_if(){
    vector<int> v = {3,2,4};
    auto it = my_find_if(v.begin(), v.end(), [](int i){return i==2;});
    cout<< *it <<endl;
    it = my_find_if(v, [](int i){return i>3;});
    cout<< *it <<endl;
    
    /* Complier error, concept not satisfied */
    // Exp 1
    //int fake_it = 3;
    //auto it = myfind(fake_it, fake_it, 2);
    
    // Exp 2
    //vector<char> c = {'2','3','4'};
    //auto it = myfind(c.begin(), c.end(), 2);
    
}

int main()
{
    //test_my_find();
    //test_my_find_if();
    test_my_sort();
}


