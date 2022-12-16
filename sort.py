# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 21:11:10 2022

@author: Administrator
"""
#冒泡排序
def BubbleSort(lst):
    n = len(lst)
    if n<=1:
        return lst
    for i in range(0,n):
        for j in range(0,n-i-1):
            if lst[j]>lst[j+1]:
                (lst[j],lst[j+1])=(lst[j+1],lst[j])
    return lst

# 快速排序
    ##分区排序“”
    ##递归分区
def QuickSort(lst):
    # 此函数完成分区操作
    def partition(arr,left,right):
        key = left# 划分参考数索引,默认为第一个数为基准数，可优化
        while left < right:
             # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while left < right and arr[right] >= arr[key] :
                right-=1
            # 如果列表前边的数,比基准数小或相等,则后移一位直到有比基准数大的数出现
            while left < right and arr[left] <= arr[key]:
                left +=1
             # 此时已找到一个比基准大的书，和一个比基准小的数，将他们互换位置 
            (arr[left], arr[right]) = (arr[right], arr[left])
            print(arr[left], arr[right])
        # 当从两边分别逼近，直到两个位置相等时结束，将左边小的同基准进行交换    
        (arr[left], arr[key]) = (arr[key], arr[left])
             # 返回目前基准所在位置的索引
        return left
    def quicksort(arr,left,right):
        if left >= right:
            return
        # 从基准开始分区
        mid = partition(arr,left,right)
         # 递归调用,自己调自己
        # print(arr)
        quicksort(arr,left,mid-1)
        quicksort(arr, mid+1, right)
        
    #主函数 
    n = len(lst)
    if n<1:
        return lst
    quicksort(lst,0,n-1)    
    return lst
#插入排序
def InsertSort(lst):
    n = len(lst)
    if n<1:
        return
    for i in range(0,n):
        j = i #每次循环的一个待插入的数
        target = lst[i]
        while j>0 and target<lst[j-1]:
            lst[j] = lst[j-1]
            j=j-1
        lst[j]=target            #把target插到空位
    return lst
       
# 希尔排序

def ShellSort(lst):
    n = len(lst)
    gap =n//2  #设置增量序列
    print('gap:', gap)
    while gap > 0:
        for i in range(gap,n):
            j = i
            while j>= gap and lst[j-gap] > lst[j]:
                lst[j - gap], lst[j] = lst[j], lst[j - gap]
                j -= gap
        gap = gap // 2
    return lst
                
#选择排序
def SelectSort(lst):
    n=len(lst)
    if n<=1:
        return lst
    for i in range(0,n-1):
        minIndex=i
        for j in range(i+1,n):          #比较一遍，记录索引不交换
            if lst[j]<lst[minIndex]:
                minIndex=j
        if minIndex!=i:                     #按索引交换
            (lst[minIndex],lst[i])=(lst[i],lst[minIndex])
    return lst

#堆排序

def  HeapSort(lst):
    def heapadjust(arr,start,end):  #将以start为根节点的堆调整为大顶堆
        temp=arr[start]
        son=2*start+1           
        while son<=end:
            if son<end and arr[son]<arr[son+1]:  #找出左右孩子节点较大的
                son+=1
            if temp>=arr[son]:       #判断是否为大顶堆
                break
            arr[start]=arr[son]     #子节点上移
            start=son                     #继续向下比较
            son=2*son+1
        arr[start]=temp             #将原堆顶插入正确位置
#######
    n=len(lst)
    if n<=1:
        return lst
    #建立大顶堆
    root=n//2-1    #最后一个非叶节点（完全二叉树中）
    while(root>=0):
        heapadjust(lst,root,n-1)
        root-=1
    #掐掉堆顶后调整堆
    i=n-1
    while(i>=0):
        (lst[0],lst[i])=(lst[i],lst[0])  #将大顶堆堆顶数放到最后
        heapadjust(lst,0,i-1)    #调整剩余数组成的堆
        i-=1
    return lst

# 归并排序、

def MergeSort(lst):
    def merge(left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
    
            print('------------------------->', result)
    
        result += left[l:]
        result += right[r:]
        return result

    def merge_sort(lst):
        if len(lst) <= 1:
            return lst
        # 二分分解
        num = len(lst) // 2
    
        left = merge_sort(lst[:num])  # list1[:2]  12,5  2//2    --->[12]
    
        right = merge_sort(lst[num:])  # --->[5]
        return merge(left, right)
    merge_sort(lst)
    return lst
       


#x=input("请输入待排序数列：\n")
#y=x.split()
#arr=[]
#for i in  y:
#    arr.append(int(i))
arr = [54,25,32,14,54,78,95]    
arr= MergeSort(arr)
#print(arr)
print("数列按序排列如下：")
for i in arr:
    print(i,end=' ')
