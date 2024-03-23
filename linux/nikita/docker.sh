#!/bin/bash

TIMEFORMAT='Script was runned: %R seconds.'
time {
    docker stop donotest >/dev/null 2>/dev/null
    docker rm donotest >/dev/null 2>/dev/null
    rm ~/Desktop/index.html >/dev/null 2>/dev/null

    start=`date +%s`
    docker run -d --name donotest -p 80:80 0lmi/donotest >/dev/null 2>/dev/null

    while true; do
        let n=$n+1
        curl http://127.0.0.1 >/dev/null 2>/dev/null
        if [ $? -eq 0 ]; then
            end=`date +%s`
            sleep 2
            docker cp donotest:usr/local/apache2/htdocs/index.html ~/Desktop/ >/dev/null 2>/dev/null
            htmlval -w -l ~/Desktop/index.html | grep -v "Comment\|File" | sed 's/[=]//g'
            break
        elif [ $(($(date +%s)-$start)) -ge 15 ]; then
            echo "15sec Error"
            exit
        fi
    done
}

echo "Container fist answer detected in: $(($end-$start)) seconds."

