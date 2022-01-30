import subprocess

proc = subprocess.Popen('dir C:\\', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = proc.communicate()
print(out)