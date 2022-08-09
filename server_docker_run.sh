#!/bin/bash
image_name="attitude_estimator_in_TimeSformer"
tag_name="docker"
script_dir=$(cd $(dirname $0); pwd)

docker run -it \
    --net="host" \
    --gpus all \
    --privileged \
    --shm-size=400g \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --name="attitude_estimator_in_TimeSformer" \
    --volume="$script_dir/:/home/pycode/$image_name/" \
    --volume="/home/kawai/ssd_dir/:/home/ssd_dir/" \
    --volume="/fs/kawai/:/home/strage/" \
    $image_name:$tag_name