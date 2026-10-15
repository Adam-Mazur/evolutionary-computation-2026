# Assignment 1: Greedy heuristics

Team:

- Adam Mazur 160297
- Jakub Jęsiek 160312

## Problem description

We are given three columns of integers with a row for each node. The first two columns contain x and y coordinates of the node positions in a plane. The third column contains node costs. The goal is to select exactly 50% of the nodes (if the number of nodes is odd we round the number of nodes to be selected up) and form a Hamiltonian cycle (closed path) through this set of nodes such that the sum of the total length of the path plus the total cost of the selected nodes is minimized.

## Implemented algorithms

### Random solution

We pick half of the nodes at random and put them in a random order.

```
RandomSolution(n):
    k = n / 2
    pick k different nodes at random
    return them in random order
```

### Nearest neighbor (add only at the end)

We start from one node. In each step we look at the last node of the path. We add the node that gives the smallest distance from the last node plus its cost.

```
NearestNeighborEnd(start):
    path = [start]
    while path has less than k nodes:
        last = last node of path
        for each node j not in path:
            score(j) = dist(last, j) + cost(j)
        add the node with the smallest score at the end of path
    return path
```

### Nearest neighbor (add at any position)

We start from one node. In each step we try every node that is not in the path yet and every place where we could put it: at the beginning, at the end, or between two nodes in the path. We pick the node and the place that increase the objective the least.

```
NearestNeighborAny(start):
    path = [start]
    while path has less than k nodes:
        for each node j not in path:
            for each position i in path (from 0 to length of path):
                if i is the beginning:
                    delta = dist(j, first) + cost(j)
                if i is the end:
                    delta = dist(last, j) + cost(j)
                if i is between nodes a and b:
                    delta = dist(a, j) + dist(j, b) - dist(a, b) + cost(j)
        insert the node with the smallest delta at its best position
    return path
```

In both nearest neighbor methods we build an open path. At the end we close it into a cycle by connecting the last node with the first one.

### Greedy cycle

We start from one node and add the node that increases the objective the least. With only two nodes the cycle goes to the second node and back, so the edge is counted twice. Then in each step we try every node that is not in the cycle yet and every edge of the cycle where we could put it. We pick the node and the edge that increase the objective the least. Unlike the nearest neighbor methods, we always work on a closed cycle, so there is no beginning or end.

```
GreedyCycle(start):
    for each node j other than start:
        score(j) = 2 * dist(start, j) + cost(j)
    cycle = [start, node with the smallest score]
    while cycle has less than k nodes:
        for each node j not in cycle:
            for each edge (a, b) in cycle (including the edge from last to first):
                delta = dist(a, j) + dist(j, b) - dist(a, b) + cost(j)
        insert the node with the smallest delta into its best edge
    return cycle
```

## Results

We ran each method 200 times on each instance. The table shows the objective function value (cycle length plus node costs).

| Method | TSPA min | TSPA max | TSPA mean | TSPB min | TSPB max | TSPB mean |
|---|---|---|---|---|---|---|
| Random | 241035 | 287165 | 261226.03 | 183160 | 229951 | 206128.23 |
| NN (end only) | 84362 | 90075 | 87476.03 | 56007 | 63166 | 59553.28 |
| NN (any position) | 72328 | 77022 | 74293.92 | 52915 | 66164 | 59274.41 |
| Greedy cycle | 72590 | 75132 | 73777.69 | 55655 | 63736 | 60221.98 |

## Visualization

The plots show the best solution for each method and instance. Gray dots are nodes that were not picked. Picked nodes are colored by their cost, and bigger dots mean higher cost.

![Best solutions](solutions.png)

## Best solutions

### Random

TSPA (241035):

171, 4, 77, 100, 94, 142, 1, 96, 166, 66, 146, 144, 90, 86, 182, 137, 11, 39, 187, 152, 69, 191, 160, 194, 134, 57, 3, 85, 2, 148, 131, 179, 47, 26, 106, 189, 21, 19, 35, 113, 36, 193, 61, 174, 183, 169, 158, 180, 49, 5, 150, 177, 27, 7, 80, 48, 149, 23, 9, 176, 143, 99, 192, 190, 185, 74, 126, 188, 153, 147, 34, 124, 43, 107, 155, 162, 120, 109, 93, 33, 163, 127, 167, 13, 197, 119, 83, 67, 44, 20, 88, 116, 159, 91, 22, 102, 87, 63, 104, 62

TSPB (183160):

186, 43, 124, 167, 182, 129, 139, 193, 171, 55, 184, 159, 130, 47, 172, 85, 174, 126, 74, 195, 160, 183, 71, 16, 120, 185, 18, 64, 40, 45, 56, 148, 32, 49, 194, 78, 104, 137, 90, 156, 142, 60, 53, 191, 27, 97, 86, 82, 54, 10, 141, 188, 75, 61, 1, 136, 143, 70, 44, 67, 123, 77, 165, 146, 22, 107, 19, 157, 5, 176, 197, 190, 152, 154, 98, 198, 7, 134, 73, 34, 28, 178, 102, 51, 26, 132, 140, 155, 52, 128, 6, 14, 114, 101, 199, 89, 149, 125, 133, 72

### NN (end only)

