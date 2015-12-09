import linecache
import time
now=time.time()
data_keys = ('bid', 'uid', 'username', 'v_class', 'content', 'img', 'created_at', 'source', 'rt_num', 'cm_num', 'rt_uid', 'rt_username', 'rt_v_class', 'rt_content', 'rt_img', 'src_rt_num', 'src_cm_num', 'gender', 'rt_bid', 'location', 'rt_mid', 'mid', 'lat', 'lon', 'lbs_type', 'lbs_title', 'poiid', 'links', 'hashtags', 'ats', 'rt_links', 'rt_hashtags', 'rt_ats', 'v_url', 'rt_v_url')

keys = {data_keys[k]:k for k in range(0,len(data_keys))}

f = linecache.getlines('tw.txt')

lines = [x[1:-1].split('","') for x in f] #拆分

#input all users
users=set(line[keys['username']] for line in lines)
user_total = len(set(users))
assert type(user_total) == int
print(user_total)

#all username

usernames=list(users)

#print(usernames)

#line from 2012 11

lines_from_2012=filter(lambda line:line[keys['created_at']].startswith("2012-11"),lines)
print(len(list(lines_from_2012)))


