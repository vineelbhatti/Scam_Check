# Scam_Check

Our scam checker will detect scams and malicious content in all of your emails. It can be scaled up to be implemented in popular email, text, and other messaging platforms.

## Inspiration
Scams and phishing have become more prominent over the last few decades. This has been especially harmful to the elderly and others that are not informed about the dangers of an insecure cyberspace. While there exists some software to combat spam in platforms, spam emails remain a common threat in many messaging platforms. We were inspired by this problem to create a simple program that can be implemented to solve these issues.

## What it does
Our program checks to see if an email is a scam or not. It assesses the likelihood of a scam based on the occurrence of specific words associated with scam emails. It can either check a text file or check a user’s input directly. 

## How we built it
We collaborated using an online IDE called Replit which allowed us to work on the project simultaneously. Using Python, we made a list of common scam words and iterated through a text file to see how often those words showed up in an email. We then divided the number of times those words showed up by the total number of words to get a percentage of how scam-likely the email would be. To see if it was a scam, we asked the user how strictly they wanted the program to check the email and used if statements to compare the scam-likely percentage with the strictness level they chose. 

## Challenges we ran into
We ran into many challenges while building our program because none of us are very familiar with cyber security. So, in a sense, this whole hackathon was a challenge to us. We persevered, however, and researched ways to implement our coding skills into this new field: cybersecurity. Along the way, we faced other challenges, like aligning our schedules, brainstorming ideas, and learning new coding languages.

## Accomplishments that we're proud of
We are proud of the program being fully functional and being able to detect the trustworthiness of a message with fairly good accuracy. We are also proud of the clean user interface of our program and the ease with which it can be implemented to other platforms. It is very accessible to people not accustomed to technology because of its clean and simple interface.

## What we learned
During this hackathon, we encountered many challenges, and so learned a lot of things to overcome these challenges. For example, while researching the topic, cybersecurity, we learned the basic principles and how to identify malicious software and malware. Then, we had to learn new techniques in coding languages we were unfamiliar with in order to build our final project. These techniques included reading and writing files and interacting with the user.

## What's next for Scam Checker
In the future, Scam Checker can be improved to be more accurate using artificial intelligence. This can create a more accurate measurement or rating with regards to the email. In addition, we can deploy our program by implementing it with commonly used messaging platforms. By doing so, we gain access to users that can provide us with feedback so that we can further improve our algorithm. Our final goal is to create a program that has a near 100% success rate in determining whether or not an email is trustworthy. 
