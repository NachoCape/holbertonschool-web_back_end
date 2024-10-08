#!/usr/bin/env python3

wait_n = __import__('1-concurrent_coroutines').wait_n
import asyncio
import time

def measure_time(n:int, max_delay:int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    
    total_time = (end - start) / n      
    return total_time