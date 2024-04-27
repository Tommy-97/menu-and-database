#my_traceback.py
import traceback

try:
    1 / 0
except Exception as e:
   
    traceback.print_exc()
