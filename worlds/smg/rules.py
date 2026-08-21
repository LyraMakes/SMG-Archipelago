from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import SMGWorld

from .items import ItemNames
from .regions import EntranceNames

from rule_builder.rules import Has, Rule


location_rules = [
    # Terrace
    ("Good Egg Galaxy: Dino Piranha",                           Has(ItemNames.POWER_STAR, 1)),
    ("Good Egg Galaxy: A Snack of Cosmic Proportions",          Has(ItemNames.POWER_STAR, 1)),
    ("Good Egg Galaxy: King Kaliente's Battle Fleet",           Has(ItemNames.POWER_STAR, 1)),
    ("Good Egg Galaxy: Luigi on the Roof",                      Has(ItemNames.POWER_STAR, 1)),

    ("Honeyhive Galaxy: Bee Mario Takes Flight",                Has(ItemNames.POWER_STAR, 3)),
    ("Honeyhive Galaxy: Trouble on the Tower",                  Has(ItemNames.POWER_STAR, 3)),
    ("Honeyhive Galaxy: Big Bad Bugaboom",                      Has(ItemNames.POWER_STAR, 3)),
    ("Honeyhive Galaxy: Luigi in the Honeyhive Kingdom",        Has(ItemNames.POWER_STAR, 3)),

    ("Loopdeeloop Galaxy: Surfing 101",                         Has(ItemNames.POWER_STAR, 5)),
    ("Flipswitch Galaxy: Painting the Planet Yellow",           Has(ItemNames.POWER_STAR, 7)),

    ("Bowser Jr's Robot Reactor: Megaleg's Moon",               Has(ItemNames.BJrRR_ACCESS)),

    # Fountain
    ("Space Junk Galaxy: Pull Star Path",                       Has(ItemNames.POWER_STAR, 9)),
    ("Space Junk Galaxy: Kamella's Airship Attack",             Has(ItemNames.POWER_STAR, 9)),
    ("Space Junk Galaxy: Tarantox's Tangled Web",               Has(ItemNames.POWER_STAR, 9)),
    ("Space Junk Galaxy: Yoshi's Unexpected Appearance",        Has(ItemNames.POWER_STAR, 9)),

    ("Battlerock Galaxy: Battlerock Barrage",                   Has(ItemNames.POWER_STAR, 12)),
    ("Battlerock Galaxy: Breaking into the Battlerock",         Has(ItemNames.POWER_STAR, 12)),
    ("Battlerock Galaxy: Topmaniac and the Topman Tribe",       Has(ItemNames.POWER_STAR, 12)),
    ("Battlerock Galaxy: Battlerock's Garbage Dump",            Has(ItemNames.POWER_STAR, 12)),

    ("Rolling Green Galaxy: Rolling in the Clouds",             Has(ItemNames.POWER_STAR, 11)),
    ("Hurry-Scurry Galaxy: Shrinking Satellite",                Has(ItemNames.POWER_STAR, 18)),

    ("Bowser's Star Reactor: The Fiery Stronghold",             Has(ItemNames.BSR_ACCESS)),

    # Kitchen
    ("Beach Bowl Galaxy: Sunken Treasure",                      Has(ItemNames.POWER_STAR, 16)),
    ("Beach Bowl Galaxy: Passing the Swim Test",                Has(ItemNames.POWER_STAR, 16)),
    ("Beach Bowl Galaxy: Secret Undersea Cavern",               Has(ItemNames.POWER_STAR, 16)),
    ("Beach Bowl Galaxy: Wall Jumping up Waterfalls",           Has(ItemNames.POWER_STAR, 16)),

    ("Ghostly Galaxy: Luigi and the Haunted Mansion",           Has(ItemNames.POWER_STAR, 20)),
    ("Ghostly Galaxy: A Very Spooky Sprint",                    Has(ItemNames.POWER_STAR, 20)),
    ("Ghostly Galaxy: Beware of Bouldergeist",                  Has(ItemNames.POWER_STAR, 20)),
    ("Ghostly Galaxy: Matter Splatter Mansion",                 Has(ItemNames.POWER_STAR, 20)),

    ("Buoy Base Galaxy: The Floating Fortress",                 Has(ItemNames.POWER_STAR, 30)),
    ("Bubble Breeze Galaxy: Through the Poison Swamp",          Has(ItemNames.POWER_STAR, 19)),

    ("Bowser Jr's Airship Armada: Sinking the Airships",        Has(ItemNames.BJrAA_ACCESS)),

    # Bedroom
    ("Gusty Garden Galaxy: Bunnies in the Wind",                Has(ItemNames.POWER_STAR, 24)),
    ("Gusty Garden Galaxy: The Dirty Tricks of Major Burrows",  Has(ItemNames.POWER_STAR, 24)),
    ("Gusty Garden Galaxy: Gusty Garden's Gravity Scramble",    Has(ItemNames.POWER_STAR, 24)),
    ("Gusty Garden Galaxy: The Golden Chomp",                   Has(ItemNames.POWER_STAR, 24)),

    ("Freezeflame Galaxy: The Frozen Peak of Baron Brrr",       Has(ItemNames.POWER_STAR, 26)),
    ("Freezeflame Galaxy: Freezeflame's Blistering Core",       Has(ItemNames.POWER_STAR, 26)),
    ("Freezeflame Galaxy: Hot and Cold Collide",                Has(ItemNames.POWER_STAR, 26)),
    ("Freezeflame Galaxy: Conquering the Summit",               Has(ItemNames.POWER_STAR, 26)),

    ("Dusty Dune Galaxy: Soaring on the Desert Winds",          Has(ItemNames.POWER_STAR, 29)),
    ("Dusty Dune Galaxy: Blasting through the Sand",            Has(ItemNames.POWER_STAR, 29)),
    ("Dusty Dune Galaxy: Sunbaked Sand Castle",                 Has(ItemNames.POWER_STAR, 29)),
    ("Dusty Dune Galaxy: Bullet Bill on Your Back",             Has(ItemNames.POWER_STAR, 29)),

    ("Honeyclimb Galaxy: Scaling the Sticky Wall",              Has(ItemNames.POWER_STAR, 42)),

    ("Bowser's Dark Matter Plant: Darkness on the Horizon",     Has(ItemNames.BDMP_ACCESS)),

    # Engine Room
    ("Gold Leaf Galaxy: Star Bunnies on the Hunt",              Has(ItemNames.POWER_STAR, 34)),
    ("Gold Leaf Galaxy: Cataquack to the Skies",                Has(ItemNames.POWER_STAR, 34)),
    ("Gold Leaf Galaxy: When It Rains, It Pours",               Has(ItemNames.POWER_STAR, 34)),
    ("Gold Leaf Galaxy: The Bell on the Big Tree",              Has(ItemNames.POWER_STAR, 34)),

    ("Sea Slide Galaxy: Going After Guppy",                     Has(ItemNames.POWER_STAR, 36)),
    ("Sea Slide Galaxy: Faster Than a Speeding Penguin",        Has(ItemNames.POWER_STAR, 36)),
    ("Sea Slide Galaxy: The Silver Stars of Sea Slide",         Has(ItemNames.POWER_STAR, 36)),
    ("Sea Slide Galaxy: Hurry, He's Hungry",                    Has(ItemNames.POWER_STAR, 36)),

    ("Toy Time Galaxy: Heavy Metal Mecha-Bowser",               Has(ItemNames.POWER_STAR, 40)),
    ("Toy Time Galaxy: Mario Meets Mario",                      Has(ItemNames.POWER_STAR, 40)),
    ("Toy Time Galaxy: Bouncing Down Cake Lane",                Has(ItemNames.POWER_STAR, 40)),
    ("Toy Time Galaxy: The Flipswitch Chain",                   Has(ItemNames.POWER_STAR, 40)),

    ("Bonefin Galaxy: Kingfin's Fearsome Waters",               Has(ItemNames.POWER_STAR, 55)),

    ("Bowser Jr's Lava Reactor: King Kaliente's Spicy Return",  Has(ItemNames.BJrLR_ACCESS)),

    # Garden
    ("Deep Dark Galaxy: The Undergroud Ghost Ship",             Has(ItemNames.POWER_STAR, 46)),
    ("Deep Dark Galaxy: Bubble Blastoff",                       Has(ItemNames.POWER_STAR, 46)),
    ("Deep Dark Galaxy: Guppy and the Underground Lake",        Has(ItemNames.POWER_STAR, 46)),
    ("Deep Dark Galaxy: Boo in a Box",                          Has(ItemNames.POWER_STAR, 46)),

    ("Dreadnought Galaxy: Infiltrating the Dreadnought",        Has(ItemNames.POWER_STAR, 48)),
    ("Dreadnought Galaxy: Dreadnought's Colossan Cannons",      Has(ItemNames.POWER_STAR, 48)),
    ("Dreadnought Galaxy: Revenge of the Topman Tribe",         Has(ItemNames.POWER_STAR, 48)),
    ("Dreadnought Galaxy: Dreadnought's Garbage Dump",          Has(ItemNames.POWER_STAR, 48)),

    ("Melty Molten Galaxy: The Sinking Lava Spire",             Has(ItemNames.POWER_STAR, 52)),
    ("Melty Molten Galaxy: Through the Meteor Storm",           Has(ItemNames.POWER_STAR, 52)),
    ("Melty Molten Galaxy: Fiery Dino Piranha",                 Has(ItemNames.POWER_STAR, 52)),
    ("Melty Molten Galaxy: Burning Tide",                       Has(ItemNames.POWER_STAR, 52)),

    ("Matter Splatter Galaxy: Watch Your Step",                 Has(ItemNames.POWER_STAR, 50)),


    # Trial Galaxies
    ("Loopdeswoop Galaxy: The Galaxy's Greatest Wave",          Has(ItemNames.GREEN_STAR, 3)),
    ("Bubble Blast Galaxy: The Electric Labyrinth",             Has(ItemNames.GREEN_STAR, 3)),
    ("Rolling Gizmo Galaxy: Gizmo's, Gears, and Gadgets",       Has(ItemNames.GREEN_STAR, 3)),

    ("Gateway Galaxy: Gateway's Purple Coins",                  Has(ItemNames.BJrLR_ACCESS)),

    # Green Stars
    ("Buoy Base Galaxy: Secret Buoy Base",                      Has(ItemNames.POWER_STAR, 30)),
    ("Buoy Base Galaxy: Green Star",                            Has(ItemNames.POWER_STAR, 30)),
    ("Dusty Dune Galaxy: Treasure of the Pyramid",              Has(ItemNames.POWER_STAR, 29)),
    ("Dusty Dune Galaxy: Green Star",                           Has(ItemNames.POWER_STAR, 29)),
    ("Battlerock Galaxy: Luigi under the Saucer",               Has(ItemNames.POWER_STAR, 20) & Has(ItemNames.BJrAA_ACCESS)),
    ("Battlerock Galaxy: Green Star",                           Has(ItemNames.POWER_STAR, 20) & Has(ItemNames.BJrAA_ACCESS)),

    # -- Hungry Lumas -- Might change????
    ("Sweet Sweet Galaxy: Rocky Road",                          Has(ItemNames.POWER_STAR,  3)), # Honeyhive Galaxy
    ("Sling Pod Galaxy: A Very Sticky Situation",               Has(ItemNames.POWER_STAR,  9)), # Space Junk Galaxy
    ("Drip Drop Galaxy: Giant Eel Outbreak",                    Has(ItemNames.POWER_STAR, 16)), # Beach Bowl Galaxy
    ("Bigmouth Galaxy: Bigmouth's Gold Bait",                   Has(ItemNames.POWER_STAR, 29)), # Dusty Dune Galaxy
    ("Boo's Boneyard Galaxy: Racing the Spooky Speedster",      Has(ItemNames.BJrLR_ACCESS  )), # Gateway Galaxy  
    ("Sand Spiral Galaxy: Chosing a Favorite Snack",            Has(ItemNames.POWER_STAR, 36)), # Sea Slide Galaxy
    ("Snowcap Galaxy: Star Bunnies in the Snow",                Has(ItemNames.POWER_STAR, 52)), # Melty Molten Galaxy

    ("Bowser Jr's Robot Reactor: Access",                       Has(ItemNames.POWER_STAR,  8)),
    ("Bowser's Star Reactor: Access",                           Has(ItemNames.POWER_STAR, 15)),
    ("Bowser Jr's Airship Armada: Access",                      Has(ItemNames.POWER_STAR, 23)),
    ("Bowser's Dark Matter Plant: Access",                      Has(ItemNames.POWER_STAR, 33)),
    ("Bowser Jr's Lava Reactor: Access",                        Has(ItemNames.POWER_STAR, 45)),

    ("Good Egg Galaxy: Dino Piranha Speed Run",                 Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 1)),
    ("Honeyhive Galaxy: Honeyhive Cosmic Mario Race",           Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 3)),
    ("Space Junk Galaxy: Pull Star Path Speed Run",             Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 9)),
    ("Battlerock Galaxy: Topmaniac's Daredevil Run",            Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 12)),
    ("Beach Bowl Galaxy: Fast Foes on the Stone Cyclone",       Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 16)),
    ("Ghostly Galaxy: Bouldergeist's Daredevil Run",            Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 20)),
    ("Gusty Garden Galaxy: Major Burrows's Daredevil Run",      Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 24)),
    ("Freezeflame Galaxy: Frosty Cosmic Mario Race",            Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 26)),
    ("Dusty Dune Galaxy: Sandblast Speed Run",                  Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 29)),
    ("Gold Leaf Galaxy: Cosmic Mario Forest Race",              Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 34)),
    ("Sea Slide Galaxy: Underwater Cosmic Mario Race",          Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 36)),
    ("Toy Time Galaxy: Fast Foes of Toy Time",                  Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 40)),
    ("Deep Dark Galaxy: Ghost Ship Daredevil Run",              Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 46)),
    ("Dreadnought Galaxy: Topman Tribe Speed Run",              Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 48)),
    ("Melty Molten Galaxy: Lava Spire Daredevil Run",           Has(ItemNames.COMET_ACCESS) & Has(ItemNames.POWER_STAR, 52)),

    ("Good Egg Galaxy: Purple Coin Omelet",                     Has(ItemNames.BDMP_ACCESS) & Has(ItemNames.POWER_STAR, 60)),
    ("Honeyhive Galaxy: The Honeyhive's Purple Coins",          Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 3)),
    ("Space Junk Galaxy: Purple Coin Spacewalk",                Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 9)),
    ("Battlerock Galaxy: Purple Coins on the Battlerock",       Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 12)),
    ("Beach Bowl Galaxy: Beachcombing for Purple Coins",        Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 16)),
    ("Ghostly Galaxy: Purple Coins in the Bone Pen",            Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 20)),
    ("Gusty Garden Galaxy: Purple Coins on the Puzzle Cube",    Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 24)),
    ("Freezeflame Galaxy: Purple Coins on the Summit",          Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 26)),
    ("Dusty Dune Galaxy: Purple Coins in the Desert",           Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 29)),
    ("Gold Leaf Galaxy: Purple Coins in the Woods",             Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 34)),
    ("Sea Slide Galaxy: Purple Coins by the Seaside",           Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 36)),
    ("Toy Time Galaxy: Luigi's Purple Coins",                   Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 40)),
    ("Deep Dark Galaxy: Plunder the Purple Coins",              Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 46)),
    ("Dreadnought Galaxy: Battlestation's Purple Coins",        Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 48)),
    ("Melty Molten Galaxy: Red-Hot Purple Coins",               Has(ItemNames.PURPLE_ACCESS) & Has(ItemNames.POWER_STAR, 52)),


    ("Bowser's Galaxy Generator: The Fate of the Universe",     Has(ItemNames.POWER_STAR, 60)),
    ("Grand Finale Galaxy: The Star Festival",                  Has(ItemNames.BDMP_ACCESS) & Has(ItemNames.POWER_STAR, 120)),

    ("Luigi Rescue Access",                                     Has(ItemNames.POWER_STAR, 20)),
    ("Comet Mission Access",                                    Has(ItemNames.POWER_STAR, 13)),
    ("Purple Comet Access",                                     Has(ItemNames.COMET_ACCESS) & Has(ItemNames.BDMP_ACCESS) & Has(ItemNames.POWER_STAR, 60)),

    # ("Gateway Galaxy: Grand Star Rescue",                       ), # - Opening Mission, No rule
]




