from dataclasses import dataclass

from Options import Toggle, OptionGroup, PerGameCommonOptions, Choice, DeathLink, Range


class EnableGatewayStar(Toggle):
    """Include Gateway Galaxy: Grand Star Rescue in the item pool."""
    display_name = "Randomize Gateway Galaxy's initial Star"

class EnableLuigiCampaign(Toggle):
    """Include all 120 Stars in Luigi's campaign, as well as the Grand Finale Galaxy"""
    display_name = "Randomize Luigi's Campaign"

class EnableLuigiRescue(Toggle):
    """Include access to Luigi's Rescue missions in logic."""
    display_name = "Randomize Luigi Rescue Missions"

class EnableCometAccess(Toggle):
    """Include access to Comet Missions in logic.
    Will also randomize access to Purple Comets if Purple Comets are enabled"""
    display_name = "Randomize Comet Access"

class EnablePurpleComets(Toggle):
    """Include Purple Comets in logic"""
    display_name = "Randomize Purple Comet Missions"

class AmountOfStars(Range):
    """How many stars exist.
    If there aren't enough locations to hold the given total, the total will be reduced."""
    display_name = "Total Power Stars"
    range_start = 60
    range_end = 120
    default = 120


class CompletionType(Choice):
    """Set goal for game completion"""
    display_name = "Completion Goal"
    option_Bowsers_Galaxy_Reactor = 0
    option_120_Stars = 1
    # option_242_Stars = 2

    default = option_Bowsers_Galaxy_Reactor

smg_option_groups = [
    OptionGroup("Logic Options", [
        AmountOfStars,
        EnableLuigiCampaign,
        EnableLuigiRescue,
        EnableCometAccess,
        EnablePurpleComets,
    ])
]


smg_option_presets = {
    "Standard": {
        "initial_gateway_rando": False,
        "luigi_game_rando": False,
        "luigi_rescue_rando": False,
        "comet_rando": False,
        "purple_comet_rando": False,
        "completion_type": 0
    },
    "Hard Mode": {
        "initial_gateway_rando": True,
        "luigi_rando": True,
        "comet_rando": True,
        "purple_comet_rando": True,
        "completion_type": 3
    }
}


@dataclass
class SMGOptions(PerGameCommonOptions):
    star_amount: AmountOfStars
    initial_gateway_rando: EnableGatewayStar
    luigi_game_rando: EnableLuigiCampaign
    luigi_rescue_rando: EnableLuigiRescue
    comet_rando: EnableCometAccess
    purple_comet_rando: EnablePurpleComets
    death_link: DeathLink
    completion_type: CompletionType

