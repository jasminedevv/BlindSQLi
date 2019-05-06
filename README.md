# Blind SQLi Proof of Concept
This is my solution for a take-home interview problem which asked me to guess an admin password on their site. I tried to make it more generic and removed references to the target. You could probably still guess what web framework it targets though. 

The target had the following features:
1. A form that runs SQL commands but does not return results
2. Unencrypted passwords

## My solution
### get_base_response_time
Establishes how long the site normally takes to respond. I found that a high degree of accuracy was not really needed here so it only runs once.

### inject
Submits the target form with a SQL command. Returns True if the command takes longer to run than the base time.

### guess_pass_length
Injects commands that try different password lengths until it gets a positive result.

### guess_pass
Given a password length, tries substrings until it guesses the full password.

## My Process
I used mocks and stubs to test the functionality of each function to avoid sending the site anything before I know that my code works. I used pytest for this. Since the these tests contain hardcoded info about the target, they are not in this repo.

## Did it work?
Yea! The script guessed the password in under a minute. Putting lowercase letters first in the try order would have made it go a lot faster.

## Did you get the job?
I did!!
