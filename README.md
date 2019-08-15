# Secure &amp; Private AI AMA search

Demo: https://ingus-t.github.io/SPAI-AMA-search/  

This is an idea that came to my mind when the S&P AI Challenge started. Now I got back to it.  
Currently this search does not use ML, and is implemented in Javascript.

This project consists of 4 parts:
1. Converter - py script to parse AMA transcript into a JSON array
2. Web frontend - main purpose is testing
3. Node.js web service that performs the search in JSON arrays
4. ML model (for the future)

## Implemented:
  
## To-do:

* Allow using web service in the slack app
* Check if request comes from Slack authenticated person
* Remove all user names completely (need full member list for that)
* Perform load testing
* Limit max number of questions returned (25?)
* Test for js injections
* Apply ML:
  * to estimate if question has been answered
  * to match question with the best answer
  * to get better precision than pure text search that is used currently