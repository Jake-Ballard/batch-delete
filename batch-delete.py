import os
import glob
import time

# log all files processed in current dir
op_log = open("batch_" + str(time.time()) + ".log", "w")

# set root dir (you might change it :P)
# os.chdir('/') # - linux / mac os
os.chdir('c:\\')  # - winZoz

# set counters
file_processed, file_removed, file_skipped = 0, 0, 0

# delete all files for this extension (you might change it :P)
ext = "tmp"

# start recrsive operations
for file in glob.glob("**/*."+ext, recursive=True):
    file_processed += 1
    try:
        os.remove(file)
        file_removed += 1
        op_log.write(str(file) + " << DELETED\n")
    except:
        file_skipped += 1
        op_log.write(str(file) + " << LOCKED\n")
        pass

# close log
op_log.close()

# print summary
print("Files processed", file_processed)
print("Files removed", file_removed)
print("File locked", file_skipped)
