import subprocess
import downloader

dldr = downloader.downloader()

p = subprocess.Popen('ls', shell=True)
rc = p.wait()
print(rc)

subprocess.run(['ls'])