# StateMinimization

This is a little script that calculates the optimal number of states
for a given finite state machine.

## How it works

The algorithm behind it is a greedy algorithm that begins by grouping each
state into the minimum possible grouping, and then it continually splits
each of these groups up until no more splits can be performed without
introducing redundancies.

## Operation

Edit the arguments to the `MinimizeStates()` function in `main()` to reflect
your state machine and execute the script.

## License
MIT License
