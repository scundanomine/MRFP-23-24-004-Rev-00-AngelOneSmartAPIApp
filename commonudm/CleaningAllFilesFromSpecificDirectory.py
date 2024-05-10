import os


def cleaningAllFilesFromSpecificDirectory(dirName):
    try:
        files = os.listdir(dirName)
        for file in files:
            file_path = os.path.join(dirName, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
        # print("All files deleted successfully.")
    except OSError:
        print("Error occurred while deleting files.")


# Usage
# dirNameA = 'F:\\AT\\readandrecord\\rrstate\\positionplots'
# cleaningAllFilesFromSpecificDirectory(dirNameA)
