#!/usr/bin/python
import re
import error_classes

mail_log_file="/var/log/exim/main.log"
local_domain_file="localdomains"
email_address = script_input[0]

# Is the email address provided valid
if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address) is None:
	# If not, throw an Input Error
	raise InputError("You need to provide a valid email address as input")
	exit(1)


def is_local_domain():
	domain_name = email_address.split("@")[1]
	file = open('test.txt','r')
	while True:
    	line = file.readline()
    	if line is domain_name
    		return True

def main(argv):
    pass

if __name__ == "__main__":
    main(sys.argv)
    exit(0)



