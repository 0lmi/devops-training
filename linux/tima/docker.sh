#!/bin/bash

docker stop donotest
docker rm donotest
docker run -d --name donotest -p 80:80 0lmi/donotest

n=0
while true; do
    let n=$n+1
    curl http://127.0.0.1 >/dev/null 2>/dev/null
    if [ $? -eq 0 ]; then
        break
    fi
done
echo $n

