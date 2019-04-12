#!/bin/bash

HOST_IP=$(docker-machine ls |grep default | awk {'print $5'} | cut -f 2-2 -d : | sed "s/\/\///")
#echo $HOST_IP
CONTAINERS=$(docker ps | grep 9092 | awk '{print $1}')
BROKERS=$(for CONTAINER in ${CONTAINERS}; do docker port "$CONTAINER" 9092 | sed -e "s/0.0.0.0:/$HOST_IP:/g"; done)
echo "${BROKERS/$'\n'/,}"
