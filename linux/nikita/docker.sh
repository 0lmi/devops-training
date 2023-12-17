#!/bin/bash

TIMEFORMAT='Script was runned %R seconds.'
time {
docker stop donotest >/dev/null 2>/dev/null
docker rm donotest >/dev/null 2>/dev/null
docker run -d --name donotest -p 80:80 0lmi/donotest >/dev/null 2>/dev/null
rm ~/Desktop/index.html

n=0

while true; do
    let n=$n+1
    curl http://127.0.0.1 >/dev/null 2>/dev/null
if [ $? -eq 0 ]; then
    sleep 2
    docker cp donotest:usr/local/apache2/htdocs/index.html ~/Desktop/ | grep -v successfully
    htmlval -w -l ~/Desktop/index.html | grep -v "Comment\|File" | sed 's/[=]//g'
    break
elif [ $n -eq 1915 ]; then
    echo "15sec Error"
    break
fi
done
}

