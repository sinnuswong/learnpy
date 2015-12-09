import subprocess
cmd="cmd.exe"
begin=199
end=200
while begin<end:
    p=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,
                       stdin=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    p.stdin.write("ping 192.168.1.2".encode())
    p.stdin.close()
    p.wait()
    print ("execution result: %s" %p.stdout.read())
    begin+=1
