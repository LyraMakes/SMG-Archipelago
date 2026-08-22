from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import SMGWorld

from rule_builder.rules import Has

location_rules = [
    # Terrace
    ("Good Egg Galaxy: Dino Piranha",                           Has("Power_Star", 1)),
    ("Good Egg Galaxy: A Snack of Cosmic Proportions",          Has("Power_Star", 1)),
    ("Good Egg Galaxy: King Kaliente's Battle Fleet",           Has("Power_Star", 1)),
    ("Good Egg Galaxy: Luigi on the Roof",                      Has("Power_Star", 1) & Has("Luigi Rescue Access")),

    ("Honeyhive Galaxy: Bee Mario Takes Flight",                Has("Power_Star", 3)),
    ("Honeyhive Galaxy: Trouble on the Tower",                  Has("Power_Star", 3)),
    ("Honeyhive Galaxy: Big Bad Bugaboom",                      Has("Power_Star", 3)),
    ("Honeyhive Galaxy: Luigi in the Honeyhive Kingdom",        Has("Power_Star", 3) & Has("Luigi Rescue Access")),

    ("Loopdeeloop Galaxy: Surfing 101",                         Has("Power_Star", 5)),
    ("Flipswitch Galaxy: Painting the Planet Yellow",           Has("Power_Star", 7)),

    ("Bowser Jr's Robot Reactor: Megaleg's Moon",               Has("Bowser Jr's Robot Reactor: Access")),

    # Fountain
    ("Space Junk Galaxy: Pull Star Path",                       Has("Power_Star", 9)),
    ("Space Junk Galaxy: Kamella's Airship Attack",             Has("Power_Star", 9)),
    ("Space Junk Galaxy: Tarantox's Tangled Web",               Has("Power_Star", 9)),
    ("Space Junk Galaxy: Yoshi's Unexpected Appearance",        Has("Power_Star", 9)),

    ("Battlerock Galaxy: Battlerock Barrage",                   Has("Power_Star", 12)),
    ("Battlerock Galaxy: Breaking into the Battlerock",         Has("Power_Star", 12)),
    ("Battlerock Galaxy: Topmaniac and the Topman Tribe",       Has("Power_Star", 12)),
    ("Battlerock Galaxy: Battlerock's Garbage Dump",            Has("Power_Star", 12)),

    ("Rolling Green Galaxy: Rolling in the Clouds",             Has("Power_Star", 11)),
    ("Hurry-Scurry Galaxy: Shrinking Satellite",                Has("Power_Star", 18)),

    ("Bowser's Star Reactor: The Fiery Stronghold",             Has("Bowser's Star Reactor: Access")),

    # Kitchen
    ("Beach Bowl Galaxy: Sunken Treasure",                      Has("Power_Star", 16)),
    ("Beach Bowl Galaxy: Passing the Swim Test",                Has("Power_Star", 16)),
    ("Beach Bowl Galaxy: Secret Undersea Cavern",               Has("Power_Star", 16)),
    ("Beach Bowl Galaxy: Wall Jumping up Waterfalls",           Has("Power_Star", 16)),

    ("Ghostly Galaxy: Luigi and the Haunted Mansion",           Has("Power_Star", 20)),
    ("Ghostly Galaxy: A Very Spooky Sprint",                    Has("Power_Star", 20)),
    ("Ghostly Galaxy: Beware of Bouldergeist",                  Has("Power_Star", 20)),
    ("Ghostly Galaxy: Matter Splatter Mansion",                 Has("Power_Star", 20)),

    ("Buoy Base Galaxy: The Floating Fortress",                 Has("Power_Star", 30)),
    ("Bubble Breeze Galaxy: Through the Poison Swamp",          Has("Power_Star", 19)),

    ("Bowser Jr's Airship Armada: Sinking the Airships",        Has("Bowser Jr's Airship Armada: Access")),

    # Bedroom
    ("Gusty Garden Galaxy: Bunnies in the Wind",                Has("Power_Star", 24)),
    ("Gusty Garden Galaxy: The Dirty Tricks of Major Burrows",  Has("Power_Star", 24)),
    ("Gusty Garden Galaxy: Gusty Garden's Gravity Scramble",    Has("Power_Star", 24)),
    ("Gusty Garden Galaxy: The Golden Chomp",                   Has("Power_Star", 24)),

    ("Freezeflame Galaxy: The Frozen Peak of Baron Brrr",       Has("Power_Star", 26)),
    ("Freezeflame Galaxy: Freezeflame's Blistering Core",       Has("Power_Star", 26)),
    ("Freezeflame Galaxy: Hot and Cold Collide",                Has("Power_Star", 26)),
    ("Freezeflame Galaxy: Conquering the Summit",               Has("Power_Star", 26)),

    ("Dusty Dune Galaxy: Soaring on the Desert Winds",          Has("Power_Star", 29)),
    ("Dusty Dune Galaxy: Blasting through the Sand",            Has("Power_Star", 29)),
    ("Dusty Dune Galaxy: Sunbaked Sand Castle",                 Has("Power_Star", 29)),
    ("Dusty Dune Galaxy: Bullet Bill on Your Back",             Has("Power_Star", 29)),

    ("Honeyclimb Galaxy: Scaling the Sticky Wall",              Has("Power_Star", 42)),

    ("Bowser's Dark Matter Plant: Darkness on the Horizon",     Has("Bowser's Dark Matter Plant: Access")),

    # Engine Room
    ("Gold Leaf Galaxy: Star Bunnies on the Hunt",              Has("Power_Star", 34)),
    ("Gold Leaf Galaxy: Cataquack to the Skies",                Has("Power_Star", 34)),
    ("Gold Leaf Galaxy: When It Rains, It Pours",               Has("Power_Star", 34)),
    ("Gold Leaf Galaxy: The Bell on the Big Tree",              Has("Power_Star", 34)),

    ("Sea Slide Galaxy: Going After Guppy",                     Has("Power_Star", 36)),
    ("Sea Slide Galaxy: Faster Than a Speeding Penguin",        Has("Power_Star", 36)),
    ("Sea Slide Galaxy: The Silver Stars of Sea Slide",         Has("Power_Star", 36)),
    ("Sea Slide Galaxy: Hurry, He's Hungry",                    Has("Power_Star", 36)),

    ("Toy Time Galaxy: Heavy Metal Mecha-Bowser",               Has("Power_Star", 40)),
    ("Toy Time Galaxy: Mario Meets Mario",                      Has("Power_Star", 40)),
    ("Toy Time Galaxy: Bouncing Down Cake Lane",                Has("Power_Star", 40)),
    ("Toy Time Galaxy: The Flipswitch Chain",                   Has("Power_Star", 40)),

    ("Bonefin Galaxy: Kingfin's Fearsome Waters",               Has("Power_Star", 55)),

    ("Bowser Jr's Lava Reactor: King Kaliente's Spicy Return",  Has("Bowser Jr's Lava Reactor: Access")),

    # Garden
    ("Deep Dark Galaxy: The Undergroud Ghost Ship",             Has("Power_Star", 46)),
    ("Deep Dark Galaxy: Bubble Blastoff",                       Has("Power_Star", 46)),
    ("Deep Dark Galaxy: Guppy and the Underground Lake",        Has("Power_Star", 46)),
    ("Deep Dark Galaxy: Boo in a Box",                          Has("Power_Star", 46)),

    ("Dreadnought Galaxy: Infiltrating the Dreadnought",        Has("Power_Star", 48)),
    ("Dreadnought Galaxy: Dreadnought's Colossan Cannons",      Has("Power_Star", 48)),
    ("Dreadnought Galaxy: Revenge of the Topman Tribe",         Has("Power_Star", 48)),
    ("Dreadnought Galaxy: Dreadnought's Garbage Dump",          Has("Power_Star", 48)),

    ("Melty Molten Galaxy: The Sinking Lava Spire",             Has("Power_Star", 52)),
    ("Melty Molten Galaxy: Through the Meteor Storm",           Has("Power_Star", 52)),
    ("Melty Molten Galaxy: Fiery Dino Piranha",                 Has("Power_Star", 52)),
    ("Melty Molten Galaxy: Burning Tide",                       Has("Power_Star", 52)),

    ("Matter Splatter Galaxy: Watch Your Step",                 Has("Power_Star", 50)),


    # Trial Galaxies
    ("Loopdeswoop Galaxy: The Galaxy's Greatest Wave",          Has("Green_Star", 3)),
    ("Bubble Blast Galaxy: The Electric Labyrinth",             Has("Green_Star", 3)),
    ("Rolling Gizmo Galaxy: Gizmo's, Gears, and Gadgets",       Has("Green_Star", 3)),

    ("Gateway Galaxy: Gateway's Purple Coins",                  Has("Bowser Jr's Lava Reactor: Access")),

    # Green Stars
    ("Buoy Base Galaxy: Secret Buoy Base",                      Has("Power_Star", 30)),
    ("Buoy Base Galaxy: Green Star",                            Has("Power_Star", 30)),
    ("Dusty Dune Galaxy: Treasure of the Pyramid",              Has("Power_Star", 29)),
    ("Dusty Dune Galaxy: Green Star",                           Has("Power_Star", 29)),
    ("Battlerock Galaxy: Luigi under the Saucer",               Has("Power_Star", 20) & Has("Luigi Rescue Access")),
    ("Battlerock Galaxy: Green Star",                           Has("Power_Star", 20) & Has("Luigi Rescue Access")),

    # -- Hungry Lumas -- Might change????
    ("Sweet Sweet Galaxy: Rocky Road",                          Has("Power_Star",  3)), # Honeyhive Galaxy
    ("Sling Pod Galaxy: A Very Sticky Situation",               Has("Power_Star",  9)), # Space Junk Galaxy
    ("Drip Drop Galaxy: Giant Eel Outbreak",                    Has("Power_Star", 16)), # Beach Bowl Galaxy
    ("Bigmouth Galaxy: Bigmouth's Gold Bait",                   Has("Power_Star", 29)), # Dusty Dune Galaxy
    ("Boo's Boneyard Galaxy: Racing the Spooky Speedster",      Has("Bowser Jr's Lava Reactor: Access"  )), # Gateway Galaxy  
    ("Sand Spiral Galaxy: Chosing a Favorite Snack",            Has("Power_Star", 36)), # Sea Slide Galaxy
    ("Snowcap Galaxy: Star Bunnies in the Snow",                Has("Power_Star", 52)), # Melty Molten Galaxy

    ("Bowser Jr's Robot Reactor: Access",                       Has("Power_Star",  8)),
    ("Bowser's Star Reactor: Access",                           Has("Power_Star", 15)),
    ("Bowser Jr's Airship Armada: Access",                      Has("Power_Star", 23)),
    ("Bowser's Dark Matter Plant: Access",                      Has("Power_Star", 33)),
    ("Bowser Jr's Lava Reactor: Access",                        Has("Power_Star", 45)),

    ("Good Egg Galaxy: Dino Piranha Speed Run",                 Has("Comet Mission Access") & Has("Power_Star", 1)),
    ("Honeyhive Galaxy: Honeyhive Cosmic Mario Race",           Has("Comet Mission Access") & Has("Power_Star", 3)),
    ("Space Junk Galaxy: Pull Star Path Speed Run",             Has("Comet Mission Access") & Has("Power_Star", 9)),
    ("Battlerock Galaxy: Topmaniac's Daredevil Run",            Has("Comet Mission Access") & Has("Power_Star", 12)),
    ("Beach Bowl Galaxy: Fast Foes on the Stone Cyclone",       Has("Comet Mission Access") & Has("Power_Star", 16)),
    ("Ghostly Galaxy: Bouldergeist's Daredevil Run",            Has("Comet Mission Access") & Has("Power_Star", 20)),
    ("Gusty Garden Galaxy: Major Burrows's Daredevil Run",      Has("Comet Mission Access") & Has("Power_Star", 24)),
    ("Freezeflame Galaxy: Frosty Cosmic Mario Race",            Has("Comet Mission Access") & Has("Power_Star", 26)),
    ("Dusty Dune Galaxy: Sandblast Speed Run",                  Has("Comet Mission Access") & Has("Power_Star", 29)),
    ("Gold Leaf Galaxy: Cosmic Mario Forest Race",              Has("Comet Mission Access") & Has("Power_Star", 34)),
    ("Sea Slide Galaxy: Underwater Cosmic Mario Race",          Has("Comet Mission Access") & Has("Power_Star", 36)),
    ("Toy Time Galaxy: Fast Foes of Toy Time",                  Has("Comet Mission Access") & Has("Power_Star", 40)),
    ("Deep Dark Galaxy: Ghost Ship Daredevil Run",              Has("Comet Mission Access") & Has("Power_Star", 46)),
    ("Dreadnought Galaxy: Topman Tribe Speed Run",              Has("Comet Mission Access") & Has("Power_Star", 48)),
    ("Melty Molten Galaxy: Lava Spire Daredevil Run",           Has("Comet Mission Access") & Has("Power_Star", 52)),

    ("Good Egg Galaxy: Purple Coin Omelet",                     Has("Bowser's Dark Matter Plant: Access") & Has("Power_Star", 60)),
    ("Honeyhive Galaxy: The Honeyhive's Purple Coins",          Has("Purple Comet Access") & Has("Power_Star", 3)),
    ("Space Junk Galaxy: Purple Coin Spacewalk",                Has("Purple Comet Access") & Has("Power_Star", 9)),
    ("Battlerock Galaxy: Purple Coins on the Battlerock",       Has("Purple Comet Access") & Has("Power_Star", 12)),
    ("Beach Bowl Galaxy: Beachcombing for Purple Coins",        Has("Purple Comet Access") & Has("Power_Star", 16)),
    ("Ghostly Galaxy: Purple Coins in the Bone Pen",            Has("Purple Comet Access") & Has("Power_Star", 20)),
    ("Gusty Garden Galaxy: Purple Coins on the Puzzle Cube",    Has("Purple Comet Access") & Has("Power_Star", 24)),
    ("Freezeflame Galaxy: Purple Coins on the Summit",          Has("Purple Comet Access") & Has("Power_Star", 26)),
    ("Dusty Dune Galaxy: Purple Coins in the Desert",           Has("Purple Comet Access") & Has("Power_Star", 29)),
    ("Gold Leaf Galaxy: Purple Coins in the Woods",             Has("Purple Comet Access") & Has("Power_Star", 34)),
    ("Sea Slide Galaxy: Purple Coins by the Seaside",           Has("Purple Comet Access") & Has("Power_Star", 36)),
    ("Toy Time Galaxy: Luigi's Purple Coins",                   Has("Purple Comet Access") & Has("Power_Star", 40)),
    ("Deep Dark Galaxy: Plunder the Purple Coins",              Has("Purple Comet Access") & Has("Power_Star", 46)),
    ("Dreadnought Galaxy: Battlestation's Purple Coins",        Has("Purple Comet Access") & Has("Power_Star", 48)),
    ("Melty Molten Galaxy: Red-Hot Purple Coins",               Has("Purple Comet Access") & Has("Power_Star", 52)),


    ("Bowser's Galaxy Generator: The Fate of the Universe",     Has("Power_Star", 60)),
    # ("Grand Finale Galaxy: The Star Festival",                  Has("Bowser's Dark Matter Plant: Access") & Has("Power_Star", 120)),

    ("Luigi Rescue Access",                                     Has("Power_Star", 20) & Has("Bowser's Star Reactor: Access")),
    ("Comet Mission Access",                                    Has("Power_Star", 13)),
    ("Purple Comet Access",                                     Has("Comet Mission Access") & Has("Bowser's Dark Matter Plant: Access") & Has("Power_Star", 60)),

    # ("Gateway Galaxy: Grand Star Rescue",                       ), # - Opening Mission, No rule
]




