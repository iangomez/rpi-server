from pushbullet import Pushbullet
pb = Pushbullet(keys.pbapi)
push = pb.push_note('Wifi', 'ping: {}ms, down: {}mb/s, up: {}mb/s'.format(ping, down, up))
