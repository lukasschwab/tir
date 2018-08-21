#!/bin/sh
cd ~/Programming/tir/
# If there's a change to tir.html
if ! git diff-index --quiet HEAD -- tir.html; then
    # Push any changes in tir.html / tir.xml to github
    git add tir.html
    git add tir.xml
    git commit --quiet -m 'auto tir update'
    git push --quiet
    /usr/local/bin/terminal-notifier -title 'tir' -message 'Automatically updated'  -open 'http://lukasschwab.github.io/tir' -sound default
fi
