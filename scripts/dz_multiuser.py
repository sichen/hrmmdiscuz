#!/usr/bin/env python
'''
The python script helps me create discuz users in batch
Created on Nov 14, 2011

@author: sichen
'''
from optparse import OptionParser
import datetime
import time
import sys
import md5
import random
import re

# Globals
# the global salt value
SALT = 'ab12cd'
# the global password
PW = 'rzxlszy'
# the global md5 hash of
# md5(md5($password).$salt);
M = md5.new(PW).hexdigest()
PASSWORD = md5.new(M+SALT).hexdigest()
TIMEBASE = 1319783169
TIMENOW = int(time.time())

def add_user(uid, username, password, salt, email, timestamp='1318315182', ip = '71.198.27.101', timeoffset = 9999, credit = 2):
    insert_user = "INSERT IGNORE INTO pre_ucenter_members(username,password,email,regip,regdate,salt) VALUES(" + " '" + username + "','" + password + "','" + email + "','" + ip + "'," + timestamp + ",'" + salt + "');"
    insert_memberfield = "INSERT IGNORE INTO pre_ucenter_memberfields(uid) VALUES (" + str(uid) + ");" 
    print insert_user
    print insert_memberfield
    
    activate_user = "INSERT IGNORE INTO pre_common_member(email,username,password,emailstatus, regdate,credits,timeoffset ) VALUES( " + "'" + email + "','" + username + "','" + password + "', 1, " + timestamp + ", " + str(credit) + ", " + str(timeoffset) + ");"
    activate_user_membercount = "INSERT IGNORE INTO pre_common_member_count(uid,extcredits2) VALUES (" + str(uid) + ", " + str(credit) + ");" 
    print activate_user
    print activate_user_membercount

def validate_user(username):
    pattern = re.compile('[\w\d.+-]+')
    match = pattern.search(username)
    if match:
        return username
    else:
        return ''
    
def process_user(uid, username):
    if username == '':
        return
    email = username + '@telekbird.com.cn'

    rtime = random.randint(TIMEBASE, TIMENOW)
    timestamp = str(rtime)

    ip0 = random.randint(1, 255)
    ip1 = random.randint(1, 255)
    ip2 = random.randint(1, 255)
    ip = '71.%d.%d.%d' % (ip0, ip1, ip2)

    add_user(uid, username, PASSWORD, SALT, email, timestamp, ip)

def process_file(startuid, filename):
    lines = []
    uid = startuid
    number_processed = 0
    try:
        f = open(filename)
        lines = f.readlines()
        f.close()
    except IOError, e:
        print "IOError: %s" % (str(e))
        sys.exit(1)

    print "========================="
    # each line contains a username
    for line in lines:
        uname = validate_user(line.strip())
        if uname == '':
            break
        process_user(uid, uname)
        uid += 1
        number_processed += 1
    # print out summary
    print "========================="
    print "processed: " + str(number_processed)
    print "========================="
        
def options_parser(scriptname):
    usage = "Usage: " + scriptname + "[--start-uid UID] [--user-file FILE] "
    parser = OptionParser(usage)

    parser.add_option("", "--start-uid", type="int", dest="uid", action="store",
                      help="The uid to start with, must not be in the database already.")

    parser.add_option("", "--user-file", type="string", dest="userfile", action="store",
                      help="The file that contains a list of usernames to be created.")

    return parser

def main():
    parser = options_parser(sys.argv[0])
    (options, args) = parser.parse_args(sys.argv)
    if not options.uid:
        print parser.print_help()
        sys.exit(1)
    if not options.userfile:
        print parser.print_help()
        sys.exit(1)
    process_file(options.uid, options.userfile)
    
if __name__ == "__main__":
    main()