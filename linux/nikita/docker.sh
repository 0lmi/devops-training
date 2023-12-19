#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

global_start=`date +%s`

cleanup() {
    if [ -f index.html ]; then
        rm -f index.html
    fi
    if [ -d tmpf ]; then
        rm -rf tmpf
    fi
    docker stop donotest >/dev/null 2>/dev/null
    docker rm donotest >/dev/null 2>/dev/null
    global_end=`date +%s`
    echo "Total script execution time: $(( $global_end-$global_start )) seconds."
}
trap cleanup EXIT

mkdir tmpf
start=`date +%s`
docker run -d --name donotest -p 80:80 0lmi/donotest >/dev/null 2>/dev/null
exit_code=$?
if [ $exit_code -ne 0 ]; then
    echo "ERROR: unable to start docker container"
    exit $exit_code
fi

while true; do
  let n=$n+1
  curl http://127.0.0.1 >/dev/null 2>/dev/null
  if [ $? -eq 0 ]; then
      end=`date +%s`
      docker cp donotest:usr/local/apache2/htdocs/index.html $SCRIPT_DIR >/dev/null 2>/dev/null

      OUTPUT=$( mktemp -p $SCRIPT_DIR/tmpf )
      curl -s -H "Content-Type: text/html; charset=utf-8" --data-binary @index.html \
          https://validator.w3.org/nu/?out=gnu >> $OUTPUT

      val_errors=$( grep -i Error $OUTPUT | wc -l)
      val_warnings=$( grep -i warning $OUTPUT | wc -l )

      if [ $val_errors -ge 1 ]; then
          echo "Validation not passed, errors: $val_errors warnings: $val_warnings"
      else
          echo "Validation passed, warnings: $val_warnings"
      fi

      docker stop donotest >/dev/null 2>/dev/null
      break
  elif [ $(($(date +%s)-$start)) -ge 15 ]; then
      echo "15sec Error"
      exit
  fi
done

echo "Container fist answer detected in: $(($end-$start)) seconds."
