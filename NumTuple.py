from collections import namedtuple

player = namedtuple('player','name score count')

Earth = player(name = 'Earth', score = '104',count = '14')
#Mars =  player('Mars','105','6')

print(Earth.name,Earth.score,Earth.count)






