# Tell Me When

## Summary
I'm trying to create a Firefox extension that converts recognized times on the web page (like 3:00 PM GMT) to your local timezone!

## Prerequisites & Installation
Blank for now


- - - - -
## Adventure Log

Welcome to the diary of my first solo project.

**Welcome readers:** casual spectators, prospective employers, habitual critics

**Unwelcome readers:** people who refuse to post about an event on LinkedIn the way I need them to


### Journey (& References)

**2020-11-18:** I'm going to make a browser extension that reads all the text on a page and converts any text-entered time into the user's local timezone!

**2020-11-18:** I can't do it for pictures (... yet?)

**2020-11-18:** It's going to be on Firefox!

**2020-11-18:** Google if you can write a Firefox extension in Python: hmm... looks imperfect but possible. Deal with it later. Set up making an extension first.

**2020-11-18:** Firefox's "Your First Extension" tutorial found [here](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension)

**2020-11-18:** I kept changing stuff and resetting git commits! That was fun, and my git log is so cleeean!

**2020-11-18:** Time for that pesky "deal with it later." How am I going to write the code in Python? ... There's a complicated way that seems dead, or I could use a compiler(?) to translate my Python to Javascript..... uh, like talking to someone through Google Translate? No, thanks. Let's just try doing this on Chrome.

**2020-11-18:** Documenting first, I added this reference to the README:
> Learned how to create a Chrome extension on pythonspot, link [here](https://pythonspot.com/create-a-chrome-plugin-with-python/)

**2020-11-18:** That uses a compiler to translate to JavaScript! Looks like Javascript is for web stuff and Python is a way cooler process for under the hood stuff. Duh. Should've known that. Alright, fine, I'll just do that on Firefox.

(I prefer Firefox because Chrome is slow. Maybe I have too many extensions.)

**2020-11-18:** Tried to rewrite a comment using git REBASE [reference link [here](https://docs.github.com/en/free-pro-team@latest/github/committing-changes-to-your-project/changing-a-commit-message)]- OOPS. Although I did this successfully before (in a Udacity course, not in this project), it looks like I did something wrong this time. I really want to spend the time to fix it, but I need to get to sleep for work tomorrow. I'm a responsible adult.

**2020-11-18:** Almost couldn't sleep thinking about how I got the answer: delete the local directory and just GIT PULL! It should work, right? I didn't already try that? I will NOT get my laptop out and check. Is it bad that I'm taking the easy way out, or is that what GitHub is FOR?

**2020-11-19:** Git pull worked! And I won't be late for work.

**2020-11-19:** Am I really going to rely on the code version of Google Translate to work with TIMEZONES? Arguably the worst and most difficult type of data to work with across the board? (In my experience, at least.) I should at least TRY to do this in JavaScript first.

**2020-11-19:** See how to get timezone offset in JavaScript [here](https://www.w3schools.com/jsref/jsref_gettimezoneoffset.asp). W3Schools says it's `var.getTimezoneOffset()` but Atom autocompletes the part after `var.` to `jsref_gettimezoneoffset`... YIKES. I'm going with W3S for now.

**2020-11-19:** Grrrr. I'm all over the place. Different ways to get user's timezone in Python found [here](https://stackoverflow.com/questions/13473175/how-to-get-users-local-timezone-other-than-server-timezoneutc-in-python).

**2020-11-19:** I found an AMAZING book! https://eloquentjavascript.net/
