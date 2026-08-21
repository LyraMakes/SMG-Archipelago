from __future__ import annotations
import random

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


NEXT_OFFSET_NUM = 0
def create_location_data(classification: ItemClassification = ItemClassification.progression):
    global NEXT_OFFSET_NUM
    item = SMGItemData(smg_base_id + NEXT_OFFSET_NUM, classification)
    NEXT_OFFSET_NUM += 1
    return item

item_data_table: Dict[str, SMGItemData] = {
    "Power_Star":                           create_location_data(ItemClassification.progression_deprioritized_skip_balancing),
    "Green_Star":                           create_location_data(ItemClassification.progression_deprioritized_skip_balancing),

    "Bowser Jr's Robot Reactor: Access":    create_location_data(),
    "Bowser's Star Reactor: Access":        create_location_data(),
    "Bowser Jr's Airship Armada: Access":   create_location_data(),
    "Bowser's Dark Matter Plant: Access":   create_location_data(),
    "Bowser Jr's Lava Reactor: Access":     create_location_data(),

    "Luigi Rescue Access":                  create_location_data(),
    "Comet Mission Access":                 create_location_data(),
    "Purple Comet Access":                  create_location_data(),

    "Star Bits":                            create_location_data(ItemClassification.filler),
    "1UP Mushroom":                         create_location_data(ItemClassification.filler),
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}


def create_single_item(world: SMGWorld, name: str) -> SMGItem:
    classification = item_data_table[name].classification
    code = item_data_table[name].code
    return SMGItem(name, classification, code, world.player)


def create_all_items(world: SMGWorld) -> None:
    itempool: List[Item] = [
        world.create_item("Bowser Jr's Robot Reactor: Access"),
        world.create_item("Bowser's Star Reactor: Access"),
        world.create_item("Bowser Jr's Airship Armada: Access"),
        world.create_item("Bowser's Dark Matter Plant: Access"),
        world.create_item("Bowser Jr's Lava Reactor: Access"),
    ]

    itempool += [world.create_item("Power_Star") for _ in range(119)]
    itempool += [world.create_item("Green_Star") for _ in range(3)]

    if world.options.initial_gateway_rando:
        itempool.append(world.create_item("Power_Star"))

    if world.options.luigi_rando:
        itempool.append(world.create_item("Luigi Rescue Access"))

    if world.options.comet_rando:
        itempool.append(world.create_item("Comet Mission Access"))
        
    if world.options.purple_comet_rando:
        itempool.append(world.create_item("Purple Comet Access"))


    unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    filled_spots = len(itempool)
    needed_filler = unfilled_locations - filled_spots

    if needed_filler < 0:
        raise ValueError(f"Attempted to place too many items. Filled {filled_spots} with {unfilled_locations} left")

    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool


def get_filler_item_name():
    return random.choice(["Star Bits", "1UP Mushroom"])
