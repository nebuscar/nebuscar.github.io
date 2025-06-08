---
date: "2025-01-17 12:14"
title: "Pipeline for classification of TCR&MHCs"
---

# 1.获取PDB数据集

## 1.1筛选PDB文件，仅包含TCR-MHC
---
    如何筛选？
    如何批量下载？
    数据量多大？
---

---
Q1:如何筛选？  
    1.Advanced Search  
    2.Additional Structure Keywords ---- TCR-pMHC,complex  
    3. Structure Title ---- TCR-pMHC,complex  
    4.物种：Homo sapiens  
    5.分辨率：0.5-1.5A  
    ![查询条件](/images/image-1.png)






---
[参考1-CSDN：PDB数据库数据查看和下载](https://blog.csdn.net/qq_27390023/article/details/142143693)
[参考2-知乎：一键从PDB数据库批量下载蛋白质结构文件](https://zhuanlan.zhihu.com/p/4136813710)
---

## 1.2

# 2.计算Protein contact map并生成contact map特征矩阵
---
[参考1-CSDN：蛋白质Pdb文件的氨基酸接触网络矩阵生成](https://blog.csdn.net/Liu_sirrr/article/details/132160588)


# 3.训练二分类模型

---
    1.可选择CNN，FC，选择tensorflow框架
    2.以第2步获得的contact map特征矩阵为输入
---

## 3.1Tensorflow-CNN网络构建

## 3.2训练模型，调参

## 3.3模型评估