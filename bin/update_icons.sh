#!/usr/bin/env bash

LICENSES="by-nc-sa,by-sa,by-nc-nd,by-nd,by-nc,by"
SIZES="80x15,88x31"
VERSIONS="4.0"
ASSETS="lektor_creative_commons/assets"

mkdir -p $(eval echo $ASSETS/{$LICENSES}/$VERSIONS/)

for icon in $(eval echo {$LICENSES}/$VERSIONS/{$SIZES}.png)
do
    curl https://licensebuttons.net/l/$icon > $ASSETS/$icon
done
