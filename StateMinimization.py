#!/usr/bin/env python3

import sys
import collections

def PrintGrouping(groupDict):
    groupId = 0

    for states in groupDict.values():
        groupId += 1

        for state in states:
            print('{} {}'.format(groupId, state))

    print('=====')

def CalcNextStateGrouping(stateDict, nextStates):
    nextGrouping = {}

    for state in stateDict.keys():
        stateTuple = tuple(map(lambda ns: stateDict[ns], nextStates[state]))

        nextGrouping[state] = hash(stateTuple) ^ stateDict[state]

    return nextGrouping

def ReverseMapping(stateGroup):
    groupStates = collections.defaultdict(set)

    for (state, group) in stateGroup.items():
        groupStates[group].add(state)

    # I need the return value's elements to be hashable, so I have to convert
    # the elements to an immutable type.
    result = {}

    for (group, states) in groupStates.items():
        result[group] = tuple(states)

    return result

def IsFinished(nextGrouping, currGrouping):
    # Once a fixed-point has been reached, the minimal grouping has been achieved.
    return set(nextGrouping.values()) == set(currGrouping.values())

def MinimizationLoop(stateGroup, nextStates):
    currGroupStates = ReverseMapping(stateGroup)

    PrintGrouping(currGroupStates)

    while True:
        nextStateGrouping = CalcNextStateGrouping(stateGroup, nextStates)
        nextGroupStates = ReverseMapping(nextStateGrouping)

        if IsFinished(nextGroupStates, currGroupStates):
            return

        PrintGrouping(nextGroupStates)

        stateGroup = nextStateGrouping
        currGroupStates = nextGroupStates

def MinimizeStates(states, transitions, outputs):
    # stateGroup[s] -> The group to which state s belongs.
    #
    #   A group is a collection of one or more FSM states, and can be considered
    #   a meta-state of sorts. The goal of this program is to group the states
    #   of the input FSM into the smallest number of groups possible while
    #   keeping its functionality intact. In other words, this program finds an
    #   equivalent state machine with the optimal number of states.
    stateGroup = {}
    # stateTransitions[s] -> The groups that are reachable from state s.
    #
    #   The value of an entry in stateTransitions is an ordered list
    #   whose values are the names of a states in the FSM. Note that it is an
    #   ordered list. The order is important because the order corresponds
    #   to a particular input value to the state machine.
    #       To clarify, let I be an input vector to the state machine,
    #   and index(I) be the corresponding index value to the ordered state list.
    #   Consider a state machine at state S with the current input being I. The
    #   machine's next state will be stateTransitions[S][index(I)].
    stateTransitions = {}

    for i in range(0, len(states)):
        currState = states[i];

        stateGroup[currState] = hash(outputs[i])
        stateTransitions[currState] = transitions[i]

    MinimizationLoop(stateGroup, stateTransitions)


def main():
    # The minimal FSM should be
    # 1: A, F
    # 2: B, J
    # 3: C
    # 4: D, G
    # 5: E
    # 6: H, K
    MinimizeStates(states='ABCDEFGHJK',
            transitions=['DJ','KF','FC','HJ','BK','GJ','KB','BC','HA','JC'],
            outputs=[2,2,3,1,3,2,1,3,2,3])

    return 0;

if __name__ == '__main__':
    sys.exit(main())
