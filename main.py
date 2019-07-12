from osrsbox import *
from OSRS_Hiscores import Hiscores

# User to lookup
username = 'Zezima'

# Initialize user object, if no account type is specified, we assume 'N'
user = Hiscores(username, 'N')

# Get the entire stat dictionary
print(user.stats)

# Get total Levels
print(user.skill('total'))

# Get a specific skill's ranking, level, and experience
print(user.stats['runecrafting'])

# Get skill's level, ranking, and experience separately
print(user.stats['runecrafting']['level'])
print(user.stats['runecrafting']['rank'])
print(user.stats['runecrafting']['experience'])

# A simpler way to just get a skill's level
print(user.skill('attack'))