def set_all_rules(world: SMGWorld) -> None:

    # Entrance Rules
    world.set_rule(world.get_entrance("Observatory to Terrace"),        Has("Power_Star", 1))
    world.set_rule(world.get_entrance("Observatory to Fountain"),       Has("Bowser Jr's Robot Reactor: Access", 1))
    world.set_rule(world.get_entrance("Observatory to Kitchen"),        Has("Bowser's Star Reactor: Access", 1))
    world.set_rule(world.get_entrance("Observatory to Bedroom"),        Has("Bowser Jr's Airship Armada: Access", 1))
    world.set_rule(world.get_entrance("Observatory to Engine Room"),    Has("Bowser's Dark Matter Plant: Access", 1))
    world.set_rule(world.get_entrance("Observatory to Garden"),         Has("Bowser Jr's Lava Reactor: Access", 1))
    world.set_rule(world.get_entrance("Observatory to Trial Galaxies"), Has("Green_Star", 3))
    
    # Location Rules

    for (location, rule) in location_rules:
        world.set_rule(world.get_location(location), rule)

    # Event Rules
    world.set_rule(world.get_location("Final Bowser Defeated"   ), Has("Power_Star", 60))
    world.set_rule(world.get_location("120 Star Bowser Defeated"), Has("Power_Star", 120))
    # world.set_rule(world.get_location("242 Star Bowser Defeated"), Has("Power_Star", 242))

    # Completion Condition

    if world.options.completion_type == 1:
        world.set_completion_rule(Has("120 Star Victory"))
    # elif world.options.completion_type == 2:
    #     world.set_completion_rule(Has("242 Star Victory"))
    else:
        world.set_completion_rule(Has("Any Percent Victory"))




