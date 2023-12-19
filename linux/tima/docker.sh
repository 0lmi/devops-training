#!/bin/bash

docker stop donotest >/dev/null 2>/dev/null
docker rm donotest >/dev/null 2>/dev/null
docker pull 0lmi/donotest >/dev/null 2>/dev/null
docker run -d --name donotest -p 80:80 0lmi/donotest >/dev/null
start=$(date +%s.%N)

while true; do
    curl http://127.0.0.1 >/dev/null 2>/dev/null
    if [ $? -eq 0 ]; then
		end=$(date +%s.%N)
        break
    fi
done


dur=$(echo "$end - $start" | bc)
LC_NUMERIC="en_US.UTF-8" printf "Execution time: %.6f seconds\n" $dur

