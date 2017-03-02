#!/usr/bin/env python

import collections

def PrintGrouping(groupDict):
    groupId = 0

    for states in groupDict.values():
        groupId += 1

        for state in states:
            print('{} {}'.format(groupId, state))

    print('=====')

def CalcNextGrouping(stateDict, nextStates):
    nextGrouping = {}

    for state in stateDict.keys():
        toople = tuple(map(lambda ns: stateDict[ns], nextStates[state]))

        nextGrouping[state] = hash(toople) ^ stateDict[state]

    return nextGrouping

def ConstructGroupDict(stateDict):
    groupDict = collections.defaultdict(set)

    for (state, group) in stateDict.items():
        groupDict[group].add(state)

    # I need the dict's elements to be hashable, so I have to convert
    # the elements to an immutable type.
    result = {}

    for (group, states) in groupDict.items():
        result[group] = tuple(states)

    return result

def IsFinished(nextGrouping, currGrouping):
    return set(nextGrouping.values()) == set(currGrouping.values())

def StateMinimize(states, nextStates):
    groupDict = ConstructGroupDict(states)

    PrintGrouping(groupDict)

    while True:
        nextGrouping = CalcNextGrouping(states, nextStates)
        nextGroupDict = ConstructGroupDict(nextGrouping)

        if IsFinished(nextGroupDict, groupDict):
            return

        PrintGrouping(nextGroupDict)

        states = nextGrouping
        groupDict = nextGroupDict

def MinimizeStates(states, nextState, output):
    stateDict = {}
    nextStateDict = {}
    i = 0

    for state in states:
        stateDict[state] = hash(output[i])
        nextStateDict[state] = nextState[i]

        i += 1

    StateMinimize(stateDict, nextStateDict)
def main():
    MinimizeStates(states='ABCDEFGHJKL', nextState=['HF','JL','FC','HA','BJ','KA','JG','BC','AC','JB','DA'], output=[0,0,1,1,1,0,1,1,1,1,0])

    return 0;

if __name__ == '__main__':
    main()
