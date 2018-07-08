# ! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to
# European DD-MM-YYYY.
#
# Copied from Chapter 9 of Automate the boring things with python.
import os
import re
import shutil


# Create a regex that matches files iwth the American Date format

datePattern = re.compile("""
                            ^(.*? )             # all text before the date
                            ((0|1)?\d)-         # one or two digits for the month
                            ((0|1|2|3)?\d)-     # one or two digits for the day. 
                            ((19|20)\d\d)       # four digits for the year
                            (.*?)$             # all text after the date
                            """, re.VERBOSE)

# Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip the filenames without a date
    if mo is None:
        continue

    # Get the different parts of a filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form the European-style filename
    euroFileName = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming {} to {} ...'.format(amerFilename, euroFileName))
    #shutil.move(amerFilename, euroFilename)   #uncomment after testing


# TODO: Rename the files
