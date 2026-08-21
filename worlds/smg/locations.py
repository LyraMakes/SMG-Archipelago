from __future__ import annotations
from typing import Any, Dict, NamedTuple, List, TYPE_CHECKING

if TYPE_CHECKING:
    from . import SMGWorld

from .items import SMGItem

from BaseClasses import Location

smg_base_id: int = 0xEFA000

class SMGLocation(Location):
    game: str = "Super Mario Galaxy"


class SMGLocationData(NamedTuple):
    code: int | None = None
    vanilla_item_data: str | None = "Power_Star"


NEXT_OFFSET_NUM = 0
def create_location_data(vanilla_item_data: str | None = "Power_Star"):
    global NEXT_OFFSET_NUM
    loc = SMGLocationData(smg_base_id + NEXT_OFFSET_NUM, vanilla_item_data)
    NEXT_OFFSET_NUM += 1
    return loc


loc_terrace_data = {
    "Good Egg Galaxy: Dino Piranha":                    create_location_data(),
    "Good Egg Galaxy: A Snack of Cosmic Proportions":   create_location_data(),
    "Good Egg Galaxy: King Kaliente's Battle Fleet":    create_location_data(),
    "Good Egg Galaxy: Dino Piranha Speed Run":          create_location_data(),
    "Good Egg Galaxy: Purple Coin Omelet":              create_location_data(),
    "Good Egg Galaxy: Luigi on the Roof":               create_location_data(),
    "Honeyhive Galaxy: Bee Mario Takes Flight":         create_location_data(),
    "Honeyhive Galaxy: Trouble on the Tower":           create_location_data(),
    "Honeyhive Galaxy: Big Bad Bugaboom":               create_location_data(),
    "Honeyhive Galaxy: Honeyhive Cosmic Mario Race":    create_location_data(),
    "Honeyhive Galaxy: The Honeyhive's Purple Coins":   create_location_data(),
    "Honeyhive Galaxy: Luigi in the Honeyhive Kingdom": create_location_data(),
    "Loopdeeloop Galaxy: Surfing 101":                  create_location_data(),
    "Flipswitch Galaxy: Painting the Planet Yellow":    create_location_data(),
    "Sweet Sweet Galaxy: Rocky Road":                   create_location_data(),
    "Bowser Jr's Robot Reactor: Access":                create_location_data("Bowser Jr's Robot Reactor: Access"),
    "Bowser Jr's Robot Reactor: Megaleg's Moon":        create_location_data(),
}

loc_fountain_data = {
    "Space Junk Galaxy: Pull Star Path":                    create_location_data(),
    "Space Junk Galaxy: Kamella's Airship Attack":          create_location_data(),
    "Space Junk Galaxy: Tarantox's Tangled Web":            create_location_data(),
    "Space Junk Galaxy: Pull Star Path Speed Run":          create_location_data(),
    "Space Junk Galaxy: Purple Coin Spacewalk":             create_location_data(),
    "Space Junk Galaxy: Yoshi's Unexpected Appearance":     create_location_data(),
    "Battlerock Galaxy: Battlerock Barrage":                create_location_data(),
    "Battlerock Galaxy: Breaking into the Battlerock":      create_location_data(),
    "Battlerock Galaxy: Topmaniac and the Topman Tribe":    create_location_data(),
    "Battlerock Galaxy: Topmaniac's Daredevil Run":         create_location_data(),
    "Battlerock Galaxy: Purple Coins on the Battlerock":    create_location_data(),
    "Battlerock Galaxy: Battlerock's Garbage Dump":         create_location_data(),
    "Battlerock Galaxy: Luigi under the Saucer":            create_location_data(),
    "Battlerock Galaxy: Green Star":                        create_location_data("Green_Star"),
    "Rolling Green Galaxy: Rolling in the Clouds":          create_location_data(),
    "Hurry-Scurry Galaxy: Shrinking Satellite":             create_location_data(),
    "Sling Pod Galaxy: A Very Sticky Situation":            create_location_data(),
    "Bowser's Star Reactor: Access":                        create_location_data("Bowser's Star Reactor: Access"),
    "Bowser's Star Reactor: The Fiery Stronghold":          create_location_data(),
}

