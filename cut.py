#!/usr/bin/env python

import re

log="[10:31:00] [Server thread/INFO]: trick_ogino[/183.180.174.160:33715] logged in with entity id 70220 at (241.82326476802376, 71.0, 263.40629566104127)"

print re.split(r"[ \[\]]+",log)

