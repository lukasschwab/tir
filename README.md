# tir
<p align="center">
tir––short for "Today I Read"––is a barebones CLI for logging memorable articles.<br><br>
<img src="http://lukasschwab.github.io/img/reading.gif">
</p>

***

## About

The aim is to collect everything you read every day so you can find and share it. No more "I forget where I read it..."

This was supposed to be functionality that I'd build into ezrss, but I'm finding that difficult (because that would require scraping a whole bunch of text that is structured differently). There might be eventual integration, but not right now.

## Setup

1. Download/unzip or clone this repository: `git clone https://github.com/lukasschwab/tir.git`.

2. Optionally, move `tir.html` to a desired location (e.g. if you don't want to host tir separately, move `tir.html` into a GitHub Pages repo). Simplest setup with GitHub Pages would be to create a gh-pages branch (`git branch gh-pages`) and leave `tir.html` where it is.

3. Modify [tir/\_\_main\_\_.py](https://github.com/lukasschwab/tir/blob/master/tir/__main__.py) so that the path on line four points to your local copy of `tir.html`. For example, `html = "~/Desktop/tir/tir.html"`.

4. *After changing that path*, run `python setup.py install` from the project root directory.

5. From the command line, just run `tir`. To undo an entry, run `tir --delete`.

I've also done some hacking with `crontab` to auto-push changes to my tir.html file. This is very hacky, and will stop whenever I have to do development in that repo. That script lives [here](https://github.com/lukasschwab/lukasschwab.github.io).

## To do

+ Only list last 15 or so tirs in the feed (cleanup)
    + Maybe need to include date as an attr for each item element? Shouldn't screw up the rest...

+ RSS setup instructions in README on this branch. Mention that this is the version I use locally.