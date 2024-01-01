data = [line.strip().split() for line in open("Day 19/rawData.txt")]

blueprints = []
for blueprint in data:
    blueprints.append([int(blueprint[6]), int(blueprint[12]), int(blueprint[18]), int(blueprint[21]), int(blueprint[27]), int(blueprint[30])])

test_blueprints = [
    [4, 2, 3, 14, 2, 7],
    [2, 3, 3, 8, 3, 12]
]

# resources and robots:
# [ore, clay, obsidian, geoge]
#   0     1       2       3

# blueprints:
# [ore_cost_in_ore, clay_cost_in_ore, obsidian_cost_in_ore, obsidian_cost_in_clay, geode_cost_in_ore, geode_cost_in_obsidian]
#       0                   1               2                           3                   4                   5

def tick_minute(blueprint, robots_inp, resources_inp):

    # buy robots
    robots, resources = robots_inp, resources_inp
    building_queue = [0, 0, 0, 0]
    # geode
    if resources[2] >= blueprint[5] and resources[0] >= blueprint[4]:
        building_queue[3] += 1
        resources[2] -= blueprint[5]
        resources[0] -= blueprint[4]
    # obsidian
    if resources[1] >= blueprint[3] and resources[0] >= blueprint[2]:
        building_queue[2] += 1
        resources[1] -= blueprint[3]
        resources[0] -= blueprint[2]
    # clay
    if resources[0] >= blueprint[1] and robots[1] + resources[1] < blueprint[3] and robots[2] + resources[2] < blueprint[5]:
        building_queue[1] += 1
        resources[0] -= blueprint[1]

    # collect resources
    for index, robot_count in enumerate(robots):
        print(f"{index} robots collected {robot_count} resources")
        resources[index] += robot_count

    # build robots
    for index, robot_count in enumerate(building_queue):
        print(f"{robot_count} {index} robots built")
        robots[index] += robot_count
    
    return robots, resources

robots = [1, 0, 0, 0]
resources = [0, 0, 0, 0]
for _ in range(24):
    print(f"\n### MINUTE {_+1} ###")
    robots, resources = tick_minute(test_blueprints[0], robots, resources)
    print(f"resources: {resources}\nrobots: {robots}")

print(resources[3])