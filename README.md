# Funktools

This repository holds the code for `Funktools` that implements the `fold` function.

## Description

`fold` is a higher order function that takes
* a sequence of type A
* a "starting" value of type B
* a function (A, B) -> B

and returns a B. E.g., the `sum` of an array is a special case of fold, where
* the sequence is an array of numbers
* the starting value is 0
* the function is `+`


You can find more information on [Wikipedia](https://en.wikipedia.org/wiki/Fold_(higher-order_function)).


## Approach

- Implement barebones fold to replicate `reduce` function from `functools`
- Add test-cases to verify parity with `reduce`
- If time permits, add fold-right & fold-left operations.

## Scope

- No parallelism. Accumulator functions that are associative could be parallelized, but it is beyond the scope.
