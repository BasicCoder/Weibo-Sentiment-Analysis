# Weibo Sentiment Analysis
1. 基于[开源代码](https://github.com/real-brilliant/bert_chinese_pytorch)中改写的
2. 大多数情感分析模型只是开源代码，没有提供对应预训练模型。针对微博情感分析同样也缺乏相应的预训练模型，本模型提供情感分析训练代码，以及模型推断
3. 主要针对的数据集
   | 数据集           |                                                   链接                                                   |
   | :--------------- | :------------------------------------------------------------------------------------------------------: |
   | weibo_senti_100k | [地址](https://github.com/SophonPlus/ChineseNlpCorpus/blob/master/datasets/weibo_senti_100k/intro.ipynb) |
   |                  |                                                                                                          |

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

| 模型         |         F1         |
| :----------- | :----------------: |
| Bert-base    | 0.9840746441110737 |
| Bert-wwm-ext |         --         |
| XLNet-base   |         --         |
| XLNet-mid    |         --         |
| XLNet-large  |         --         |
| Roberta-mid  |         --         |



## Model Test
```shell
sh test.sh
```