def set_all_rules(world: SMGWorld) -> None:

    # Entrance Rules
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_TERRACE),       Has(ItemNames.POWER_STAR, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_FOUNTAIN),      Has(ItemNames.BJrRR_ACCESS, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_KITCHEN),       Has(ItemNames.BSR_ACCESS, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_BEDROOM),       Has(ItemNames.BJrAA_ACCESS, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_ENGINE_ROOM),   Has(ItemNames.BDMP_ACCESS, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_GARDEN),        Has(ItemNames.BJrLR_ACCESS, 1))
    world.set_rule(world.get_entrance(EntranceNames.OBSERVATORY_TRIALS),        Has(ItemNames.GREEN_STAR, 3))
    
    # Location Rules

    for (location, rule) in location_rules:
        world.set_rule(world.get_location(location), rule)

    # Event Rules
    world.set_rule(world.get_location("Final Bowser Defeated"), Has(ItemNames.POWER_STAR, 60))
    world.set_rule(world.get_location("120 Star Bowser Defeated"), Has(ItemNames.POWER_STAR, 120))
    world.set_rule(world.get_location("242 Star Bowser Defeated"), Has(ItemNames.POWER_STAR, 242))

    # Completion Condition

    if world.options.completion_type == 1:
        world.set_completion_rule(Has("120 Star Victory"))
    elif world.options.completion_type == 2:
        world.set_completion_rule(Has("242 Star Victory"))
    else:
        world.set_completion_rule(Has("Any Percent Victory"))




