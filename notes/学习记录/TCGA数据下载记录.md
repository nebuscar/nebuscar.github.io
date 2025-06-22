---
日期: 2025-06-22
项目: RE-EC-MDKNCL
工具: R / Bioconductor / TCGAbiolinks
---
---

## 问题
- 我想复现一篇【单细胞+空转】的生信分析文章，其部分数据来源于TCGA，而由于美国川普政府24年禁止中国ip访问下载NCBI-TCGA数据，我无法直接从网页下载获取。
- 经多方搜索，发现可以通过R包`TCGAbiolinks`进行下载。

---

## 📌 数据来源
- 项目名称：**TCGA-UCEC**（Uterine Corpus Endometrial Carcinoma）
- 数据平台：GDC Data Portal（https://portal.gdc.cancer.gov）
- 下载方式：R 语言 `TCGAbiolinks` 包
- 数据类型：
  - 原始表达矩阵（RNA-Seq count，STAR - Counts）
  - 临床数据（Patient XML）

---

## 🧰 软件环境

```r
# 安装 Bioconductor 和 TCGAbiolinks
if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("TCGAbiolinks")

########## 1. library ##########
library(TCGAbiolinks)
library(SummarizedExperiment)
```

---

## 🔍 查询表达数据
```r
########## 2. params ##########
query <- GDCquery(project = 'TCGA-UCEC',
                  experimental.strategy = 'RNA-Seq',
                  data.category = 'Transcriptome Profiling',
                  data.type = 'Gene Expression Quantification',
                  workflow.type = 'STAR - Counts',
                  access = 'open',
                  platform = 'Illumina', 
                  data.format = 'tsv',
                  barcode = FALSE,
                  sample.type = FALSE
                  )
```

## ⬇️ 下载表达数据
```r
GDCdownload(query)
data <- GDCprepare(query)
```

---

## 🧩 TCGAbiolinks核心函数解析总览

| 函数                            | 功能                           | 常见用途                         |
| ----------------------------- | ---------------------------- | ---------------------------- |
| `GDCquery()`                  | 构造查询任务                       | 指定项目、数据类型、工作流等               |
| `GDCdownload()`               | 下载数据文件                       | 执行由 `GDCquery()` 创建的查询任务     |
| `GDCprepare()`                | 加载数据为 `SummarizedExperiment` | 自动整合表达矩阵、样本注释                |
| `GDCprepare_clinic()`         | 提取临床数据                       | 从 xml 文件中解析临床信息              |
| `TCGAquery_SampleTypes()`     | 筛选特定类型样本                     | 例如提取 Tumor / Normal          |
| `TCGAanalyze_Normalization()` | 表达量标准化                       | 通常用于 raw count 数据（如 TMM 标准化） |
| `TCGAanalyze_Filtering()`     | 过滤低表达基因                      |                              |
| `TCGAanalyze_DEA()`           | 差异表达分析                       | 基于 limma-voom、edgeR 等        |
| `TCGAbiolinks::colData()`     | 提取元数据                        | 用于访问样本注释信息                   |

---

## ✅ 函数详解

---

### 🔹 `GDCquery()`

**功能**：创建查询对象，用于定义数据的项目、类型、来源、样本等

```r
query <- GDCquery(
  project = "TCGA-UCEC",
  data.category = "Transcriptome Profiling",
  data.type = "Gene Expression Quantification",
  experimental.strategy = "RNA-Seq",
  workflow.type = "STAR - Counts",
  sample.type = c("Primary Tumor", "Solid Tissue Normal")
)
```

**常用参数**：

|参数|说明|
|---|---|
|`project`|TCGA 项目名（如 `"TCGA-BRCA"`）|
|`data.category`|数据分类（如 `"Transcriptome Profiling"`）|
|`data.type`|数据类型（如 `"Gene Expression Quantification"`）|
|`workflow.type`|流程类型（如 `"HTSeq - FPKM"`、`"STAR - Counts"`）|
|`sample.type`|样本类型筛选（如 `"Primary Tumor"`）|

---

### 🔹 `GDCdownload()`

**功能**：执行实际下载，默认使用 GDC API

```r
GDCdownload(query)
```

**可选参数**：

- `method = "api"`：默认方式，建议使用
    
- `resume = TRUE`：断点续传
    
- `files.per.chunk = 20`：控制并发数，防止失败
    

---

### 🔹 `GDCprepare()`

**功能**：读取下载的数据并构建 `SummarizedExperiment` 对象

```r
se <- GDCprepare(query)
```

**输出结构**：

- `assay(se)`：表达矩阵
    
- `colData(se)`：样本元信息（临床+文件结构）
    
- `rowData(se)`：基因注释
    

---

### 🔹 `GDCprepare_clinic()`

**功能**：提取 XML 临床数据为 data.frame

```r
clinical <- GDCprepare_clinic(query, clinical.info = "patient")
```

**参数 `clinical.info` 可选值**：

- `"patient"`：基本病人信息
    
- `"follow_up"`：随访数据
    
- `"radiation"`, `"drug"`：治疗信息等
    

---

### 🔹 `TCGAquery_SampleTypes()`

**功能**：从表达矩阵中筛选指定样本类型

```r
# 提取 tumor 样本名
tumor_samples <- TCGAquery_SampleTypes(barcode = colnames(se), typesample = "TP")
```

**常用类型值**：

| 代码     | 说明              |
| ------ | --------------- |
| `"TP"` | Primary tumor   |
| `"NT"` | Normal tissue   |
| `"TR"` | Recurrent tumor |

---

### 🔹 `TCGAanalyze_Normalization()`

**功能**：对原始 count 数据进行 TMM 标准化

```r
norm <- TCGAanalyze_Normalization(tabDF = assay(se), geneInfo = geneInfoHT)
```

---

### 🔹 `TCGAanalyze_DEA()`

**功能**：差异表达分析（默认使用 edgeR + voom）

```r
DEA.results <- TCGAanalyze_DEA(
  mat1 = tumor_counts,
  mat2 = normal_counts,
  Cond1type = "Tumor",
  Cond2type = "Normal",
  method = "edgeR"
)
```

---

## ✅ 小结

|模块|常用函数|
|---|---|
|数据获取|`GDCquery` → `GDCdownload` → `GDCprepare`|
|临床信息|`GDCprepare_clinic`|
|样本筛选|`TCGAquery_SampleTypes`|
|表达标准化|`TCGAanalyze_Normalization`|
|差异分析|`TCGAanalyze_DEA`|

---
参考
1. [[基于obsidian软件的第一篇markdown笔记]]