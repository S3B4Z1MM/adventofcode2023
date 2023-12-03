def is_game_possible(game, cube_counts):
    for subset in game[0]:
        for cube in subset.split(','):
            count, color = cube.strip().split(' ')
            if cube_counts[color] < int(count):
                return False
    return True

def find_possible_games(games, cube_counts):
    possible_games = []
    for game in games:
        game_id, *subsets = game.split(':')
        subsets = [subset.strip().split(';') for subset in subsets]
        if is_game_possible(subsets, cube_counts):
            possible_games.append(int(game_id.strip().split(' ')[-1]))
    return possible_games

# Cube configuration
cube_counts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# Find possible games
with open('day2/input.txt') as games_input:
    possible_games = find_possible_games(games_input, cube_counts)

# Calculate the sum of IDs of possible games
sum_of_ids = sum(possible_games)

print("Sum of IDs of possible games:", sum_of_ids)
