#!/usr/bin/python

arr=raw_input("enter the string - ")
arr = arr.split()
A=""
for i in range(len(arr)) :
	A+=arr[i]+"*"
print A
