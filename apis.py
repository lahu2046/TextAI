from utils.util import get_cmd_popen, dataset_cmd, train_cmd, \
    generate_cmd, rm_file_cmd, post_requests, get_requests


def generate_ai(rs_json):
    get_cmd_popen(
        generate_cmd.format(
            rs_json.get("len", 1024),
            rs_json.get("count"),
            rs_json.get("keyword"),
            rs_json.get("id"),
            rs_json.get("type")
        )
    )


def train_ai(rs_json):
    get_requests(rs_json.get("id"), rs_json.get("files"))
    get_cmd_popen(dataset_cmd)
    get_cmd_popen(rm_file_cmd)
    print("预处理完成, 准备执行训练")
    get_cmd_popen(train_cmd)
    """训练完成"""
    rs_json['status'] = 1
    print("训练完成：", rs_json)
    post_requests(rs_json)


def train_and_generate_ai(rs_json):
    get_requests(rs_json.get("id"), rs_json.get("files"))
    get_cmd_popen(dataset_cmd)
    get_cmd_popen(rm_file_cmd)
    print("预处理完成, 准备执行训练")
    get_cmd_popen(train_cmd)
    print("训练完成，准备执行生成")
    get_cmd_popen(
        generate_cmd.format(
            rs_json.get("len"),
            rs_json.get("count"),
            rs_json.get("keyword"),
            rs_json.get("id"),
            rs_json.get("type")
        )
    )
    print("训练和生成完成")


func_dict = {
    "1": generate_ai,
    "2": train_ai,
    "3": train_and_generate_ai,
}
