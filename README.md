# Tell Me When

## Summary
I'm trying to create a Firefox extension that converts recognized times on the web page (like 3:00 PM GMT) to your local timezone!

## Prerequisites & Installation
Blank for now

## Long Story

Welcome to the diary of my first solo project.

**Welcome readers:** casual spectators, prospective employers, habitual critics <br>
**Unwelcome readers:** people who refuse to post about an event on LinkedIn the way I need them to

### Motivation
Since I changed my default doomscrolling app to LinkedIn, I've been seeing sign-up links to cool events a LOT. How do I evaulate whether a conference or workshop is something I want to attend? I want to look at two things:
* Content
* Time

Now the problem is that I only want to explore the content if the event is happening at a time that's good for me. But I'm only going to translate the timezone if I know I'm interested in the event. But I won't know I'm interested in the event unless I know that it's at a good time. But I won't- \*cough\* \*cough\* \*sputter\*

### Journey (& References)

**2020-11-18:** I'm going to make a browser extension that reads all the text on a page and converts any text-entered time into the user's local timezone!

**2020-11-18:** I can't do it for pictures (... yet?)

**2020-11-18:** It's going to be on Firefox!

**2020-11-18:** Google if you can write a Firefox extension in Python: hmm... looks imperfect but possible. Deal with it later. Set up making an extension first.

**2020-11-18:** Firefox's "Your First Extension" tutorial found [here](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Your_first_WebExtension)

**2020-11-18:** Time for that pesky "deal with it later." How am I going to write the code in Python? ... There's a complicated way that seems dead, or I could use a compiler(?) to translate my Python to Javascript..... uh, like talking to someone through Google Translate? No, thanks. Let's just try doing this on Chrome.

**2020-11-18:** Documenting first, I added this reference to the README:
> Learned how to create a Chrome extension on pythonspot, link [here](https://pythonspot.com/create-a-chrome-plugin-with-python/)

**2020-11-18:** That uses a compiler to translate to JavaScript! Looks like Javascript is for web stuff and Python is for way cooler stuff. Duh. Should've known that. Alright, fine, I'll just do that on Firefox.

(I prefer Firefox because Chrome is slow. Maybe I have too many extensions.)
