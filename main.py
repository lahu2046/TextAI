import requests
import time
import argparse
from apis import func_dict

parser = argparse.ArgumentParser(description='-t 每次轮询时间')
parser.add_argument(
    '-t',
    dest='t',
    type=int,
    default=10,
    help='int default 10',
)

args = parser.parse_args()
t = args.t
print("当前轮询时间：{}秒".format(t))


def main():
    num = 0
    while True:
        num += 1
        time.sleep(t)
        try:
            rs_json = requests.get("http://10.huangtongwei.cn:8099/v1/ai/task").json()
        except Exception as e:
            print(e)
            input("请求异常，请检测问题, 按回车重试")
            continue
        type_num = rs_json.get("type")
        print("轮询第{}次： {}".format(num, rs_json))
        if not type_num:
            continue
        else:
            func_dict.get(str(type_num))(rs_json)


if __name__ == '__main__':
    main()
