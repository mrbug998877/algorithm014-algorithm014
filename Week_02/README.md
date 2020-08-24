学习笔记
二叉树的前、中、后知识点学习掌握；
熟悉python的二叉树前中后的编写；
1. 对于前k个高频单词这道题目，对于匿名函数+字典的使用更加深刻，看国际版leetcode讨论，对于本题目中：
    key = lambda word:(~freqs[word],word)

    ~Freqs[word]意思是降序排列单词出现的频次（此为lambda函数的第一个排序条件）
    
    word将已经根据频次排好序的单词，根据字母顺序再次排序（此为lambda函数的第二个排序条件）

    最后nsmallest()返回前k个结果