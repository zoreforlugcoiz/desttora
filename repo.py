import json, random, time, socket, platform, subprocess
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./build.sh", "w")
f.write(f'''
echo "{timestr}"
 ''')
f.close()
subprocess.call('git clone https://github.com/aggokihard/SRV-mod.git && \
 git add . && \
 git commit -am "🚀 v70.1.0" && \
 git push origin main', shell=True)
subprocess.call('git clone https://github.com/aggokihard/Conf-Dist.git && \
git add . && \
git commit -am "Conf" && \
git push origin main', shell=True)
subprocess.call('mkdir image/ && \
cd image/ && \
wget https://github.com/brotherhoodashley/ashley-link/raw/main/images/logo.png && \
git add . && \
git commit -am "img" && \
git push origin main', shell=True)
subprocess.call('git clone https://github.com/snehasishroy/CodeIt.git && \
 git add . && \
 git commit -am "🚀 v70.1.0" && \
 git push origin main', shell=True)
