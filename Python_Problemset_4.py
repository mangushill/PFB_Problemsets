#!/usr/bin/env python3

#Problemset 5
favorite_things = {}
print(favorite_things)
favorite_things['Books'] = 'Science'
favorite_things['Dogs'] = 'Border Collie'
favorite_things['Fish'] = 'Koi'
print (favorite_things['Dogs'])
thing = 'Dogs'
print (favorite_things[thing])
print (favorite_things['Fish'])
favorite_things['Organism'] = 'Fungi'
thing = 'Organism'
print(favorite_things[thing])
things = ['Books','Dogs','Fish','Organism']
for thing in things:
	print (thing)

