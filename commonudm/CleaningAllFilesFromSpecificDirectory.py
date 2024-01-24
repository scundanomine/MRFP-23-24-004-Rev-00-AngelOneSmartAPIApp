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
# dirNameA = 'E:\\WebDevelopment\\2023-2024\\MRFP-23-24-004-Rev-00-AngelOneSmartAPIApp\\readandrecord\\rrstate\\positionplots'
# cleaningAllFilesFromSpecificDirectory(dirNameA)
