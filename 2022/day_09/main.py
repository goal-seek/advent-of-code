"""
--- Part One ---
--- Day 9: Rope Bridge ---
This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far
below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics;
maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far
enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a
two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can
determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always
be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...
If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that
direction so it remains close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...
Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step
diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....
You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail
both start at the same position, overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step,
and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer
adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

== Initial State ==

......
......
......
......
H.....  (H covers T, s)

#### deleted ####
......
......
.TH...
......
s.....
After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s
again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..
So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?

"""

import numpy as np

file_name = "input.txt"

instructions = []

with open(file_name) as file:
    for line in file:
        direction = line.split(' ')[0]
        distance = int(line.split(' ')[1].replace('\n', ''))
        instructions = instructions + [direction] * distance

#print(instructions)

directions = {'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0]}

initial_head_pos = [0, 0]
initial_tail_pos = [0, 0]
head_log = [initial_head_pos]
tail_log = [initial_tail_pos]


def move_head(head_xy, dir):
    head_xy[0] = int(head_xy[0] + directions[dir][0])
    head_xy[1] = int(head_xy[1] + directions[dir][1])
    return head_xy


def move_tail(head_xy, tail_xy):
    dx, dy = head_xy[0] - tail_xy[0], head_xy[1] - tail_xy[1]
    adx, ady = abs(dx), abs(dy)

    if adx == 2:
        tail_xy[0] = tail_xy[0] + (dx/adx)
        if ady == 1:
            tail_xy[1] = tail_xy[1] + dy

    if ady == 2:
        tail_xy[1] = tail_xy[1] + (dy/ady)
        if adx == 1:
            tail_xy[0] = tail_xy[0] + dx

    tail_xy = [int(tail_xy[0]), int(tail_xy[1])]
    return tail_xy

head_pos = initial_head_pos.copy()
tail_pos = initial_tail_pos.copy()

for i in instructions:
    new_head_pos = move_head(head_pos, i)
    head_log.append(new_head_pos)

    new_tail_pos = move_tail(head_pos, tail_pos)
    tail_log.append(new_tail_pos)

    head_pos = new_head_pos.copy()
    tail_pos = new_tail_pos.copy()

#print(head_log)
#print(tail_log)

unique_tail_pos = []

for j in tail_log:
    if j in unique_tail_pos:
        continue
    else:
        unique_tail_pos.append(j)
#print(unique_tail_pos)
print(len(unique_tail_pos))
"""
--- Part Two ---
A rope snaps! Suddenly, the river is getting a lot closer than you remember. The bridge is still there, but some of the 
ropes that broke are now whipping toward you as you fall through the air!

The ropes are moving too quickly to grab; you only have a few seconds to choose how to arch your body to avoid being 
hit. Fortunately, your simulation can be extended to support longer ropes.

Rather than two knots, you now must simulate a rope consisting of ten knots. One knot is still the head of the rope and 
moves according to the series of motions. Each knot further down the rope follows the knot in front of it using the same 
rules as before.

Using the same series of motions as the above example, but with the knots marked H, 1, 2, ..., 9, the motions now occur 
as follows:

== Initial State ==
##### deleted ######
......
......
.1H3..  (H covers 2, 4)
.5....
6.....  (6 covers 7, 8, 9, s)
Now, you need to keep track of the positions the new tail, 9, visits. In this example, the tail never moves, and so it 
only visits 1 position. However, be careful: more types of motion are possible than before, so you might want to 
visually compare your simulated rope to the one above.

Here's a larger example:

R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
These motions occur as follows (individual steps are not shown):

== Initial State ==

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
...........H..............  (H covers 1, 2, 3, 4, 5, 6, 7, 8, 9, s)
..........................
..........................
..........................
..........................
..........................

##### deleted #####

== U 20 ==

H.........................
1.........................
2.........................
3.........................
4.........................
5.........................
6.........................
7.........................
8.........................
9.........................
..........................
..........................
..........................
..........................
..........................
...........s..............
..........................
..........................
..........................
..........................
..........................

Now, the tail (9) visits 36 positions (including s) at least once:

..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
..........................
#.........................
#.............###.........
#............#...#........
.#..........#.....#.......
..#..........#.....#......
...#........#.......#.....
....#......s.........#....
.....#..............#.....
......#............#......
.......#..........#.......
........#........#........
.........########.........
Simulate your complete series of motions on a larger rope with ten knots. How many positions does the tail of the rope visit at least once?

"""

initial_rope_pos = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
rope_log = [initial_rope_pos]
rope_pos = initial_rope_pos.copy()

for i in instructions:
    for j in range(0, len(rope_pos)):
        if j == 0:
            rope_pos[0] = move_head(rope_pos[0], i)
        else:
            rope_pos[j] = move_tail(rope_pos[j-1], rope_pos[j])
    #print(i)
    #print(rope_pos)
    new_rope_pos = rope_pos.copy()
    rope_log.append(new_rope_pos)

#print('rope log')
#print(rope_log)
unique_tail_pos = []

for j in rope_log:
    if j[9] in unique_tail_pos:
        continue
    else:
        unique_tail_pos.append(j[9])
#print(unique_tail_pos)
print(len(unique_tail_pos))