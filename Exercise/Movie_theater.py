"""The movie theater has cinema halls that can accommodate a certain number of viewers each.
Figure out if a movie theater can hold a given number of viewers 
that plan to visit it on a particular day."""


number_of_halls = int(input(" ").strip())
capacity = int(input(" ").strip())
number_of_viewers = int(input(" ").strip())

print((number_of_halls * capacity) >= number_of_viewers)
