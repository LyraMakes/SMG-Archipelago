from __future__ import annotations
import random
from enum import StrEnum
from typing import NamedTuple, Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    from . import SMGWorld

from BaseClasses import Item, ItemClassification

smg_base_id: int = 0xEFA000

class SMGItem(Item):
    game: str = "Super Mario Galaxy"

class SMGItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression


class ItemNames(StrEnum):
    POWER_STAR      = "Power_Star"
    GREEN_STAR      = "Green_Star"

    BJrRR_ACCESS    = "Bowser Jr's Robot Reactor: Access"
    BSR_ACCESS      = "Bowser's Star Reactor: Access"
    BJrAA_ACCESS    = "Bowser Jr's Airship Armada: Access"
    BDMP_ACCESS     = "Bowser's Dark Matter Plant: Acess"
    BJrLR_ACCESS    = "Bowser Jr's Lava Reactor: Access"

    RESCUE_ACCESS   = "Luigi Rescue Access"
    COMET_ACCESS    = "Comet Mission Access"
    PURPLE_ACCESS   = "Purple Comet Access"
    
    STARBITS        = "Star Bits"
    ONEUP           = "1UP Mushroom"


NEXT_OFFSET_NUM = 0
def create_location_data(classification: ItemClassification = ItemClassification.progression):
    global NEXT_OFFSET_NUM
    item = SMGItemData(smg_base_id + NEXT_OFFSET_NUM, classification)
    NEXT_OFFSET_NUM += 1
    return item

item_data_table: Dict[str, SMGItemData] = {
    ItemNames.POWER_STAR:       create_location_data(ItemClassification.progression_deprioritized_skip_balancing),
    ItemNames.GREEN_STAR:       create_location_data(ItemClassification.progression_deprioritized_skip_balancing),

    ItemNames.BJrRR_ACCESS:     create_location_data(),
    ItemNames.BSR_ACCESS:       create_location_data(),
    ItemNames.BJrAA_ACCESS:     create_location_data(),
    ItemNames.BDMP_ACCESS:      create_location_data(),
    ItemNames.BJrLR_ACCESS:     create_location_data(),

    ItemNames.RESCUE_ACCESS:    create_location_data(),
    ItemNames.COMET_ACCESS:     create_location_data(),
    ItemNames.PURPLE_ACCESS:    create_location_data(),

    ItemNames.STARBITS:         create_location_data(ItemClassification.filler),
    ItemNames.ONEUP:            create_location_data(ItemClassification.filler),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}


def create_single_item(world: SMGWorld, name: str) -> SMGItem:
    classification = item_data_table[name].classification
    code = item_data_table[name].code
    return SMGItem(name, classification, code, world.player)


def create_all_items(world: SMGWorld) -> None:
    itempool: List[Item] = [
        world.create_item(ItemNames.BJrRR_ACCESS),
        world.create_item(ItemNames.BSR_ACCESS),
        world.create_item(ItemNames.BJrAA_ACCESS),
        world.create_item(ItemNames.BDMP_ACCESS),
        world.create_item(ItemNames.BJrLR_ACCESS),
    ]

    itempool += [world.create_item(ItemNames.POWER_STAR) for _ in range(119)]
    itempool += [world.create_item(ItemNames.GREEN_STAR) for _ in range(3)]

    if world.options.initial_gateway_rando:
        itempool.append(world.create_item(ItemNames.POWER_STAR))

    if world.options.luigi_rando:
        itempool.append(world.create_item(ItemNames.RESCUE_ACCESS))

    if world.options.comet_rando:
        itempool.append(world.create_item(ItemNames.COMET_ACCESS))
        
    if world.options.purple_comet_rando:
        itempool.append(world.create_item(ItemNames.PURPLE_ACCESS))


    unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    filled_spots = len(itempool)
    needed_filler = unfilled_locations - filled_spots

    if needed_filler < 0:
        raise ValueError(f"Attempted to place too many items. Filled {filled_spots} with {unfilled_locations} left")

    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool


def get_filler_item_name():
    return random.choice([ItemNames.STARBITS, ItemNames.ONEUP])
