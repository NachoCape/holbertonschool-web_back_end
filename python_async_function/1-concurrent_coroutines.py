#!/usr/bin/env python3

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int) -> list[float]:
    
    listy = []
    for i in range(n):
        elem = await wait_random(max_delay)
        if len(listy) == 0:
            listy.append(elem)
        else:
            for j in range(0, len(listy)):
                if elem <= listy[j]:
                    listy.insert(j, elem)
                    break  
    return listy