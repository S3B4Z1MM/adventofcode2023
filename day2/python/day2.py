import re

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

def calculate_power_of_min_set_of_cubes(games):
    min_sets = []
    for game in games:
        product = 1
        min_set = {"red":0,"green":0,"blue":0}
        subsets = game.split(':')[-1]
        # Use re.split() to split using both ',' and ';'
        colors = re.split(r'[,;]', subsets)

        # Filter out empty strings and trim whitespace
        colors = [color.strip() for color in colors if color.strip()]
        
        for color in colors:
            cube, color = color.split()
            cube = int(cube)
            if (min_set.get(color) > cube):
                continue
            
            min_set.update({color: cube})
 
        for color, cube in min_set.items():
            product *= cube
        min_sets.append(product)

    return min_sets

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

with open('day2/input.txt') as games_input:
    power_of_min_set_of_cubes = calculate_power_of_min_set_of_cubes(games_input)

print(f'Power of the minimal sets are: {sum(power_of_min_set_of_cubes)}')