# Sorting

> - Name: Zejun Lin
> - UNI: zl2844

## What does the code do

- Measure the time needed to sort 1,000,000 random integers using sort and qsort(); once in increasing and once in decreasing order.
- Measure the time needed to sort 1,000,000 random strings using sort() and qsort(); once in increasing and once in decreasing order; once for short strings (less than 8 characters) and once for longer strings (between 8 and 32 characters).

- Set `debug` to `True` and `N` to `10` to verify by a small example (e.g., 10 ints) that the sorts actually do what they are supposed to do.
- Beware: `qsort` uses simple copies and not all implementations of `std::string` can be copied just by copying the bits.

## Thoughts & Performance Results

### Results

- With -O2 option

<table style="border-collapse:collapse;border-spacing:0" class="tg"><tr><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top"></th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top"></th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">Integers</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">Strings(1-7)</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">C-style Strings (1-7)</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">Strings(8-32)</th><th style="font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">C-style Strings (8-32)</th></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top" rowspan="3">qsort</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">ACS</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.147841s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.423887s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.315252s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.521493s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.619003s</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">DECS</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.14524s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.397117s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.336815s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.617757s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.476s</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">Mean</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-decoration:underline;text-align:left;vertical-align:top">0.146541s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-decoration:underline;text-align:left;vertical-align:top">0.410502s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-decoration:underline;text-align:left;vertical-align:top">0.326033s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-decoration:underline;text-align:left;vertical-align:top">0.569625s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-decoration:underline;text-align:left;vertical-align:top">0.547501</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top" rowspan="3">sort</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">ACS</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.066516s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.219531s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.279227s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.459843s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.424813s</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">DECS</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.07576s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.228513s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.282523s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.453608s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">0.401639s</td></tr><tr><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;text-align:left;vertical-align:top">Mean</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;font-weight:bold;text-decoration:underline;text-align:left;vertical-align:top">0.071138s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;font-weight:bold;text-decoration:underline;text-align:left;vertical-align:top">0.224022s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;font-weight:bold;text-decoration:underline;text-align:left;vertical-align:top">0.280875s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;font-weight:bold;text-decoration:underline;text-align:left;vertical-align:top">0.456726s</td><td style="font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:inherit;font-weight:bold;text-decoration:underline;text-align:left;vertical-align:top">0.413226s</td></tr></table>

### Analysis

- For all kinds of data types, `sort` is much faster than `qsort`
- Among all data types, they have the biggest speed difference in integer types (almost 2 times faster), then short strings, and the smallest speed difference is in long strings.
  - I think this phenomenon occurs because with the size of data type grows, more time is needed to make a simple comparison between two elements (O(n) for a string of length n). So even though in terms of the sorting alrightm, `sort` is faster than `qsort`, the difference between their speeds is decreasing.
- `sort` does better with`string` than `c-style string` when strings are short, but the situation is reversed when the strings become longer. While `qsort` is always good at dealing with `c-style string` than `string`, which is not surprising.

## Experience with writing the code

I hope I may get some insights...

### Template

To maximize code reuse, I seperate abstract level and extract common functions. But there's something really annoying about template.

1. You cannot pass lambdas as function arugment with the same template type, even though they have the same signature.

- ```c++
  template<typename T>
  void foo(T a, T b){}
  
  auto lambda1 = [](int a, int b){return a-b;};
  auto lambda2 = [](int a, int b){return b-a;};
  
  foo(lambda1, lambda2) // Error cuz not the same type (T)
  // I really do not want to have two typename for two lambdas because there are also other template argument in foo, which makes it even more ugly.
  ```

- Also, things became weird when you try to return a lambda with template, and wanna make a template lambda...

2. cannot `bind` a template function like `sort`: `bind(sort, vec.begin(), vec.end()) //Error`



Well, when the template things did not work and after I got tired of searching with google, I was like "**who cares! It is just my own code, I would use DEFINE with args instead!!!**" But finally I did figure out some ways. For example, the lambda one, I just instead use one argument `T tuple` and pass a `make_pair(lambda1, lambda2)` into it.

### Others

Mainly about all sorts of complex function. **I am really confused why things cannot be simpler, which from my perspective is feasible**.

1. Timing function

   - ```c++
     chrono::time_point<std::chrono::system_clock> start, end;
     start = chrono::system_clock::now();
     func();
     end =chrono::system_clock::now();
     chrono::duration<double> elapsed_seconds = end - start;
     cout << "---- Elapsed time: " << elapsed_seconds.count() << "s\n";
     ```

   - you see, many different long complex type here. Why is not there's a simple function call `time()` that gives you the time from 1971 as of `unsigned int` type just like python does? I think it's feasible.

2. Uniform distribution: in order to geneate a number with uniform distribution, you need to:

   - ```c++
     // Init a uniform dist
     const long long SEED = chrono::steady_clock::now().time_since_epoch().count();
     mt19937 RNG(SEED);
     uniform_int_distribution<> distribution(lower, higher);
     // Nest TWO FUNCTIONS to use it
     distribution(RNG);
     ```

   - Why there is no a function like that one in python giving you some like `number = randint(lower, higher)`? Well for this I guess maybe it costs to get init different `uniform_int_distribution`...

