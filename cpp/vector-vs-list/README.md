# vector-vs-list

 > Comparing performance of insertion and deletion between vector and list in C++ in different situations.

- Generate N random integers and insert them into a sequence so that each is inserted in its proper position in the numerical order. 5 1 4 2 gives:
  * 5
  * 1 5
  * 1 4 5
  * 1 2 4 5
- Remove elements one at a time by picking a random position in the sequence and removing the element there. Positions 1 2 0 0 gives
  * 1 2 4 5
  * 1 4 5
  * 1 4
  * 4

For which N is it better to use a linked list than a vector (or an array) to represent the sequence?

The sequence grows incrementally.

One might say that absolutely linked list is faster since insertion and deletion are all O(1). I would say that if it's in an interview.

## Experiment 1

### Setup:
  * I test std::list and std::vector with various numbers of elements (e.g., for 100K, 200K, … elements)
  * For complementary, I add std::set to see the effect of a O(log n) algorithm.
  * For fairness, I do not use any thing like `advance`, `lower_bound`, `find_if`, but just explicit `for` to do the job.
### Result:
#### Data
```
———
Begin testing vector (N = 50k):
Elapsed time: 12.3755s
Elapsed time: 12.8767s
Elapsed time: 14.0637s
Mean time for type vector:    12.6667 s

Begin testing list (N = 50k):
Elapsed time: 37.5031s
Elapsed time: 42.8347s
Elapsed time: 36.9231s
Mean time for type list:    38.3333 s

Begin testing set (N = 50k):
Elapsed time: 56.9607s
Elapsed time: 49.2562s
Elapsed time: 52.5954s
Mean time for type set:    52.3333 s
———
Begin testing vector (N = 100k):
Elapsed time: 49.9614s
Elapsed time: 50.7069s
Elapsed time: 49.2089s
Mean time for type vector:    49.3333 s

Begin testing list (N = 100k):
Elapsed time: 163.363s
Elapsed time: 180.219s
Elapsed time: 177.682s
Mean time for type list:    173.333 s

Begin testing set (N = 100k):
Elapsed time: 236.857s
Elapsed time: 245.695s
Elapsed time: 218.069s
Mean time for type set:    233 s
———
Begin testing vector (N = 200k):
Elapsed time: 208.625s
Elapsed time: 201.431s
Elapsed time: 196.78s
Mean time for type vector:    201.667 s

Begin testing list (N = 200k):
Elapsed time: 855.533s
Elapsed time: 849.724s
Elapsed time: 827.668s
Mean time for type list:    843.667 s

Begin testing set (N = 200k):
Elapsed time: 1062.4s
Elapsed time: 1047.7s
Elapsed time: 1053.28s
Mean time for type list:    1054.46 s
```

### Plot
![image](https://user-images.githubusercontent.com/20517842/75392941-0d179780-58bb-11ea-8f95-07cdbcb2845f.png)

### Thinking

For this experiment:
- I think that list is slower because every element in a linked-list takes 12 bytes (assuming on a 32-bit machine, so there's 4 bytes for an int, 2 4-byte pointer), while a new element in a vector only cost 4 bytes.
- This means that the allocation of a new element in a vector is 3 times (maybe) faster than that in a list (also thinking that the size is so large).
- This is true for a set too (which is a BST in C++ which means it needs more overhead for a single element.)


## Experiment 2

So I do another experiment where element where value type is much larger structure (has an array of thousands of integers). And the situation is completely different.

### Data

```
Begin testing vector (N = 5k):
Elapsed time: 3.81323s
Elapsed time: 3.51637s
Elapsed time: 3.26446s
Mean time for type vector:    3 s

Begin testing list (N = 5k):
Elapsed time: 0.672911s
Elapsed time: 0.556644s
Elapsed time: 0.68999s
Mean time for type list:    0 s

Begin testing set (N = 5k):
Elapsed time: 0.84846s
Elapsed time: 0.80943s
Elapsed time: 0.675822s
Mean time for type set:    0 s

Begin testing vector (N = 10k):
Elapsed time: 16.8489s
Elapsed time: 17.0209s
Elapsed time: 16.6364s
Mean time for type vector:    16.3333 s

Begin testing list (N = 10k):
Elapsed time: 3.18084s
Elapsed time: 4.96234s
Elapsed time: 4.55936s
Mean time for type list:    3.66667 s

Begin testing set (N = 10k):
Elapsed time: 4.66955s
Elapsed time: 5.38687s
Elapsed time: 4.98485s
Mean time for type set:    4.33333 s

Begin testing vector (N = 20k):
Elapsed time: 78.7979s
Elapsed time: 79.6892s
Elapsed time: 76.6594s
Mean time for type vector:    77.6667 s

Begin testing list (N = 20k):
Elapsed time: 20.9402s
Elapsed time: 23.128s
Elapsed time: 22.8777s
Mean time for type list:    21.6667 s

Begin testing set (N = 20k):
Elapsed time: 25.1323s
Elapsed time: 25.4292s
Elapsed time: 25.9977s
Mean time for type set:    25 s
```

### Plot
![image](https://user-images.githubusercontent.com/20517842/75393197-844d2b80-58bb-11ea-9d49-8a008a9d7616.png)


Actually this is an assignment give by Bjarne Stroustrup. For more information, refer to his [post](http://www.stroustrup.com/Software-for-infrastructure.pdf)
