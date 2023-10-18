# Important variables:
#     games_db: list of 4-tuples (imported from gamess.py)
#     pa_list: list of pattern-action pairs (queries)
#       pattern - strings with % and _ (not consecutive)
#       action  - return list of strings

# THINGS TO ASK THE games CHAT BOT:
# what gamess were made in _ (must be date, because we don't have location)
# what gamess were made between _ and _
# what gamess were made before _
# what gamess were made after _
# who directed %
# who was the publisher of %
# what gamess were directed by %
# who acted in %
# when was % made
# in what gamess did % appear
# bye

#  Include the games database, named games_db
from games import games_db
from match import match
from typing import List, Tuple, Callable, Any

# The projection functions, that give us access to certain parts of a "games" (a tuple)
def get_title(games: Tuple[str, str, int, List[str]]) -> str:
    return games[0]


def get_publisher(games: Tuple[str, str, int, List[str]]) -> str:
    return games[1]


def get_year(games: Tuple[str, str, int, List[str]]) -> int:
    return games[2]


def get_tags(games: Tuple[str, str, int, List[str]]) -> List[str]:
    return games[3]


# Below are a set of actions. Each takes a list argument and returns a list of answers
# according to the action and the argument. It is important that each function returns a
# list of the answer(s) and not just the answer itself.


def title_by_year(matches: List[str]) -> List[str]:
    """Finds all gamess made in the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of games titles made in the passed in year
    """
    results = []
    for games in games_db:
        if int(matches[0]) == get_year(games):
            results.append(get_title(games))
    return results
##hellooo


def title_by_year_range(matches: List[str]) -> List[str]:
    """Finds all gamess made in the passed in year range

    Args:
        matches - a list of 2 strings, the year beginning the range and the year ending
            the range. For example, to get gamess from 1991-1994 matches would look like
            this - ["1991", "1994"] Note that these years are passed as strings and
            should be converted to ints.

    Returns:
        a list of games titles made during those years, inclusive (meaning if you pass
        in ["1991", "1994"] you will get gamess made in 1991, 1992, 1993 & 1994)
    """
    results = []
    for games in games_db:
        if int(matches[0]) <= get_year(games) <= int(matches[1]):
            results.append(get_title(games))
    return results


def title_before_year(matches: List[str]) -> List[str]:
    """Finds all gamess made before the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of games titles made before the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any gamess made that year, only before)
    """
    results = []
    for games in games_db:
        if get_year(games) < int(matches[0]):
            results.append(get_title(games))
    return results



def title_after_year(matches: List[str]) -> List[str]:
    """Finds all gamess made after the passed in year

    Args:
        matches - a list of 1 string, just the year. Note that this year is passed as a
            string and should be converted to an int

    Returns:
        a list of games titles made after the passed in year, exclusive (meaning if you
        pass in 1992 you won't get any gamess made that year, only after)
    """
    results = []
    for games in games_db:
        if get_year(games) > int(matches[0]):
            results.append(get_title(games))
    return results


def publisher_by_title(matches: List[str]) -> List[str]:
    """Finds publisher of games based on title

    Args:
        matches - a list of 1 string, just the title

    Returns:
        a list of 1 string, the publisher of the games
    """
    results = []
    for games in games_db:
        
        if get_title(games) == (matches[0]):
            results.append(get_publisher(games))
    return results


def title_by_publisher(matches: List[str]) -> List[str]:
    """Finds gamess directed by the passed in publisher

    Args:
        matches - a list of 1 string, just the publisher

    Returns:
        a list of gamess titles directed by the passed in publisher
    """
    results = []
    for games in games_db:
        if get_publisher(games) == str(matches[0]):
            results.append(get_title(games))
    return results


def tags_by_title(matches: List[str]) -> List[str]:
    """Finds tags who acted in the passed in games title

    Args:
        matches - a list of 1 string, just the games title

    Returns:
        a list of tags who acted in the passed in title
    """
    results = []
    for games in games_db:
        if get_title(games) == (matches[0]):
            results=(get_tags(games))
    return results


def year_by_title(matches: List[str]) -> List[int]:
    """Finds year of passed in games title

    Args:
        matches - a list of 1 string, just the games title

    Returns:
        a list of one item (an int), the year that the games was made
    """
    results = []
    for games in games_db:
        if get_title(games) == str(matches[0]):
            results.append(get_year(games))
    return results


def title_by_tags(matches: List[str]) -> List[str]:
    """Finds titles of all gamess that the given actor was in

    Args:
        matches - a list of 1 string, just the actor

    Returns:
        a list of games titles that the actor acted in
    """
    results = []
    for games in games_db:
        if matches[0] in get_tags(games):
            results.append(get_title(games))
    return results


# dummy argument is ignored and doesn't matter
def bye_action(dummy: List[str]) -> None:
    raise KeyboardInterrupt


# The pattern-action list for the natural language query system A list of tuples of
# pattern and action It must be declared here, after all of the function definitions
pa_list: List[Tuple[List[str], Callable[[List[str]], List[Any]]]] = [
    (str.split("what games were made in _"), title_by_year),
    (str.split("what games were made between _ and _"), title_by_year_range),
    (str.split("what games were made before _"), title_before_year),
    (str.split("what games were made after _"), title_after_year),
    # note there are two valid patterns here two different ways to ask for the publisher
    # of a games
    (str.split("who published %"), publisher_by_title),
    (str.split("who was the publisher of %"), publisher_by_title),
    (str.split("what games were published by %"), title_by_publisher),
    (str.split("what tags does % have"), tags_by_title),
    (str.split("when was % released"), year_by_title),
    (str.split("what games involve %"), title_by_tags),
    (["bye"], bye_action),
]


def search_pa_list(src: List[str]) -> List[str]:
    """Takes source, finds matching pattern and calls corresponding action. If it finds
    a match but has no answers it returns ["No answers"]. If it finds no match it
    returns ["I don't understand"].

    Args:
        source - a phrase represented as a list of words (strings)

    Returns:
        a list of answers. Will be ["I don't understand"] if it finds no matches and
        ["No answers"] if it finds a match but no answers
    """
    for pat, act in pa_list:
        mat = match(pat, src)
        if mat is not None:
            answer = act(mat)
            return answer if answer else ["no answers"]
            
    return ["I don't understand"]

 ####hellooo]

def query_loop() -> None:
    """The simple query loop. The try/except structure is to catch Ctrl-C or Ctrl-D
    characters and exit gracefully.
    """
    print("Welcome to the games database!\n")
    while True:
        try:
            print()
            query = input("Your query? ").replace("?", "").lower().split()
            answers = search_pa_list(query)
            for ans in answers:
                print(ans)

        except (KeyboardInterrupt, EOFError):
            break

    print("\nSo long!\n")


# uncomment the following line once you've written all of your code and are ready to try
# it out. Before running the following line, you should make sure that your code passes
# the existing asserts.
query_loop()
