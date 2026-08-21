#!/usr/bin/env python3
import sys

async def main(argc: int, *argv:str) -> None:
    return


def launch(*args: str) -> None:
    from .launch import launch_smg_client
    launch_smg_client(*args)

if __name__ == "__main__":
    launch(*sys.argv[1:])
