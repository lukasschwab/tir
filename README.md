# tir
<p align="center">
tir – short for "Today I Read" – is a barebones CLI for logging memorable articles. It's archived; use <a href="https://github.com/lukasschwab/tiir">tiir</a> instead!<br><br>
<img src="http://lukasschwab.github.io/img/reading.gif">
</p>

***

## About

The aim is to collect everything you read every day so you can find and share it. No more "I forget where I read it..."

This was supposed to be functionality that I'd build into ezrss, but I'm finding that difficult (because that would require scraping a whole bunch of text that is structured differently). There might be eventual integration, but not right now.

## Setup

1. Download/unzip or clone this repository: `git clone https://github.com/lukasschwab/tir.git`.

2. Optionally, move `index.html` to a desired location (e.g. if you don't want to host tir separately, move `index.html` into a GitHub Pages repo). Simplest setup with GitHub Pages would be to create a gh-pages branch (`git branch gh-pages`) and leave `index.html` where it is.

3. Modify [tir/\_\_main\_\_.py](https://github.com/lukasschwab/tir/blob/master/tir/__main__.py) so that the path on line four points to your local copy of `index.html`. For example, `html = "~/Desktop/tir/index.html"`.

4. *After changing that path*, run `python setup.py install` from the project root directory.

5. From the command line, just run `tir`. To undo an entry, run `tir --delete`. To push changes to GitHub, run `tir -p`.

### RSS

1. Add an empty RSS feed XML file to a location where it'll be tracked (it would make sense to put this in the same directory as `index.html`). For example, see [feed.xml](https://github.com/lukasschwab/tir/blob/feed/feed.xml).

2. Modify [tir/\_\_main\_\_.py](https://github.com/lukasschwab/tir/blob/master/tir/__main__.py) to point at the correct feed file.

### Reversibility

By default, tir will add new items to the top of the table. To reverse this, toggle the flag `INORDER` in `__main__.py`.

If you want to transition from one ordering to the other––i.e. if you have an established tir page with `INORDER = True` and you want to switch to `INORDER = False` or vice versa, use `reverse.py`.

## To do

+ Only list last 15 or so tirs in the feed (cleanup)
    + Maybe need to include date as an attr for each item element? Shouldn't screw up the rest...
    + ON ADD:
        + Check if there are 15+ items.
        + Iterate through and map parsed datetime to item. Get minimum key (datetime, all naive probably) and then delete that item.
