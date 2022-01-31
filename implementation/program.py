from implementation.Database import Database
from implementation.utils import *

def program(database: Database, userInput: str) -> str: 
    userInput = userInput.split("_")
    if(len(userInput) != 2): return "Bad input!"
    userId, adId = userInput

    ad = database.findAd(adId)
    if(not ad): return "Ad does not exist"
    if(ad.owner != userId): return "This is not yours!"

    users = [user for user in database.usersWithAdAsFavourite(adId) if filterUser(user, userId)]
    if(not len(users)): return "your ad seems to need some love"

    users = distinctList(users)
    return "Favourited by: " + ", ".join([user.email for user in users])