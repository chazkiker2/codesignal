# Sprint 03 M.C.

---

## cs BST Range Sum

### U.P.E.R.

### BST Range Sum Implementation Challenges

I had initially approached this problem planning to use a DFT and thus implemented a solution for just that. (Should've
UPERed better.) After implementing that, I ran the tests and quickly realized that the DFT is not the way to go for such
a problem, I needed an in-order traversal of the tree.

After realizing that I needed an in-order traversal, the solution was rather quick. I decided to implement a very basic
recursive in_order_traversal as one might in printing a BST. Instead of printing, however, I actually append the node's
value to a List (nonlocal scope) and simply return the sum of that list!

It's likely not the MOST efficient solution, but it is clean and easy to read. It's a solution that makes sense in this
case (in my humble opinion).

I regret not UPERing harder, a lot of time could have been saved right there.

### BST Range Sum Complexity Defense

FIRST PASS:

The time complexity of my solution (worst case) I dare say might be O(n^2). Looking at my code right now, I'm actually
realizing I could've added `node.value` to a `sum_count` variable rather than `.append(node.value)`. In fact, I'll be
going back to refactor and resubmit my code. Other than that, I can't say there's much else to change. Could switch from
recursion to a while loop, might even do that in my second or third pass. But I must move on to the other problems now!

---

## Binary Tree Invert

### U.P.E.R.

### binary tree invert — summary & implementation challenges

My solution uses a recursive util called `invert` that inverts a given node in-place then calls itself passing in the
given node's children. Nothing need be returned, as (again) this function inverts in-place. I did not need much time on
this solution as I've solved it previously. Inverting trees is rather basic in my opinion; I was kind of stunned by how
simple it was in my first learning. Literally just swap right with left. Not all too hard.

Anyway, I encountered no obstacles this time around. The first time I solved it, I had instruction so no challenges
there either lol.

### binary tree invert complexity defense

The time complexity is `O(n)` because of the recursive loop. The space complexity is `O(h)` (where `h` is the height of
the tree). The recursive implementation will create a recursion call stack proportional to the height of the tree.

One alternative to my recursive solution, of course, would be an iterative solution. If we did that the time complexity
would remain `O(n)` and the space complexity would be `O(n)` where `n` is the total number of nodes. So recursive vs
iterative in this case each have their benefits depending on the tree coming in... but I'd venture to guess that the
recursive is actually better for the `O(h)` space complexity!

---

## Find All Paths

### U.P.E.R.

### implementation challenges

(Note: This solution I had already created previously.)

Man this problem gave me quite some trouble the other day. I spent a LONG time on it.

A summary of my solution:

- We've got ourselves a `GraphNode` class which defines the shape of a GraphNode
- we've got a `create_graph` util function that takes in an array representation of a graph and creates proper
  GraphNodes for each one (and eventually returns an array of proper GraphNodes).
- we've got a `csFindAllPathsFromAToB` function — the driver of the program that takes an array representation of a
  graph and returns an array of every possible path.
- And, finally, we've got a `traverse` function within `csFindAllPathsFromAToB`. This inner util is a recursive function
  that creates the paths themselves given a `GraphNode`.

Challenges in implementation:

- So many challenges, my oh my
- I have a file with about 4-5 different approaches to this problem. Only one of them works (though many of them are
  very close). I think in dictionaries and many of my attempts used "clever" dictionary manipulation to loop through and
  access the next possible node given the key. I finally got it working with a `.pop(0)` to remove the first element in
  the value of each dictionary entry, but then I would be missing 1 or 2 paths in my final returned array. Shit was
  infuriating. Eventually, I needed help and talked through a different approach with a peer. She got it working with
  that approach, and I decided to throw my dictionary attempts behind me and give her mental approach a shot. It didn't
  take long to get a first-pass solution with her mental framework that first-pass has been refactored into what I've
  submitted.

### complexity defense

I am absolutely, 100% certain that there is a smarter, faster, better way to do this. Whether that involves dictionaries
or not, I'm unsure. (Though I believe dicts are one possible approach to a very clean solution). I'd also argue that
there would be room for a clean DFS with some minor changes (maybe adding a color for nodes that don't have any children so
go back through the path til you're above one of those children and take the other child and finally color
fully-exhausted nodes some color?).

Regardless. The time complexity for my solution is a SWIFT `O(n^2)` (I think... it could be worse than that). I do
believe there exists a solution with worst-case`O(n)`.

Space complexity, lord knows... My guess would be something in the realm of `O(n)` but I couldn't be sure. I struggle
with Space Complexity when there are recursive calls inside loops and whatnot. 