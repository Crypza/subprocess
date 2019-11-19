import subprocess

cmd = "ipconfig"

returned_value = subprocess.call(cmd, shell=True)
print('returned_value:', returned_value)