#!/bin/bash
INTERVAL=31560000

current=$(date +%s)
echo $current
git for-each-ref refs/remotes | while read commit type ref;do
    headcd=$(git log -1 --pretty=%cd --date=format:%s ${commit})
    if [[ ! ${ref##*/} =~ ^(production|test|staging|levelbuilder|maker-webusb)$ ]] ; then
        PATH=$PATH:$TEMP;
        if [[ $((current-headcd)) -ge ${INTERVAL} ]];then
            echo ${ref##*/}
        fi
    fi
done
