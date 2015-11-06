import sys
import os
import logging

sys.path.insert(0, "/home/tim/http/personalWebsite")
os.chdir("/home/tim/http/personalWebsite")

from main import app as application

logging.basicConfig(stream=sys.stderr)
