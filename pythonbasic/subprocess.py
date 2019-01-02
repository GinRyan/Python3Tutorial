import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=-1, stdout=-1, stderr=-1)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('ansi'))
print('Exit code:', p.returncode)