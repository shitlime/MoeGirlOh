<h1 align="center">✨MoeGirlOh</h1>

<div align="center">为了获得所有萌娘词条。</div>

--------------------------------------------------

## 1️⃣项目说明

由于<span style="background-color: #252525; color: #252525;" onmouseover="this.style.color='white';" onmouseout="this.style.color='#252525';">萌娘百科长期以来官方API较为繁琐，并且不提供所有词条（仅词条标题不包含其他）数据。</span>

词条标题作为词语具有一定价值，例如：制作输入法词库、分析流行用语趋势等。

本项目旨在获取所有萌娘词条，按计划会定期发布到[release](https://github.com/shitlime/MoeGirlOh/releases)。


## 2️⃣如何使用

1. 克隆仓库并进入文件夹。
```shell
git clone https://github.com/shitlime/MoeGirlOh.git
cd MoeGirlOh
```

2. 运行脚本。
```shell
python moegirl-all.py
```


## 3️⃣运行时out文件夹中的文件说明

+ `萌娘词条.txt`    全部词条
+ `萌娘词条a.txt`    过程中累积记录的词条（很可能不完全，用于Debug，会占用一定空间需手动删除）
+ `nextPage`    用于爬取中断与恢复


## 声明

**本项目仅供学习参考，请勿用于非法用途。**  

**使用本项目产生的一切后果自行承担，开发者不承担任何责任。**  