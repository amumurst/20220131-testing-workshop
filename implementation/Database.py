from sys import implementation
from implementation.Ad import Ad
from implementation.User import User


class Database:
    def findAd(adId: int) -> Ad:
        pass
    def usersWithAdAsFavourite(self, adId: int) -> list[User]:
        pass

class CSVDatabase(Database):
    def __init__(self, userFileName: str, adFileName: str) -> None:
        with open(userFileName) as file:
            self.users = [User(line) for line in file]
        with open(adFileName) as file:
            self.ads = [Ad(line) for line in file]

    def findAd(self, adId: int) -> Ad:
        for ad in self.ads:
            if ad.id == adId: return ad

    def usersWithAdAsFavourite(self, adId: int) -> list[User]:
        return [user for user in self.users if adId in user.favourites]