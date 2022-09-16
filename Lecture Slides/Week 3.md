# Week 3 : Searching and Sorting Algorithms

## Lecture-1 : Range Function in Python

```abc
range(j)
Output : 0, 1, 2, .... j-1
range(i, j)
Output : i, i+1, i+2,....j-1
range(i, j, k)
Output : i, i+k, i+2k, ....i+nk where i+nk < j < i+(n+1)k
range(i, j, -1)
Output : i, i-1,....j+1 where i > j


```

* General Rules of range()
* ```
  for num in range(i, j, k):
     if k > 0 and i >= j Then
         increasing
     elif k < 0 and i <= j Then
         decreasing

  ```

Why does `range(i,j)` stop at `j-1` ?

Mainly to make it easier to process lists

List of length n has positions `0,1,..,n-1`

`range(0,len(l))` produces correct range of valid indices Easier than writing `range(0,len(l)-1)`

Compare the following 

`for i in [0,1,2,3,4,5,6,7,8,9]:`

`for i in range(0,10):`

Is `range(0,10) == [0,1,2,3,4,5,6,7,8,9]` ?

In Python2, yes

In Python3, no!
