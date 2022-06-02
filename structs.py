from struct import *

data = "14바이트패킷"
payload = unpack('<Hfff', data)

u_cnt = payload[0]
lat = payload[1]
long = payload[2]
alt = payload[3]
