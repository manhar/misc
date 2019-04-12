#!/bin/bash 

region=$1

region=europe-west2

export cluster_name=$( gcloud dataproc --region $region clusters list | tail  -n 1 | awk {'print $1'} )

#get running cluster name

if [ ! -z $cluster_name  ]
then 
	gcloud dataproc --quiet  --region $region clusters delete $cluster_name 
else 
	echo "Nothing to tear down"
       exit 1
fi 
