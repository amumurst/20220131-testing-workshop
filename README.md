# Workshop
This workshop consists of a hypothetical backend task. 

The steps to be taken are;
1. Understand the task
2. Understand the given script.py implementation
3. Give feedback on script.py and consider why we might want to refactor it
4. Understand refactored application
5. Add some unit tests
6. Add some integration tests
7. Add some golden tests
8. Add some property tests
9. Add some mutation tests
10. Reflections, Q&A, open floor and discussion of other types like UI tests and performance tests

## Task
You are a backend developer of some random classifieds site.

Your product manager wants to make a new feature!
The feature is; It should be possible to get the email of everyone that has favorited an ad.
This is the specification you get:
- It should only be possible to get this for your own ads
- The result should only contain unique addresses
- The email of users below 18 have to be removed
- The owners email should not be returned even though they somehow have favourited their own ad
- The output should follow this format: "Favorited by: some@email.com, kj@eltring.no"
- If no one has favorited the ad, respond with "Your ad seems to need some love"
- If the ad is not yours, respond with: "This is not yours!"
- If the ad does not exist, respond with: "Ad does not exist"
- If the user inputs bad values, respond with: "Bad input!"
- The program should run forever

In addition your frontend buddy tells you that you will get requests on the form `USERID_ADID` and that you can assume this data to be correct.

You have downloaded two relevant databases and made them into csv(comma separated values) so its easier to start working.

ads.txt contains ads on the format: AdId(number), price(number), owner(UserId)

users.txt contains users on the format: UserId(number), favorites(list of adIds separated by space), age(number), email(text)

## Commands
Install: `pip3 install --user pipenv && pipenv install`

run specific test: `pipenv run python -m unittest test_04_property.py`

Property test docs: https://hypothesis.readthedocs.io/en/latest/index.html

Mutation test docs: https://mutmut.readthedocs.io/en/latest/

Run mutation tests: `mutmut run --paths-to-mutate 'implementation/utils.py' --tests-dir tests`