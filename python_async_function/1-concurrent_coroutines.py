#!/usr/bin/env python3

import typing
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    listy = []
    for _ in range(n):
        elem = await wait_random(max_delay)
        for j in range(len(listy)):
            if elem <= listy[j]:
                listy.insert(j, elem)
                break
        else:
            listy.append(elem)
    return listy
