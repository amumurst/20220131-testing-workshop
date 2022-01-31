def distinctList(ls):
    return list(set(ls))

def filterUser(user, owner):
    return user.age >= 18 and user.id != owner
