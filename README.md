- generate_document_cls_script.py
```
  Label Studio Object Detection with Bounding Boxes，根据文件夹分类直接生成json文件,不需要一个一个标注。

  目录结构: 按照分类建立文件夹
           |--- 身份证
  images---|--- 银行卡
           |--- 合同
  
  1. 遍历images文件夹下所有的文件夹
  2. 每个文件夹的名称就是分类的名称
```
