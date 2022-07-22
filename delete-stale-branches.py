import subprocess
branches_list = open('stale-branches-list.txt').read().splitlines()
print(branches_list)
print(len(branches_list))

count = 0
for b in branches_list:
    toKeep = ["production", "levelbuilder", "test", "staging"] # ensure these branches are NOT deleted
    if b not in toKeep:
        count = count + 1
        bashCommand = ['git', 'push', '--delete', 'origin', b]
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
print(count)
