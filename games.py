# the content of the games database is taken from the textbook Concrete Abstractions: An
# Introduction to Computer Science Using Scheme, by Max Hailperin, Barbara Kaiser, and
# Karl Knight, Copyright (c) 1998 by the authors. Full text is available for free at
# http://www.gustavus.edu/+max/concrete-abstractions.html

# the Scheme file, Revision 1.3 as of 2005/12/20 14:09:37, has been reformated for
# Python. The original file is available as
# http://www.gustavus.edu/academics/mcs/max/concabs/code/games.scm

# list of tuples w/ following format (the first tuple in the list is also annotated):
# each tuple contains title, director, year and tags/actresses
# `[(title, director, year, [actress_one, actor_two, ...]), ...]`
from typing import List, Tuple

games_db: List[Tuple[str, str, int, List[str]]] = [
    (
        "fortnite",  # title
        "epic games",  # developer
        2017,  # year
        [
            "battle royale",
            "3D",
            "multiple players",
            "survival",
        ],  # tags/actresses
    ),
    (
        "mario kart 8 deluxe",
        "Nintendo",
        2017,
        [
            "racing",
            "power ups",
            "tracks",
            "multi player",
            "mario universe characters",
            "motorbikes and gliders",
        ],
    ),
    (
        "minecraft",
        "mojang studios",
        2009,
        [
            "block",
            "survival",
            "first person",
        ],
    ),
    (
        "call of duty modern warfare II",
        "activision",
        2022,
        [
            "3d",
            "first person",
            "shooter",
            "survival",
            "shooter",
        ],
    ),
    (
        "world of warcraft",
        "blizzard entertainment",
        2004,
        ["multiplayer", "roleplay", "fantasy", "avatar", "quests"],
    ),
    (
        "elden ring",
        "fromsoftware",
        2022,
        ["roleplaying", "worldbuilding", "fantasy", "weaponry", "action"],
    ),
    (
        "space invaders",
        "taito",
        1978,
        [
            "arcade",
            "retro",
            "survival",
            "pixels",
            "aliens"
        ],
    ),
    (
        "animal crossing",
        "nintendo",
        2001,
        [
            "animals",
            "social simulation",
            "interaction",
            "cozy",
        ],
    ),
    (
        "splatoon",
        "nintendo",
        2015,
        [
            "third person shooter",
            "competition",
            "race",
            "colorful",
        ],
    ),
    (
        "Valorant",
        "Riot Games",
        2020,
        [
            "Shooter",
            "FPS",
            "Tactical Shooter",
        ],
    ),
    ("super mario odyssey",
      "nintendo",
        2017,
        [
            "platformer", 
            "3d", 
            "adventure"]
    ),
    (
        "sonic the hedgehog",
        "sega",
        1991,
        [
            "2d",
            "arcade",
            "platformer",
        ],
    ),
    (
        "nintendogs",
        "nintendo",
        2005,
        [
            "2d", 
            "retro", 
            "chill",
        ]
    ),
    (
        "pacman",
        "namco",
        1980,
        [
            "2d",
            "arcade",
            "retro",
        ],
    ),
    (
        "grand theft auto 5",
        "rockstar",
        2013,
        [
            "shooter",
            "3d",
            "open world",
            "crime",
        ],
    ),
    (
        "red dead redemption 2",
        "rockstar",
        2018,
        [
            "open world",
            "shooter",
            "3d",
            "western",
            
        ],
    ),
    (
        "red dead redemption",
        "rockstar",
        2010,
        [
            "open world",
            "shooter",
            "3d",
            "western",
        ],
    )
]
