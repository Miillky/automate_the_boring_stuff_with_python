#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format do European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)         # all text before the date (1)
                        ((0|1)?\d)-          # one or two digits for the month (2 (3) )-
                        ((0|1|2|3)?\d)-     # one or two digits for the day (4 (5) )-
                        ((19|20)\d\d)       # four digits for the year (6 (7) )
                        (.*?)$              # all text after the date (8)$
                        """, re.VERBOSE)

# Loop over the files in the working directory.
currDir = os.path.dirname(os.path.realpath(__file__))
for amerFilename in os.listdir(currDir):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # From the European-stype filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths
    absWorkingDir = os.path.abspath(currDir)
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Rename "%s" to "%s"...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)