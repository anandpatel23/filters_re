# Anand Patel (23anandpatel23@gmail.com)
import re

def filterPath(filePath):
    """ Searches through given arguement string of a file path and searches for
    terms that are not to be included within database
    """
    # all filters and uppercasing all of them
    filters = ["TEST", "OLD", "PREVIOUS", "DRAFT", "JAR", "TEMP", "COMMON", "LOG", "RESOURCE"]
    filters = [itemFilter.upper() for itemFilter in filters]

    # uppercasing given path
    filePath = filePath.upper()

    # if there isn't a match with any filter, it's a valid item to add
    match = False
    for itemFilter in filters:
        if re.search(itemFilter, filePath, re.IGNORECASE):
            match = True
            break
    if not match:
        acceptedPath = filePath
        return acceptedPath

def main():
    # Paths here
    filePaths = []
    for item in filePaths:
       result = filterPath(item)
       if result != None:
        print result
if __name__ == '__main__':
    main()
