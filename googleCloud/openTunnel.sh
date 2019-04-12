#!/bin/bash 

source config.sh

#Kill any open ssh session 
#kill -9 $(ps -ef | grep "gcloud.py compute ssh" | awk '{print $2}')
gcloud compute ssh ${cluster_name}-m \
--project=${gcp_project} \
--zone=$zone -- \
-D ${ssh_port} -N 


