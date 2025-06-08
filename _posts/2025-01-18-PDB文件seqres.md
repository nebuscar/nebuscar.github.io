---
title: "理解PDB文件中seqres记录类型"
author: "Zhu Ni"
date: "2025-01-18 16:46"
---

### `SEQRES` 是什么？

`SEQRES` 是 **PDB 文件**（蛋白质数据银行文件）中的一种记录类型，用来描述蛋白质或核酸的序列信息，尤其是 **氨基酸序列**（对于蛋白质）或 **核苷酸序列**（对于核酸）。这些记录通常用于表示蛋白质或核酸的原始序列，而 **ATOM** 记录则包含了该序列中每个原子的位置、类型等结构信息。

- **SEQRES** 行通常用来记录蛋白质的氨基酸序列（或者核酸的核苷酸序列），并不关心这些氨基酸是否在三维空间中被解析出来。也就是说，`SEQRES` 行可以包含完整的氨基酸序列，尽管在三维结构解析时，有些氨基酸可能因为没有被观测到而没有对应的 `ATOM` 记录。

### SEQRES 的结构：
每个 `SEQRES` 行都包含多个字段，描述一个或多个链的氨基酸序列。具体结构如下：

```
SEQRES   <序号> <链标识符> <氨基酸1> <氨基酸2> ... <氨基酸N>
```

- **序号**：表示这是第几条 `SEQRES` 记录。每个 `SEQRES` 行对应一个氨基酸序列。
- **链标识符**：表示该序列所属的链。一个蛋白质可能包含多个链，每个链都会有一条 `SEQRES` 记录。
- **氨基酸序列**：列出了从 N 端到 C 端的氨基酸序列。

### 举个例子：
假设我们有一个包含氨基酸序列的蛋白质 PDB 文件中的 `SEQRES` 行：

```
SEQRES   1 A   20  ALA GLY LEU VAL SER ASN GLY ASP ARG LEU GLU ALA CYS PRO 
SEQRES   2 A   20  PHE GLU GLY MET ASN ILE CYS LYS GLY VAL LEU TYR GLY 
```

#### 解释：
- **`SEQRES   1 A`** 表示第 1 条 `SEQRES` 记录，描述了链 A 的氨基酸序列。
  - 序列：`ALA GLY LEU VAL SER ASN GLY ASP ARG LEU GLU ALA CYS PRO`，表示链 A 从 N 端到 C 端的第 1 到第 12 个氨基酸。
  
- **`SEQRES   2 A`** 表示第 2 条 `SEQRES` 记录，继续描述链 A 的氨基酸序列。
  - 序列：`PHE GLU GLY MET ASN ILE CYS LYS GLY VAL LEU TYR GLY`，表示链 A 从第 13 到第 24 个氨基酸。

### 注意：
- **SEQRES 记录** 只是描述了蛋白质的氨基酸序列（可能是一个或多个链），它并不提供氨基酸的位置、相对结构信息或原子坐标。
- **ATOM 记录** 会提供这些氨基酸的三维坐标信息，告诉我们这些氨基酸在空间中的具体位置。

### SEQRES 和 ATOM 的关系：
- **SEQRES** 行用于表示氨基酸的序列，但并不表示这些氨基酸的实际结构。
- **ATOM** 行才是真正描述氨基酸如何在三维空间中折叠的记录。某些氨基酸可能有对应的 `ATOM` 记录，也可能没有，因为它们可能由于解析限制（如数据缺失）而未被观察到。

### 例子中的 `SEQRES` 和 `ATOM`：
假设同一个 PDB 文件中，`SEQRES` 和 `ATOM` 行的内容如下：

**SEQRES**（描述序列）：
```
SEQRES   1 A   20  ALA GLY LEU VAL SER ASN GLY ASP ARG LEU GLU ALA CYS PRO 
SEQRES   2 A   20  PHE GLU GLY MET ASN ILE CYS LYS GLY VAL LEU TYR GLY 
```

**ATOM**（描述空间位置）：
```
ATOM      1  N   ALA A   1      11.104  22.398   9.532  1.00 20.00           N  
ATOM      2  CA  ALA A   1      10.051  21.258   9.019  1.00 20.00           C  
ATOM      3  C   ALA A   1       8.703  21.623   8.392  1.00 20.00           C  
ATOM      4  N   GLY A   2       8.186  22.703   8.618  1.00 20.00           N  
```

#### 解释：
- **SEQRES** 行表示链 A 的氨基酸序列，包括 24 个氨基酸。
- **ATOM** 行表示链 A 中氨基酸的原子坐标（例如 `ALA` 的第一个氨基酸的氮原子 `N`，第二个氨基酸的氨基酸 `CA` 等）。
  
尽管 `SEQRES` 行表示了 24 个氨基酸，实际的 `ATOM` 行可能只包含一部分，因为某些氨基酸的原子坐标可能没有被解析或没有测量数据。

### 总结：
- `SEQRES` 是 PDB 文件中用于描述氨基酸（或核苷酸）序列的记录。
- 它提供了蛋白质的氨基酸序列信息，但不包含三维结构数据。
- `ATOM` 记录提供了每个氨基酸的原子位置等三维结构信息。