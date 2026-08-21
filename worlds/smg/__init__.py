from collections.abc import Mapping
import logging
from typing import Any


from .options import smg_option_groups, smg_option_presets, SMGOptions
from .items import item_table, SMGItem, create_all_items, create_single_item, get_filler_item_name
from .locations import location_table, create_all_locations
from .regions import create_regions
from .rules import set_all_rules
from .generator import generate_basic


from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World


logger = logging.getLogger("Super Mario Galaxy")

class SMGWebWorld(WebWorld):
    game = "Super Mario Galaxy"
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Super Mario Galaxy randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Cynix"]
    )

    tutorials = [setup_en]

    option_groups = smg_option_groups
    options_presets = smg_option_presets


class SMGWorld(World):
    """
    Super Mario Galaxy is a game for the Nintendo Wii.
    """

    game = "Super Mario Galaxy"

    web = SMGWebWorld()
    options_dataclass = SMGOptions
    options: SMGOptions

    item_name_to_id = item_table
    location_name_to_id = location_table

    origin_region_name = "Comet Obervatory"

    required_client_version = (0, 6, 7)

    def create_regions(self) -> None:
        create_regions(self)
        create_all_locations(self)

    def set_rules(self) -> None:
        set_all_rules(self)

    def create_items(self) -> None:
        create_all_items(self) 

    def create_item(self, name: str) -> SMGItem:
        return create_single_item(self, name)

    def get_filler_item_name(self) -> str:
        return get_filler_item_name()

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "star_amount",
            "initial_gateway_rando",
            "luigi_rando",
            "comet_rando",
            "purple_comet_rando",
            "death_link",
            "completion_type"
        )
    
    def generate_basic(self) -> None:
        return generate_basic(self)
