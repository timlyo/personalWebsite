import sys
import os
import logging

sys.path.insert(0, "/home/tim/personalWebsite")
os.chdir("/home/tim/personalWebsite")

from main import app as application

logging.basicConfig(stream=sys.stderr)
