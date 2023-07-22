import datetime
import sys
# open a log with format katrain-YYYY-MM-DD-hh-mm-ss.log
f = open("katrain-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log", "w")
sys.stderr = f
sys.stdout = f
# for backward compatibility
from katrain.__main__ import run_app

run_app()
