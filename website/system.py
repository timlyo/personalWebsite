import os

import psutil

COEFFICIENT = 2 ** 20


def get_other_ram() -> int:
    """Ram used by other processes"""
    return get_ram_used() - get_process_ram()


def get_total_ram() -> int:
    mem = psutil.virtual_memory()
    return mem[0] / COEFFICIENT


def get_process_ram() -> int:
    process = psutil.Process(os.getpid())
    return process.memory_info()[0] / COEFFICIENT


def get_ram_used() -> int:
    """ram used by all processes"""
    mem = psutil.virtual_memory()
    return mem[4] / COEFFICIENT
