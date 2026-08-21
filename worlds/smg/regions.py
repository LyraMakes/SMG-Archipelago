from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import SMGWorld


from enum import StrEnum

from BaseClasses import Region



class RegionNames(StrEnum):
    OBSERVATORY = "Comet Obervatory"
    TERRACE = "Terrace"
    FOUNTAIN = "Fountain"
    KITCHEN = "Kitchen"
    BEDROOM = "Bedroom"
    ENGINE_ROOM = "Engine Room"
    GARDEN = "Garden"
    TRIALS = "Trial Galaxies"

    UNASSIGNED = "Unassigned"
    

class EntranceNames(StrEnum):
    OBSERVATORY_TERRACE = "Observatory to Terrace"
    OBSERVATORY_FOUNTAIN = "Observatory to Fountain"
    OBSERVATORY_KITCHEN = "Observatory to Kitchen"
    OBSERVATORY_BEDROOM = "Observatory to Bedroom"
    OBSERVATORY_ENGINE_ROOM = "Observatory to Engine Room"
    OBSERVATORY_GARDEN = "Observatory to Garden"
    OBSERVATORY_TRIALS = "Observatory to Trial Galaxies"
    OBSERVATORY_UNASSIGNED = "Observatory to Unassigned Missions"


def create_regions(world: SMGWorld) -> None:
    observatory = Region(RegionNames.OBSERVATORY, world.player, world.multiworld)
    terrace     = Region(RegionNames.TERRACE, world.player, world.multiworld)
    fountain    = Region(RegionNames.FOUNTAIN, world.player, world.multiworld)
    kitchen     = Region(RegionNames.KITCHEN, world.player, world.multiworld)
    bedroom     = Region(RegionNames.BEDROOM, world.player, world.multiworld)
    engine_room = Region(RegionNames.ENGINE_ROOM, world.player, world.multiworld)
    garden      = Region(RegionNames.GARDEN, world.player, world.multiworld)
    trials      = Region(RegionNames.TRIALS, world.player, world.multiworld)

    unassigned  = Region(RegionNames.UNASSIGNED, world.player, world.multiworld)

    regions = [observatory, terrace, fountain, kitchen, bedroom, engine_room, garden, trials, unassigned]
    world.multiworld.regions += regions
    # Connect regions

    observatory.connect(terrace,        EntranceNames.OBSERVATORY_TERRACE)
    observatory.connect(fountain,       EntranceNames.OBSERVATORY_FOUNTAIN)
    observatory.connect(kitchen,        EntranceNames.OBSERVATORY_KITCHEN)
    observatory.connect(bedroom,        EntranceNames.OBSERVATORY_BEDROOM)
    observatory.connect(engine_room,    EntranceNames.OBSERVATORY_ENGINE_ROOM)
    observatory.connect(garden,         EntranceNames.OBSERVATORY_GARDEN)
    observatory.connect(trials,         EntranceNames.OBSERVATORY_TRIALS)
    observatory.connect(unassigned,     EntranceNames.OBSERVATORY_UNASSIGNED)