loc_kitchen_data = {
    "Beach Bowl Galaxy: Sunken Treasure":                   create_location_data(),
    "Beach Bowl Galaxy: Passing the Swim Test":             create_location_data(),
    "Beach Bowl Galaxy: Secret Undersea Cavern":            create_location_data(),
    "Beach Bowl Galaxy: Fast Foes on the Stone Cyclone":    create_location_data(),
    "Beach Bowl Galaxy: Beachcombing for Purple Coins":     create_location_data(),
    "Beach Bowl Galaxy: Wall Jumping up Waterfalls":        create_location_data(),
    "Ghostly Galaxy: Luigi and the Haunted Mansion":        create_location_data(),
    "Ghostly Galaxy: A Very Spooky Sprint":                 create_location_data(),
    "Ghostly Galaxy: Beware of Bouldergeist":               create_location_data(),
    "Ghostly Galaxy: Bouldergeist's Daredevil Run":         create_location_data(),
    "Ghostly Galaxy: Purple Coins in the Bone Pen":         create_location_data(),
    "Ghostly Galaxy: Matter Splatter Mansion":              create_location_data(),
    "Drip Drop Galaxy: Giant Eel Outbreak":                 create_location_data(),
    "Buoy Base Galaxy: The Floating Fortress":              create_location_data(),
    "Buoy Base Galaxy: Secret Buoy Base":                   create_location_data(),
    "Buoy Base Galaxy: Green Star":                         create_location_data("Green_Star"),
    "Bubble Breeze Galaxy: Through the Poison Swamp":       create_location_data(),
    "Bowser Jr's Airship Armada: Access":                   create_location_data("Bowser Jr's Airship Armada: Access"),
    "Bowser Jr's Airship Armada: Sinking the Airships":     create_location_data(),
}

loc_bedroom_data = {
    "Gusty Garden Galaxy: Bunnies in the Wind":                 create_location_data(),
    "Gusty Garden Galaxy: The Dirty Tricks of Major Burrows":   create_location_data(),
    "Gusty Garden Galaxy: Gusty Garden's Gravity Scramble":     create_location_data(),
    "Gusty Garden Galaxy: Major Burrows's Daredevil Run":       create_location_data(),
    "Gusty Garden Galaxy: Purple Coins on the Puzzle Cube":     create_location_data(),
    "Gusty Garden Galaxy: The Golden Chomp":                    create_location_data(),
    "Freezeflame Galaxy: The Frozen Peak of Baron Brrr":        create_location_data(),
    "Freezeflame Galaxy: Freezeflame's Blistering Core":        create_location_data(),
    "Freezeflame Galaxy: Hot and Cold Collide":                 create_location_data(),
    "Freezeflame Galaxy: Frosty Cosmic Mario Race":             create_location_data(),
    "Freezeflame Galaxy: Purple Coins on the Summit":           create_location_data(),
    "Freezeflame Galaxy: Conquering the Summit":                create_location_data(),
    "Dusty Dune Galaxy: Soaring on the Desert Winds":           create_location_data(),
    "Dusty Dune Galaxy: Blasting through the Sand":             create_location_data(),
    "Dusty Dune Galaxy: Sunbaked Sand Castle":                  create_location_data(),
    "Dusty Dune Galaxy: Sandblast Speed Run":                   create_location_data(),
    "Dusty Dune Galaxy: Purple Coins in the Desert":            create_location_data(),
    "Dusty Dune Galaxy: Bullet Bill on Your Back":              create_location_data(),
    "Dusty Dune Galaxy: Treasure of the Pyramid":               create_location_data(),
    "Dusty Dune Galaxy: Green Star":                            create_location_data("Green_Star"),
    "Honeyclimb Galaxy: Scaling the Sticky Wall":               create_location_data(),
    "Bigmouth Galaxy: Bigmouth's Gold Bait":                    create_location_data(),
    "Bowser's Dark Matter Plant: Access":                       create_location_data("Bowser's Dark Matter Plant: Access"),
    "Bowser's Dark Matter Plant: Darkness on the Horizon":      create_location_data(),
}

