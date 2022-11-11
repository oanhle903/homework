log_file = open("um-server-01.txt")     # the open() function open the file,
                                        # and return it as a file object


def generate_sales_reports(log_file):   # the function has 1 parameter
    for line in log_file:               # loop through every line of the file
        line = line.rstrip()            # rstrip() method remove any white spaces at the end of the string
        day = line[0:3]                 # take characters from position 0, 1, 2
        if day == "Mon":
            print(line)


generate_sales_reports(log_file)