TSPA (84362):

54, 9, 33, 36, 177, 67, 144, 53, 135, 58, 134, 176, 174, 106, 89, 107, 57, 182, 151, 93, 50, 3, 1, 164, 178, 29, 136, 186, 184, 47, 159, 130, 153, 78, 88, 193, 170, 146, 75, 64, 150, 42, 113, 43, 85, 142, 8, 131, 84, 158, 192, 181, 114, 141, 180, 132, 76, 80, 48, 31, 63, 149, 168, 97, 127, 187, 30, 123, 152, 108, 60, 116, 49, 11, 119, 160, 83, 90, 51, 16, 35, 87, 45, 140, 52, 179, 185, 28, 102, 156, 157, 71, 91, 38, 100, 4, 112, 139, 115, 5

TSPB (56007):

43, 89, 57, 76, 54, 127, 129, 90, 153, 20, 14, 2, 110, 118, 56, 114, 196, 10, 148, 143, 78, 192, 162, 104, 185, 184, 3, 151, 69, 172, 133, 120, 96, 121, 198, 48, 72, 46, 86, 117, 160, 136, 8, 21, 154, 140, 47, 170, 125, 177, 6, 132, 29, 197, 175, 134, 45, 60, 40, 71, 155, 97, 115, 180, 65, 28, 149, 145, 158, 116, 147, 42, 50, 130, 30, 183, 38, 64, 85, 59, 167, 51, 87, 179, 82, 88, 171, 99, 67, 24, 34, 181, 152, 73, 98, 27, 135, 75, 79, 156

### NN (any position)

TSPA (72328):

104, 129, 69, 127, 97, 168, 116, 149, 63, 11, 49, 160, 83, 123, 100, 152, 108, 60, 31, 48, 80, 91, 157, 71, 4, 76, 132, 180, 28, 102, 185, 35, 156, 51, 16, 67, 144, 140, 53, 179, 52, 177, 36, 33, 9, 54, 131, 174, 8, 164, 186, 136, 163, 29, 101, 178, 1, 169, 3, 50, 147, 47, 93, 106, 42, 89, 113, 130, 159, 146, 170, 153, 193, 78, 88, 107, 64, 57, 182, 151, 150, 176, 72, 134, 84, 58, 158, 192, 181, 114, 135, 73, 45, 87, 141, 187, 30, 189, 2, 171

TSPB (52915):

110, 2, 14, 20, 74, 153, 182, 52, 90, 129, 127, 80, 54, 192, 162, 104, 76, 185, 57, 89, 86, 46, 72, 3, 184, 173, 151, 122, 117, 8, 160, 69, 172, 136, 133, 120, 156, 43, 48, 96, 198, 121, 130, 191, 50, 42, 147, 116, 37, 146, 13, 149, 28, 145, 65, 158, 177, 125, 26, 170, 197, 36, 132, 29, 6, 180, 115, 155, 71, 175, 134, 45, 157, 60, 40, 141, 97, 154, 140, 47, 38, 21, 176, 30, 183, 189, 168, 64, 59, 85, 51, 73, 167, 152, 34, 24, 181, 179, 87, 82

### Greedy cycle

TSPA (72590):

116, 149, 168, 63, 11, 49, 60, 108, 152, 100, 90, 123, 83, 160, 97, 127, 69, 171, 2, 189, 30, 187, 141, 87, 45, 73, 135, 114, 181, 192, 158, 58, 84, 134, 72, 176, 150, 151, 182, 57, 64, 107, 88, 78, 193, 153, 170, 146, 159, 130, 113, 89, 42, 106, 93, 47, 147, 50, 3, 169, 1, 178, 101, 29, 163, 136, 186, 164, 142, 8, 174, 131, 54, 9, 33, 36, 177, 52, 179, 53, 140, 144, 67, 16, 51, 156, 35, 185, 102, 28, 180, 132, 76, 4, 71, 157, 91, 80, 48, 31

TSPB (55655):

36, 197, 6, 180, 115, 170, 97, 140, 47, 155, 71, 175, 134, 45, 157, 60, 141, 40, 33, 64, 21, 189, 168, 69, 160, 172, 136, 133, 120, 8, 117, 72, 46, 86, 184, 3, 173, 122, 151, 98, 111, 27, 135, 76, 185, 162, 192, 80, 52, 182, 20, 74, 2, 93, 110, 118, 14, 153, 90, 129, 127, 54, 104, 57, 89, 156, 43, 48, 96, 198, 121, 63, 130, 191, 183, 30, 176, 38, 154, 26, 125, 177, 138, 158, 145, 149, 147, 42, 116, 37, 146, 13, 28, 65, 178, 103, 29, 132, 1, 174

## Solution checker

All best solutions were checked with the solution checker.

## Source code

https://github.com/Adam-Mazur/evolutionary-computation-2026

## Conclusions

- All greedy methods are about 3 times better than random.
- NN with any position gave the best single solutions on both instances. It can put a node in the middle of the path, so it avoids the long jumps that NN with end only has to make.
- Greedy cycle has the best mean and the smallest spread on TSPA, but on TSPB its mean is the worst of the greedy methods.
- On TSPB the two NN methods have almost the same mean, so the gain there is smaller.
