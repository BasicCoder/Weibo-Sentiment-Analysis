import numpy as np
import argparse
from datetime import datetime
import json
import os

def get_content(path, start, end):
    # 获取指定时间间隔的博文数据，构建语料库
    content = []
    tmp = ''
    count = 0
    start = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
    for line in open(path, 'r', encoding='UTF-8'):
        tmp += line.strip()
        if line.strip() == '}':
            item = json.loads(tmp)

            if 'created_at' in item:
                create_time = datetime.strptime(item['created_at'], '%Y-%m-%d %H:%M:%S')
                if start <= create_time < end:
                    content.append(item['content'])
                    count += 1
            tmp = ''

    print(start, end, count)
    return content

def save_data(path, data_list):
    json_list = []
    for stc, label in data_list:
        sample = {}
        sample['content'] = stc
        sample['overall-label'] = label
        json_list.append(json.dumps(sample))
    json_list = '\n'.join(json_list)
    with open(path, 'w') as w:
        w.write(json_list)

def main():
    parser = argparse.ArgumentParser()
    ## Required parameters
    parser.add_argument("--data_path", default="./data/Comments.json", type=str,
                        help="The input data dir. Should contain the .json files (or other data files) for the task.")
    args = parser.parse_args()

    #需要进行聚类的文本集
    timeslices=[("2018-10-28 10:00:00", "2018-10-28 17:45:59"),("2018-10-28 17:46:00", "2018-11-02 10:16:59"),
                ("2018-11-02 10:17:00", "2018-11-03 23:59:59"),("2018-11-04 00:00:00", "2018-11-05 23:59:59")]

    for start, end in timeslices:
        data_list = []
        contents = get_content(args.data_path, start, end)
        len_contents = len(contents)
        label = [0]*len_contents
        data_list = list(zip(contents, label))

        filename = start.replace(' ', '-').replace(':', '-') + "---" + end.replace(' ', '-').replace(':', '-') + ".json"
        save_data(os.path.join('./data', filename), data_list)
        print(len(data_list))

    

if __name__ == "__main__":
    main()