loc_engineroom_data = {
    "Gold Leaf Galaxy: Star Bunnies on the Hunt":               create_location_data(),
    "Gold Leaf Galaxy: Cataquack to the Skies":                 create_location_data(),
    "Gold Leaf Galaxy: When It Rains, It Pours":                create_location_data(),
    "Gold Leaf Galaxy: Cosmic Mario Forest Race":               create_location_data(),
    "Gold Leaf Galaxy: Purple Coins in the Woods":              create_location_data(),
    "Gold Leaf Galaxy: The Bell on the Big Tree":               create_location_data(),
    "Sea Slide Galaxy: Going After Guppy":                      create_location_data(),
    "Sea Slide Galaxy: Faster Than a Speeding Penguin":         create_location_data(),
    "Sea Slide Galaxy: The Silver Stars of Sea Slide":          create_location_data(),
    "Sea Slide Galaxy: Underwater Cosmic Mario Race":           create_location_data(),
    "Sea Slide Galaxy: Purple Coins by the Seaside":            create_location_data(),
    "Sea Slide Galaxy: Hurry, He's Hungry":                     create_location_data(),
    "Toy Time Galaxy: Heavy Metal Mecha-Bowser":                create_location_data(),
    "Toy Time Galaxy: Mario Meets Mario":                       create_location_data(),
    "Toy Time Galaxy: Bouncing Down Cake Lane":                 create_location_data(),
    "Toy Time Galaxy: Fast Foes of Toy Time":                   create_location_data(),
    "Toy Time Galaxy: Luigi's Purple Coins":                    create_location_data(),
    "Toy Time Galaxy: The Flipswitch Chain":                    create_location_data(),
    "Bonefin Galaxy: Kingfin's Fearsome Waters":                create_location_data(),
    "Sand Spiral Galaxy: Chosing a Favorite Snack":             create_location_data(),
    "Bowser Jr's Lava Reactor: Access":                         create_location_data("Bowser Jr's Lava Reactor: Access"),
    "Bowser Jr's Lava Reactor: King Kaliente's Spicy Return":   create_location_data(),
}

loc_garden_data = {
    "Deep Dark Galaxy: The Undergroud Ghost Ship":          create_location_data(),
    "Deep Dark Galaxy: Bubble Blastoff":                    create_location_data(),
    "Deep Dark Galaxy: Guppy and the Underground Lake":     create_location_data(),
    "Deep Dark Galaxy: Ghost Ship Daredevil Run":           create_location_data(),
    "Deep Dark Galaxy: Plunder the Purple Coins":           create_location_data(),
    "Deep Dark Galaxy: Boo in a Box":                       create_location_data(),
    "Dreadnought Galaxy: Infiltrating the Dreadnought":     create_location_data(),
    "Dreadnought Galaxy: Dreadnought's Colossan Cannons":   create_location_data(),
    "Dreadnought Galaxy: Revenge of the Topman Tribe":      create_location_data(),
    "Dreadnought Galaxy: Topman Tribe Speed Run":           create_location_data(),
    "Dreadnought Galaxy: Battlestation's Purple Coins":     create_location_data(),
    "Dreadnought Galaxy: Dreadnought's Garbage Dump":       create_location_data(),
    "Melty Molten Galaxy: The Sinking Lava Spire":          create_location_data(),
    "Melty Molten Galaxy: Through the Meteor Storm":        create_location_data(),
    "Melty Molten Galaxy: Fiery Dino Piranha":              create_location_data(),
    "Melty Molten Galaxy: Lava Spire Daredevil Run":        create_location_data(),
    "Melty Molten Galaxy: Red-Hot Purple Coins":            create_location_data(),
    "Melty Molten Galaxy: Burning Tide":                    create_location_data(),
    "Matter Splatter Galaxy: Watch Your Step":              create_location_data(),
    "Snowcap Galaxy: Star Bunnies in the Snow":             create_location_data(),
}

loc_trials_data = {
    "Loopdeswoop Galaxy: The Galaxy's Greatest Wave":       create_location_data(),
    "Bubble Blast Galaxy: The Electric Labyrinth":          create_location_data(),
    "Rolling Gizmo Galaxy: Gizmo's, Gears, and Gadgets":    create_location_data(),
}

loc_special_data = {
    "Bowser's Galaxy Generator: The Fate of the Universe":  create_location_data(),
    "Grand Finale Galaxy: The Star Festival":               create_location_data(),
}


loc_gateway_data = {
    "Gateway Galaxy: Grand Star Rescue":                    create_location_data(),
    "Gateway Galaxy: Gateway's Purple Coins":               create_location_data(),
    "Boo's Boneyard Galaxy: Racing the Spooky Speedster":   create_location_data(),
}

loc_misc_data = {
    "Luigi Rescue Access": create_location_data("Luigi Rescue Access"),
    "Comet Mission Access": create_location_data("Comet Mission Access"),
    "Purple Comet Access":  create_location_data("Purple Comet Access"),
}


