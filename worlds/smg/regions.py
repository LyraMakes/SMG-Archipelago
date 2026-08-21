from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import SMGWorld

from BaseClasses import Region

def create_regions(world: SMGWorld) -> None:
    observatory = Region("Comet Obervatory", world.player, world.multiworld)
    terrace     = Region("Terrace", world.player, world.multiworld)
    fountain    = Region("Fountain", world.player, world.multiworld)
    kitchen     = Region("Kitchen", world.player, world.multiworld)
    bedroom     = Region("Bedroom", world.player, world.multiworld)
    engine_room = Region("Engine Room", world.player, world.multiworld)
    garden      = Region("Garden", world.player, world.multiworld)
    trials      = Region("Trial Galaxies", world.player, world.multiworld)

    unassigned  = Region("Unassigned", world.player, world.multiworld)

    regions = [observatory, terrace, fountain, kitchen, bedroom, engine_room, garden, trials, unassigned]
    world.multiworld.regions += regions
    # Connect regions

    observatory.connect(terrace,        "Observatory to Terrace")
    observatory.connect(fountain,       "Observatory to Fountain")
    observatory.connect(kitchen,        "Observatory to Kitchen")
    observatory.connect(bedroom,        "Observatory to Bedroom")
    observatory.connect(engine_room,    "Observatory to Engine Room")
    observatory.connect(garden,         "Observatory to Garden")
    observatory.connect(trials,         "Observatory to Trial Galaxies")
    observatory.connect(unassigned,     "Observatory to Unassigned Missions")