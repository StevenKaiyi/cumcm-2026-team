# 近五年国赛试题索引（2021-2025）

本目录按 A-E 题分类，收录全国大学生数学建模竞赛官网的试题名称、简要主题说明和官方来源链接。

## 版权与使用方式

全国大学生数学建模竞赛官网页脚标注 `All Rights Reserved`，未提供允许在公开仓库重新分发完整试题及附件的许可证。因此，本仓库不镜像原始 PDF、数据附件或完整逐字转写。

队员可运行以下命令，将五届官方压缩包直接下载并按 A-E 题整理到本机的 `documents/_local/`。该目录已被 Git 忽略，不会上传到 GitHub。

```powershell
powershell -ExecutionPolicy Bypass -File .\documents\download-official.ps1
```

如需在本地生成可检索的 Markdown 文本，可先安装 `pypdf`，再运行：

```powershell
python .\documents\convert-local-pdfs.py
```

转换结果位于 `documents/_local/markdown/`，同样不会被 Git 跟踪。PDF 文本抽取可能丢失公式、图形或排版，阅读和复现时应以官方 PDF 为准。

## 分类入口

- [A 题](A/README.md)
- [B 题](B/README.md)
- [C 题](C/README.md)
- [D 题](D/README.md)
- [E 题](E/README.md)

## 官方归档

- [历年竞赛赛题](https://www.mcm.edu.cn/html_cn/block/8579f5fce999cdc896f78bca5d4f8237.html)
- [2025 年赛题页面](https://www.mcm.edu.cn/html_cn/node/03c91a444e62eee81a3740fa97a461a6.html)
- [2024 年赛题页面](https://www.mcm.edu.cn/html_cn/node/a0c1fb5c31d43551f08cd8ad16870444.html)
- [2023 年赛题页面](https://www.mcm.edu.cn/html_cn/node/c74d72127066f510a5723a94b5323a26.html)
- [2022 年赛题页面](https://www.mcm.edu.cn/html_cn/node/388239ded4b057d37b7b8e51e33fe903.html)
- [2021 年赛题页面](https://www.mcm.edu.cn/html_cn/node/90d223833c1eb50f899aa096a66c6896.html)
