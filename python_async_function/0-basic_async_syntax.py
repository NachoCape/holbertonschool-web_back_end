#!/usr/bin/env python3

import random
import asyncio

async def wait_random(max_delay: int = 2) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay