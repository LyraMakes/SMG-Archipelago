from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import SMGWorld

from .items import ItemNames


def generate_basic(world: SMGWorld) -> None:
    if not world.options.luigi_rando:
        world.multiworld.get_location("Luigi Rescue Access", world.player).place_locked_item(world.create_item(ItemNames.RESCUE_ACCESS))
        
    if not world.options.comet_rando:
        world.multiworld.get_location("Comet Mission Access", world.player).place_locked_item(world.create_item(ItemNames.COMET_ACCESS))

    if not world.options.purple_comet_rando:
        world.multiworld.get_location("Purple Comet Access", world.player).place_locked_item(world.create_item(ItemNames.PURPLE_ACCESS))

    if not world.options.initial_gateway_rando:
        world.multiworld.get_location("Gateway Galaxy: Grand Star Rescue", world.player).place_locked_item(world.create_item(ItemNames.POWER_STAR))
