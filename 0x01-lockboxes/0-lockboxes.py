#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
    boxes (List[List[int]]): A list of lists where each list contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, else False.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                keys.append(key)
    
    return all(unlocked)

