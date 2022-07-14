import subprocess
# original command -> git branch -r --merged staging | egrep -v "origin\/(staging|production|test|levelbuilder$)$"
# piping does not seem to work so includes 2 other branches which will be removed below
bashCommand1 = "git branch -r --merged staging"
process = subprocess.Popen(bashCommand1.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error = process.communicate()

# convert byte object to string
output = output.decode("utf-8")
print(output)
# origin/ and newline from each branch name
output = output.replace("origin/", "")
output = output.replace("\n", "")
# remove 2 branches from list - Head -> staging and staging from branches
output = output.replace("HEAD -> staging", "")
output = output.replace("staging", "")

# convert string to string array
branches = output.split()
print(branches)
print(len(branches))
count = 0
for b in branches:
    toKeep = ["production", "levelbuilder", "test", "staging"] # ensure these branches are NOT deleted
    if b not in toKeep:
        count = count + 1
        bashCommand = ['git', 'push', '--delete', 'origin', b]
        process = subprocess.Popen(bashCommand, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        print(count)

