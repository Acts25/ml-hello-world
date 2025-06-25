import platform
import os

print("Hello , ML World from Jenkins!")
print(f"Python Version : {platform.python_version()}")
print(f"Operating System :{platform.system()}{platform.release()}")
print(f"CPU cores : {os.cpu_count()}")
 
