import subprocess

try:
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
except KeyboardInterrupt:
    print("Download Stopped")
    exit(0)

import os
import logging
logging.disable(logging.WARNING)
os.environ["TF_CPP_MIN_LOG_LEVEL"]

import sqlite3
connection = sqlite3.connect("Data/chats.db")
cursor = connection.cursor()
table = '''CREATE TABLE IF NOT EXISTS ASSISTANT (SERIAL_NO INTEGER PRIMARY KEY,
        QUERY VARCHAR(255) NOT NULL,
        DATE_TIME VARCHAR(50) NOT NULL);'''
cursor.execute(table)
connection.commit()

try:
    import io
    import os
    import tempfile
    import sys
    import subprocess
    import wave
    import aifc
    import math
    import audioop
    import collections
    import json
    import base64
    import threading
    import platform
    import stat
    import hashlib
    import hmac
    import time
    import uuid
    from pprint import pprint
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen
    from urllib.error import URLError, HTTPError
    import requests
except ImportError:
    print("Modules Not Installed")
except KeyboardInterrupt:
    print("Interrupted While Importing Modules")

print("\n\nSetup Finished")
