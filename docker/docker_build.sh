#!/bin/bash

image_name='attitude_estimator_in_TimeSformer'
image_tag='docker'

docker build -t $image_name:$image_tag --no-cache .