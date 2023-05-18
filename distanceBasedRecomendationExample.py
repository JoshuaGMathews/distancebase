from operator import itemgetter


def minkowski_distance(UXRatings,UYRatings,r):
    distance = 0       
    for k in (set(UXRatings.keys()) & set(UYRatings.keys())):
        p = UXRatings[k]
        q = UYRatings[k]
        distance += pow(abs(p - q), r)

    return pow(distance,1/r)

# example user ratings
songData3 = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }


userX = "Hailey"
userXRatings = songData3[userX]

userXMD = ()
r = 2
for s in songData3:
    if s != userX:    
        temp = (s, minkowski_distance(userXRatings, songData3[s], r)),
        userXMD = userXMD + temp
userSortedDistances = (sorted(userXMD, key = itemgetter(1)))
userXNN = userSortedDistances[0][0]
userXNNRatings = songData3[userXNN] #while not neccessary for the assignment, I felt it made the code more readable
userXRecos = ()
for i in userXNNRatings:
    if i != userXRatings:    
        temp = (i, userXNNRatings[i]),
        userXRecos = userXRecos + temp
userXSortedRecos = (sorted(userXRecos, key = itemgetter(1), reverse = True))

print ()
print ("Recommendations for", userX)
print ("--------------------------")
print ()
print (userXSortedRecos)