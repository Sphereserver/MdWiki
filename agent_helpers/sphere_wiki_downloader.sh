#!/usr/bin/env sh
python3 ./download_mediawiki.py --url "https://wiki.spherecommunity.net/api.php" --mode=api --exclude-external --workers=14 --output="../mediawiki_orig"