location_data_table = {
    **loc_terrace_data,
    **loc_fountain_data,
    **loc_kitchen_data,
    **loc_bedroom_data,
    **loc_engineroom_data,
    **loc_garden_data,
    **loc_trials_data,
    **loc_special_data,
    **loc_gateway_data,
    **loc_misc_data
}

location_table = {name: data.code for name, data in location_data_table.items() if data.code is not None}


def get_locations_by_names(names: List[str]) -> Dict[str, int | None]:
    return {name: location_table[name] for name in names}


def create_all_locations(world: SMGWorld) -> None:
    create_regular_locations(world)
    create_event_locations(world)

def create_regular_locations(world: SMGWorld) -> None:
    observatory =   world.get_region("Comet Obervatory")
    terrace =       world.get_region("Terrace")
    fountain =      world.get_region("Fountain")
    kitchen =       world.get_region("Kitchen")
    bedroom =       world.get_region("Bedroom")
    engine_room =   world.get_region("Engine Room")
    garden =        world.get_region("Garden")

    trials =        world.get_region("Trial Galaxies")

    unassigned =    world.get_region("Unassigned")

    observatory.add_locations(get_locations_by_names([
        "Gateway Galaxy: Grand Star Rescue",
    ]), SMGLocation)

    terrace.add_locations(get_locations_by_names([
        "Good Egg Galaxy: Dino Piranha",
        "Good Egg Galaxy: A Snack of Cosmic Proportions",
        "Good Egg Galaxy: King Kaliente's Battle Fleet",
        "Good Egg Galaxy: Luigi on the Roof",
        "Honeyhive Galaxy: Bee Mario Takes Flight",
        "Honeyhive Galaxy: Trouble on the Tower",
        "Honeyhive Galaxy: Big Bad Bugaboom",
        "Honeyhive Galaxy: Luigi in the Honeyhive Kingdom",
        "Loopdeeloop Galaxy: Surfing 101",
        "Flipswitch Galaxy: Painting the Planet Yellow",
        "Bowser Jr's Robot Reactor: Megaleg's Moon",
    ]), SMGLocation)

    fountain.add_locations(get_locations_by_names([
        "Space Junk Galaxy: Pull Star Path",
        "Space Junk Galaxy: Kamella's Airship Attack",
        "Space Junk Galaxy: Tarantox's Tangled Web",
        "Space Junk Galaxy: Yoshi's Unexpected Appearance",
        "Battlerock Galaxy: Battlerock Barrage",
        "Battlerock Galaxy: Breaking into the Battlerock",
        "Battlerock Galaxy: Topmaniac and the Topman Tribe",
        "Battlerock Galaxy: Battlerock's Garbage Dump",
        "Rolling Green Galaxy: Rolling in the Clouds",
        "Hurry-Scurry Galaxy: Shrinking Satellite",
        "Bowser's Star Reactor: The Fiery Stronghold",
    ]), SMGLocation)

    kitchen.add_locations(get_locations_by_names([
        "Beach Bowl Galaxy: Sunken Treasure",
        "Beach Bowl Galaxy: Passing the Swim Test",
        "Beach Bowl Galaxy: Secret Undersea Cavern",
        "Beach Bowl Galaxy: Wall Jumping up Waterfalls",
        "Ghostly Galaxy: Luigi and the Haunted Mansion",
        "Ghostly Galaxy: A Very Spooky Sprint",
        "Ghostly Galaxy: Beware of Bouldergeist",
        "Ghostly Galaxy: Matter Splatter Mansion",
        "Buoy Base Galaxy: The Floating Fortress",
        "Bubble Breeze Galaxy: Through the Poison Swamp",
        "Bowser Jr's Airship Armada: Sinking the Airships",
    ]), SMGLocation)

    bedroom.add_locations(get_locations_by_names([
        "Gusty Garden Galaxy: Bunnies in the Wind",
        "Gusty Garden Galaxy: The Dirty Tricks of Major Burrows",
        "Gusty Garden Galaxy: Gusty Garden's Gravity Scramble",
        "Gusty Garden Galaxy: The Golden Chomp",
        "Freezeflame Galaxy: The Frozen Peak of Baron Brrr",
        "Freezeflame Galaxy: Freezeflame's Blistering Core",
        "Freezeflame Galaxy: Hot and Cold Collide",
        "Freezeflame Galaxy: Conquering the Summit",
        "Dusty Dune Galaxy: Soaring on the Desert Winds",
        "Dusty Dune Galaxy: Blasting through the Sand",
        "Dusty Dune Galaxy: Sunbaked Sand Castle",
        "Dusty Dune Galaxy: Bullet Bill on Your Back",
        "Honeyclimb Galaxy: Scaling the Sticky Wall",
        "Bowser's Dark Matter Plant: Darkness on the Horizon",
    ]), SMGLocation)

    engine_room.add_locations(get_locations_by_names([
        "Gold Leaf Galaxy: Star Bunnies on the Hunt",
        "Gold Leaf Galaxy: Cataquack to the Skies",
        "Gold Leaf Galaxy: When It Rains, It Pours",
        "Gold Leaf Galaxy: The Bell on the Big Tree",
        "Sea Slide Galaxy: Going After Guppy",
        "Sea Slide Galaxy: Faster Than a Speeding Penguin",
        "Sea Slide Galaxy: The Silver Stars of Sea Slide",
        "Sea Slide Galaxy: Hurry, He's Hungry",
        "Toy Time Galaxy: Heavy Metal Mecha-Bowser",
        "Toy Time Galaxy: Mario Meets Mario",
        "Toy Time Galaxy: Bouncing Down Cake Lane",
        "Toy Time Galaxy: The Flipswitch Chain",
        "Bonefin Galaxy: Kingfin's Fearsome Waters",
        "Bowser Jr's Lava Reactor: King Kaliente's Spicy Return",
    ]), SMGLocation)

    garden.add_locations(get_locations_by_names([
        "Deep Dark Galaxy: The Undergroud Ghost Ship",
        "Deep Dark Galaxy: Bubble Blastoff",
        "Deep Dark Galaxy: Guppy and the Underground Lake",
        "Deep Dark Galaxy: Boo in a Box",
        "Dreadnought Galaxy: Infiltrating the Dreadnought",
        "Dreadnought Galaxy: Dreadnought's Colossan Cannons",
        "Dreadnought Galaxy: Revenge of the Topman Tribe",
        "Dreadnought Galaxy: Dreadnought's Garbage Dump",
        "Melty Molten Galaxy: The Sinking Lava Spire",
        "Melty Molten Galaxy: Through the Meteor Storm",
        "Melty Molten Galaxy: Fiery Dino Piranha",
        "Melty Molten Galaxy: Burning Tide",
        "Matter Splatter Galaxy: Watch Your Step",
    ]), SMGLocation)

    trials.add_locations(get_locations_by_names([
        "Loopdeswoop Galaxy: The Galaxy's Greatest Wave",
        "Bubble Blast Galaxy: The Electric Labyrinth",
        "Rolling Gizmo Galaxy: Gizmo's, Gears, and Gadgets",
    ]), SMGLocation)
    fountain.add_locations(get_locations_by_names([
        "Battlerock Galaxy: Luigi under the Saucer",
        "Battlerock Galaxy: Green Star"
    ]), SMGLocation)
    kitchen.add_locations(get_locations_by_names([
        "Buoy Base Galaxy: Secret Buoy Base",
        "Buoy Base Galaxy: Green Star"
    ]), SMGLocation)
    bedroom.add_locations(get_locations_by_names([
        "Dusty Dune Galaxy: Treasure of the Pyramid",
        "Dusty Dune Galaxy: Green Star"
    ]), SMGLocation)


    # -- Hungry Lumas -- TO BE CHANGED
    terrace.add_locations(get_locations_by_names([
        "Sweet Sweet Galaxy: Rocky Road"
    ]), SMGLocation)
    fountain.add_locations(get_locations_by_names([
        "Sling Pod Galaxy: A Very Sticky Situation"
    ]), SMGLocation)
    kitchen.add_locations(get_locations_by_names([
        "Drip Drop Galaxy: Giant Eel Outbreak"
    ]), SMGLocation)
    bedroom.add_locations(get_locations_by_names([
        "Bigmouth Galaxy: Bigmouth's Gold Bait"
    ]), SMGLocation)
    engine_room.add_locations(get_locations_by_names([
        "Sand Spiral Galaxy: Chosing a Favorite Snack"
    ]), SMGLocation)
    garden.add_locations(get_locations_by_names([
        "Boo's Boneyard Galaxy: Racing the Spooky Speedster",
        "Snowcap Galaxy: Star Bunnies in the Snow"
    ]), SMGLocation)

    # -- Comet Missions -- Maybe Changed?
    terrace.add_locations(get_locations_by_names([
        "Good Egg Galaxy: Dino Piranha Speed Run",
        "Good Egg Galaxy: Purple Coin Omelet",
        "Honeyhive Galaxy: Honeyhive Cosmic Mario Race",
        "Honeyhive Galaxy: The Honeyhive's Purple Coins",
    ]), SMGLocation)
    fountain.add_locations(get_locations_by_names([
        "Space Junk Galaxy: Pull Star Path Speed Run",
        "Space Junk Galaxy: Purple Coin Spacewalk",
        "Battlerock Galaxy: Topmaniac's Daredevil Run",
        "Battlerock Galaxy: Purple Coins on the Battlerock",
    ]), SMGLocation)
    kitchen.add_locations(get_locations_by_names([
        "Beach Bowl Galaxy: Fast Foes on the Stone Cyclone",
        "Beach Bowl Galaxy: Beachcombing for Purple Coins",
        "Ghostly Galaxy: Bouldergeist's Daredevil Run",
        "Ghostly Galaxy: Purple Coins in the Bone Pen",
    ]), SMGLocation)
    bedroom.add_locations(get_locations_by_names([
        "Gusty Garden Galaxy: Major Burrows's Daredevil Run",
        "Gusty Garden Galaxy: Purple Coins on the Puzzle Cube",
        "Freezeflame Galaxy: Frosty Cosmic Mario Race",
        "Freezeflame Galaxy: Purple Coins on the Summit",
        "Dusty Dune Galaxy: Sandblast Speed Run",
        "Dusty Dune Galaxy: Purple Coins in the Desert",
    ]), SMGLocation)
    engine_room.add_locations(get_locations_by_names([
        "Gold Leaf Galaxy: Cosmic Mario Forest Race",
        "Gold Leaf Galaxy: Purple Coins in the Woods",
        "Sea Slide Galaxy: Underwater Cosmic Mario Race",
        "Sea Slide Galaxy: Purple Coins by the Seaside",
        "Toy Time Galaxy: Fast Foes of Toy Time",
        "Toy Time Galaxy: Luigi's Purple Coins",
    ]), SMGLocation)
    garden.add_locations(get_locations_by_names([
        "Deep Dark Galaxy: Ghost Ship Daredevil Run",
        "Deep Dark Galaxy: Plunder the Purple Coins",
        "Dreadnought Galaxy: Topman Tribe Speed Run",
        "Dreadnought Galaxy: Battlestation's Purple Coins",
        "Melty Molten Galaxy: Lava Spire Daredevil Run",
        "Melty Molten Galaxy: Red-Hot Purple Coins",
    ]), SMGLocation)

    # -- Bowser Stage Accesses
    terrace.add_locations(get_locations_by_names([
        "Bowser Jr's Robot Reactor: Access"
    ]), SMGLocation)
    fountain.add_locations(get_locations_by_names([
        "Bowser's Star Reactor: Access"
    ]), SMGLocation)
    kitchen.add_locations(get_locations_by_names([
        "Bowser Jr's Airship Armada: Access"
    ]), SMGLocation)
    bedroom.add_locations(get_locations_by_names([
        "Bowser's Dark Matter Plant: Access"
    ]), SMGLocation)
    engine_room.add_locations(get_locations_by_names([
        "Bowser Jr's Lava Reactor: Access"
    ]), SMGLocation)

    # Weird little guys
    unassigned.add_locations(get_locations_by_names([
        "Luigi Rescue Access",
        "Comet Mission Access",
        "Purple Comet Access",
    ]), SMGLocation)

    engine_room.add_locations(get_locations_by_names([
        "Bowser's Galaxy Generator: The Fate of the Universe"
    ]), SMGLocation)

    garden.add_locations(get_locations_by_names([
        "Gateway Galaxy: Gateway's Purple Coins"
    ]), SMGLocation)

    unassigned.add_locations(get_locations_by_names([
        "Grand Finale Galaxy: The Star Festival"
    ]), SMGLocation)


def create_event_locations(world: SMGWorld) -> None:
    unassigned = world.get_region("Unassigned")

    unassigned.add_event(
        "Final Bowser Defeated",
        "Any Percent Victory",
        location_type=SMGLocation,
        item_type=SMGItem
    )

    unassigned.add_event(
        "120 Star Bowser Defeated",
        "120 Star Victory",
        location_type=SMGLocation,
        item_type=SMGItem
    )

    unassigned.add_event(
        "242 Star Bowser Defeated",
        "242 Star Victory",
        location_type=SMGLocation,
        item_type=SMGItem
    )
