You are a backend developer of some random classifieds site.

Your product manager wants to make a new feature!
The feature is; It should be possible to get the email of everyone that has favourited an ad.
This is the specification you get:
- It should only be possible to get this for your own ads
- The result should only contain unique addresses
- The email of users below 18 have to be removed
- The owners email should not be returned even though they somehow have favourited their own ad
- The output should follow this format: "Favourited by: some@email.com, kj@eltring.no"
- If noone has favourited the ad, respond with "Your ad seems to need some love"
- If the ad is not yours, respond with: "This is not yours!"
- If the ad does not exist, respond with: "Ad does not exist"
- If the user inputs bad values, respond with: "Bad input!"
- The program should run forever

In adition your frontend buddy tells you that you will get requests on the form `USERID_ADID` and that you can assume this data to be correct.

You have downloaded two relevant databases and made them into csv(comma separated values) so its easier to start working.

ads.txt contains ads on the format: AdId(number), vertical(text), price(number), availability status (sold, available or unlisted), owner(UserId)

users.txt contains users on the format: UserId(number), name(text), favourites(list of adIds separated by space), age(number), email(text)




pip3 install --user pipenv
pipenv run python -m unittest test_04_property.py

https://hypothesis.readthedocs.io/en/latest/index.html
https://mutmut.readthedocs.io/en/latest/

mutmut run --paths-to-mutate 'implementation/utils.py' --tests-dir tests