import requests
import platform
import os

sys = platform.system()
dataset_cmd = "python dataset/prepare_data.py -fold=1 -num_folds=1024 -base_fn=dataset/tf/data_1024 -input_fn=dataset/data -max_seq_length=1024 > tf.log"
train_cmd = "python train/train1.py --config_file=configs/mega.json --input_file=dataset/tf/data_1024train_wiki19_0001.tfrecord --output_dir=models/mega/ --max_seq_length=1024 --train_batch_size=512 --learning_rate=1e-4 --num_train_steps=30000 --num_warmup_steps=10000 --save_checkpoints_steps=1000 --iterations_per_loop=1000 --use_tpu=False --tpu_name=None --num_tpu_cores=256 --init_checkpoint=models/mega/model.ckpt-100000 > train.log"
generate_cmd = "python scripts/interactive_conditional_samples.py -model_config_fn configs/mega.json -model_ckpt models/mega/model.ckpt-100000 -eos_token 511 -min_len {} -samples {} -inp_text {} -id {} -type {}"

if sys == "Windows":
    rm_file_cmd = r"del /q dataset\data\*"
else:
    rm_file_cmd = "rm -f dataset/data/*"


def bytes2str(data):
    if isinstance(data, bytes):
        try:
            data = data.decode('utf-8')
        except:
            data = data.decode('gbk')
    data = data.strip()
    return data


def get_cmd_popen(cmd):
    os.system(cmd)


def post_requests(json_data):
    return requests.post("http://10.huangtongwei.cn:8099/v1/ai/result", json=json_data)


def get_requests(id_num, files):
    file_list = files.split(",")
    for file in file_list:
        print("file name is ", file)
        rs = requests.get("http://10.huangtongwei.cn:8099/v1/ai/task/file/{}/{}".format(id_num, file))
        with open("dataset/data/{}".format(file), 'w', encoding="utf-8") as f:
            f.write(rs.text)
