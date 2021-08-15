# Sample for Windows (E:\\Backup\\Data\\)

from dirsync import sync
source_path = 'X:'
target_path = 'G:'

sync(source_path, target_path, 'sync', verbose = 'verbose') #syncing one way
sync(target_path, source_path, 'sync', verbose = 'verbose') #syncing both
