import urllib
import sys

def usage():
    print "Usage: " + sys.argv[0] + " plain_password"
    print "example: python percent-encode.py 'r!Uopr'"
    exit(1)

if len(sys.argv) < 2:
    usage()

print urllib.quote(sys.argv[1])
