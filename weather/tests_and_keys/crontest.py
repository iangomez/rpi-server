import datetime
from pushbullet import Pushbullet
pb = Pushbullet('o.cLhE1SyrpsZYocwqDrTHUPbHGqrW8L74')

# crontab
# * * * * * /usr/bin/python3 /home/pi/weather/crontest.py

t = str(datetime.datetime.now().time())
f = open('crontab.txt','a')
wrdata = f.write(t)
f.close()
push = pb.push_note('Cron Update', 'Cron worked')
