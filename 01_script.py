while (1):
    userInput = input().split("_")
    if(len(userInput) != 2):
        print("Bad input!")
        continue
    userId, adId = userInput

    ads = [] 
    with open("ads.txt") as file:
        [ads.append(line.strip().split(", ")) for line in file]

    users = [] 
    with open("users.txt") as file:
        [users.append(line.strip().split(", ")) for line in file]

    possibleAds = [ad for ad in ads if ad[0] == adId]
    if(len(possibleAds) == 0):
        print("Ad does not exist")
        continue

    ad = possibleAds[0]
    if(ad[4] != userId):
        print("This is not yours!")
        continue

    favourited = [user for user in users if adId in user[2].split(" ") and int(user[3]) >= 18 and user[0] != userId]
    if(not len(favourited)):
        print("Your ad seems to need some love")
        continue

    emails = [user[4] for user in set(favourited)]
    print("Favourited by: " + ", ".join(emails))