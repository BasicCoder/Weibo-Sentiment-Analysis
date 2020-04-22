# Weibo Sentiment Analysis
1. 基于[开源代码](https://github.com/real-brilliant/bert_chinese_pytorch)中改写的
2. 大多数情感分析模型只是开源代码，没有提供对应预训练模型。针对微博情感分析同样也缺乏相应的预训练模型，本模型提供情感分析训练代码，以及模型推断
3. 主要针对的数据集
   | 数据集                | 类型                             |                                                     链接                                                      |
   | :-------------------- | -------------------------------- | :-----------------------------------------------------------------------------------------------------------: |
   | weibo_senti_100k      | 2种感情，正向评论和负向评论      |   [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb)    |
   | simplifyweibo_4_moods | 4 种情感，喜悦、愤怒、厌恶、低落 | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/simplifyweibo_4_moods/intro.ipynb) |

## Environmental preparation
This repo was tested on 3.6 and PyTorch 0.4.1/1.0.0
```shell
pip install pytorch-pretrained-bert
```

## Model Train
采用 `BERT-base, Chinese`<sup>Google</sup> 模型在数据集上进行fine-tune
### 准备数据集
划分 Train、Valid、Test 数据集
```shell
cd Weibo-Sentiment-Analysis
python split_weibo_senti_100k.py
```
### 模型训练
```shell
sh train.sh
```

| 模型         |        数据集         |         F1         |
| :----------- | :-------------------: | :----------------: |
| Bert-base    |   weibo_senti_100k    | 0.9840746441110737 |
|              | simplifyweibo_4_moods | 0.4969952552559987 |
| Bert-wwm-ext |          --           |
| XLNet-base   |          --           |
| XLNet-mid    |          --           |
| XLNet-large  |          --           |
| Roberta-mid  |          --           |



## Model Test

预训练模型下载：

| 模型      |        数据集         | 下载地址 |
| :-------- | :-------------------: | -------: |
| Bert-base |   weibo_senti_100k    | [地址]() |
|           | simplifyweibo_4_moods | [地址]() |

将下载下来的模型文件保存在```./checkpoints``` 目录下

```shell
sh test.sh
```

