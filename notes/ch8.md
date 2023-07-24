# Shortest Paths

**We want to find the directed path P which starts and at s and ends at t such that the overall weight of the path is as low as it can be!**

Mathematically this means we want to minimize $w(P)$, where:

$$w(P) := \Sigma_{u \rarr v \in P}$$

This directed path scenario has many real world use cases that all generically ask:

- ***"what is the fastest way to get from point A to point B"*?**

## Shortest Path Trees

Almost every algorithm that computes the shortest path from A to B actually computes much more than that!

These shortest path algorithms form trees which answer a more broader question:

- **Find the shortest paths to each vertex from a particular source vertex.**

This problem is often dubbed the *single source shortest path or SSSP problem*!

We can solve the problem by computing a tree rooted at the source vertex. This tree contains all of the shortest paths (as a result it is also a spanning tree since it hits every possible vertex reachable from s).

- If each shortest path is unique, then their combined graph forms a tree! 

How can we be so sure?:

- Well by definition the goal is to find the shortest path to each vertex, so that means that each path will hit its target vertex once.

- Furthermore, if a shortest path from s to B goes through some other vertex, A, then the shortest path from s to A is actually a subpath of another shortest path!

- **If for some reason there isn't a unique shortest path, we can always choose one in particular such that the union of paths still forms a tree.**

- Suppose two shortest paths both originating at s: $s \rarr u$ and $s \rarr v$. If these paths diverge and then meet and then diverge again, we can change a path (without affecting the path length) so that the divergence occurs only once.

*Shortest path trees are similar to MSTs because they are both optimal spanning trees.*

However there are some key differences between the two:

    - MSTs are unrooted and undirected whereas SPTs are naturally defined for directed graphs. 

    - For any particular graph there is only one MST. With SPTs the tree varies depending on the chosen source vertex.

    - For certain graphs it is possible for every SPT to use a different set of edges than the MST.

---

## Negative Edges

- Negative edges often hinder many shortest path problem solutions because:

***A negative cycle might imply that the shortest path problems may not be well defined.***

A shortest path from a to b exists iff there is at least one path from a to b, but no path from a to b that touches a vertex in a negative cycle.

What happens if the path does touch a negative cycle?

Textbook example:

![Negative Cycle Textbook Example 1](./../images/Negative_Cycle_Textbook_Example_1.PNG)

If we go through the -8 once we get a path length of: 5 + 2 + -8 + 3 = 2

Now lets check that the cycle is overall negatively weighted:

The edges in the cycle add up to a total weight of: 2 + 4 + 1 + -8 = -1!

Now what this means is that *if we step through the cycle once, then our path length is small*,
*if we step through it twice before reaching the destination then our path length is even smaller*.
**We can step through the cycle indefinitely to continue decreasing our path length!**

- **Therefore our SSSP problem has no real solution because the minimum weighted path can never really be attained (there is no minimum if we can keep getting smaller infinitely)!**

*Can we solve this? YES with a much more complicated algorithm!*

*Are we going to cover such an algorithm: **NO, thank god.***

**We still need to consider negative edge weights but we will be operating under the assumption that these algorithms are being applied to graphs that do not contain negative cycles.**

**The graphs covered in this chapter are explicitly directed and weighted, but the algorithms we will discuss will work with undirected graphs as well as long as we apply minor and straightforward changes.**

A note: We should really be saying shortest *walk* as opposed to shortest path if we want to technically accurate.

---

## The Only SSSP Algorithm

Just like graph traversals and MSTs, the SSSP problem has a generic solution that applies to every concrete algorithm made to solve it!

This generic algorithm is also known as Ford's algorithm

The algorithm has one goal which won't make sense for now:
**Repeatedly relax tense edges until no tense edges exist! (massage the damn graph!?)**

Each vertex is given 2 properties (alternatively we can implement two arrays to store the properties for each vertex).

- **dist(v)**: This property stores the length of the shortest path we know of (currently). The value of this property changes until it eventually becomes the shortest path from some source vertex, s, to v. 

- **pred(v)**: This property stores the direct predeccesor of v based on the current minimum weighted path from some source vertex, s, to v.

Note: In my code I use arrays instead of properties, and instead of dist I called the property path (different teminology, and slightly different implementation but my code accomplishes the same thing as the pseudocode you will see).

- Similar to the parent pointers of any other tree, the pred pointers here define a changing tree that is rooted at s (s has no predecessor, it is the root).

Therefore to initialize this tree as being simple s, the source vertex, we utilize the following pseudocode:

    InitSSSP(s):
        
        dist(s) = 0
        pred(s) = null

        for all vertices, v, except s:
            dist(v) = infinity
            pred(v) = null

Each edge of the tree can be defined as *tense* or *relaxed*.

**An edge is considered tense if $dist(u) + weight(u \rarr v) < dist(v)$**

**This would imply that dist v is not the shortest value it can be, because a path from the source to u and then through to v is shorter than whatever is currently considered to be the shortest path from the source to v!**

- To fix this we simply change dist(v) to equal the smaller path's length: $dist(v) = dist(u) + weight(u \rarr v)$
- We should also update the predecessor of v to now be u, since the new shortest path goes from the source to u and then directly to v!: $pred(v) = u$

The principle of a tense edge is crucial to understanding all shortest path algorithms!

The process described in the two steps above (the bullet points) is called "relaxing" a tense
edge.

If an edge is not tense then it is relaxed!

Pseudocode:

    Relax(u, v):
        dist(v) = dist(u) + weight(u, v)
        pred(v) = u
    

With all of that in mind the pseudocode for Ford's algorithm is extremely intuitive:

    FordSSSP(s):
        InitSSSP(s)
        while there is a tense edge:
            relax ANY tense edge 
            # How we find and the order in which we pick tense edges is where our specialized algorithms differ from one another.

---

## Unweighted Graphs: Breadth-First Search



---