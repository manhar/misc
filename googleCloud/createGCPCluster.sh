#!/bin/bash

#export region="europe-west2"
#export cluster_name="spark-cluster"
#export zone="europe-west2-a"

source config.sh

gcloud dataproc clusters create $cluster_name \
     --async \
     --project=${gcp_project} \
     --region=$region \
     --zone=$zone\
     --image-version=1.3 \
     --num-masters=1 \
     --master-boot-disk-size=32GB \
     --master-machine-type=n1-standard-2 \
     --worker-boot-disk-size=32GB \
     --worker-machine-type=n1-standard-1 \
     --num-workers=4 \
     --initialization-actions=gs://dataproc-initialization-actions/jupyter2/jupyter2.sh

echo  "Creating google cluster ${cluster_name}"
while [ $(gcloud dataproc --region=europe-west2  clusters list | tail  -n 1 | awk {'print $3'}) == "CREATING" ]
do 
	/bin/echo -n "."
	sleep 5
done

echo "Google cluster ${cluster_name}: RUNNING"

exit 0

gcloud compute ssh  --zone=$zone  --ssh-flag="-D" --ssh-flag="10000" --ssh-flag="-N" $cluster_name
