#!/usr/bin/env bash


NUM_FOLDS=1024
MAX_SEQ_LENGTH=1024
FN=dataset/data
OUT_BUCKET=dataset/tf

#PYTHONPATH=$(pwd) python dataset/prepare_data.py -fold=1 -num_folds=1024 -base_fn=dataset/tf/data_1024 -input_fn=dataset/data -max_seq_length=1024 > tf_log.txt
