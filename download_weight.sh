#!/bin/bash

cd pretrained_weights
wget -O TimeSformer_divST_8x32_224_K600.pyth "https://www.dropbox.com/s/4h2qt41m2z3aqrb/TimeSformer_divST_8x32_224_K600.pyth?dl=1"
wget -O TimeSformer_divST_8x32_224_K400.pyth "https://www.dropbox.com/s/g5t24we9gl5yk88/TimeSformer_divST_8x32_224_K400.pyth?dl=1"
wget -O TimeSformer_divST_8_224_SSv2.pyth "https://www.dropbox.com/s/tybhuml57y24wpm/TimeSformer_divST_8_224_SSv2.pyth?dl=1"
cd ..