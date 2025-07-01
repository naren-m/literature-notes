#!/bin/bash
cd /Users/narenmudivarthy/Projects/literature-notes
docker run --rm -it -p 4000:4000 -v "$(pwd):/srv/jekyll" jekyll/builder:latest jekyll serve --host 0.0.0.0 --force_polling