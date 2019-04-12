#!/bin/bash 

source config.sh

#kill -9 $(ps -ef | grep openJupyther| awk {'print $2'})

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --proxy-server="socks5://localhost:${ssh_port}" \
  --host-resolver-rules="MAP * 0.0.0.0 , EXCLUDE localhost" \
  --user-data-dir=/tmp/${cluster-name}-m
