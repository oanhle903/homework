def report(day, file_name):
    """Given day number & path to the deliveries, produce report.

    Opens the deliveries file at [path], processes each line,
    and generates report in all uppercase.
    """
    print(f"Day {day}")
    with open(file_name) as the_file:
        # the_file = open(file_name)
        # iterate over each line in the file object
        for line in the_file:       
            line = line.rstrip()    # remove the whitespace on the right side
            words = line.split('|') # create a list of strings

            # Assign a variable to each item from the words list
            melon = words[0]
            count = words[1]
            amount = words[2]

            # Or you could do this with "list unpacking":
            #
            # melon, count, amount = words
            
            print(f"Delivered {count} {melon}s for total of ${amount}")
        # the_file.close()

report(1, "um-deliveries-day-1.txt")
report(2, "um-deliveries-day-2.txt")
report(3, "um-deliveries-day-3.txt")