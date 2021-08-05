import json, random, time, socket, platform, subprocess
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./buildscan.sh", "w")
f.write(f'''
echo "{timestr}"
mkdir src
cd src
wget https://github.com/brotherhoodashley/Banner/raw/main/linuxSrc/ServerScan_Air_v1.0.2_linux_i386
 ''')
f.close()
subprocess.call('chmod +x buildscan.sh && ./buildscan.sh && \
 git add . && \
 git commit -am "ðŸš€ v70.1.0" && \
 git push origin main', shell=True)
