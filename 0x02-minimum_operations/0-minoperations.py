#!/usr/bin/python3
""" Module for 0-minoperations"""

def minOperations(n):
"""Gets fewest # of operations needed to result in exactly n H characters
"""
     if n < 2:
        return 0
    
    ops, root = 0, 2
    
    while root * root <= n:
        if n % root == 0:
            while n % root == 0:
                ops += root
                n //= root
        root += 1
    
    if n > 1:
        ops += n
    
    return ops
