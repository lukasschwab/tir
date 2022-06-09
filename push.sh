#!/bin/sh
cd ~/Programming/tir/
# If there's a change to tir.html
if ! git diff-index --quiet HEAD -- index.html tir.xml; then
    # Push any changes in tir.html / tir.xml to github
    git add index.html tir.xml
    git commit --quiet -m 'auto tir update'
    git push --quiet
    # terminal-notifier -title 'tir' -message 'Automatically updated' -open 'http://lukasschwab.github.io/tir' -sound default
else
    echo "[tir] No changes to tir.html or tir.xml."
fi
