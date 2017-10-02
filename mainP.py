

#Main explanation

#use main() to check if this file is being imported or being run by py directly

#print "Main is: {}".format(__name__)

#Some code is run directly and some is imported and then used.

if __name__ == '__main__':
    print "Run Directly"

else:
    print "Run from import"

