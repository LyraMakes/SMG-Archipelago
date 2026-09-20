#!/usr/bin/env python3
import asyncio
import sys

from argparse import Namespace
from copy import deepcopy
from enum import Enum
from typing import Dict, Any, List

from CommonClient import gui_enabled, CommonContext, ClientCommandProcessor, server_loop
from CommonClient import logger

from ..locations import location_data_table

# import logging
# logger = logging.getLogger("Super Mario Galaxy Client")

class ConnectionStatus(Enum):
    NOT_CONNECTED = 0
    SCOUTS_NOT_SENT = 1
    SCOUTS_SENT = 2
    GAME_RUNNING = 3

class SMGCommandProcessor(ClientCommandProcessor):
    async def _cmd_check(self, *locations: str):
        """Check a location"""
        if isinstance(self.ctx, SMGContext):
            for loc in locations:
                if loc not in location_data_table.keys():
                    logger.info("Not a recognized location")
                    return
                loc_id = location_data_table[loc].code
                if loc_id is None:
                    logger.info("Invalid location")
                    return
                logger.debug(f"{self.ctx.slot} just checked {loc}")
                await self.ctx.send_location(loc_id)


class SMGContext(CommonContext):
    game = "Super Mario Galaxy"
    items_handling = 0b111

    last_connected_slot: int | None = None

    slot_data: Dict[str, Any]
    connection_status: ConnectionStatus = ConnectionStatus.NOT_CONNECTED
    queued_locations: List[int]
    command_processor = SMGCommandProcessor

    def __init__(self, server_address: str | None = None, password: str | None = None) -> None:
        super().__init__(server_address, password)
        self.slot_data = {}
        self.queued_locations = []

    async def server_auth(self, password_requested: bool = False):
        await super().server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    def on_package(self, cmd: str, args: dict):
        if cmd == "Connected":
            if self.connection_status:
                pass

        return super().on_package(cmd, args)

    async def send_location(self, loc_id: int):
        await self.send_msgs([
            {"cmd": "LocationChecks", "locations": [loc_id]}
        ])
        

async def main(args: Namespace) -> None:
    logger.info("Starting Super Mario Galaxy Client")
    ctx = SMGContext(args.connect, args.password)
    ctx.auth = args.name
    ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
    
    if gui_enabled:
        ctx.run_gui()
    ctx.run_cli()

    await ctx.exit_event.wait()
    await ctx.shutdown()


def launch(*args: str) -> None:
    from .launch import launch_smg_client
    launch_smg_client(*args)

if __name__ == "__main__":
    launch(*sys.argv[1:])
