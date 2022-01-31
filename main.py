from implementation.program import program
from implementation.Database import CSVDatabase


if __name__ == "__main__":
    database = CSVDatabase("users.txt", "ads.txt")
    print("Application started")
    while(1):
        print(program(database, input()))