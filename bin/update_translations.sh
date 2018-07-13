#!/usr/bin/env bash

POT_FILE=lektor_creative_commons/locales/messages.pot

xgettext --no-location lektor_creative_commons/plugin.py --output $POT_FILE

for file in $(find . -name '*.po') ; do
    msgmerge --quiet --no-location --backup=none --update $file $POT_FILE
done
