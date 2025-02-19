a="bhoomika"

print(a[1])
b="bh oo mi ka"
print(b[3])

#to find lenght of the string len() function is used
print(len(a))
print(len(b))

# the below gives error index error because of out of range
#c="sky is blue"
#print(c[11])
'''Traceback (most recent call last):
  File "C:\Users\bhoom\dlitheinternship\day2\stringsarr.py", line 7, in <module>
    print(c[11])
          ~^^^^
IndexError: string index out of range'''


d,e,f="hello","good","afternoon"
print(len(d))
g=""" hey
  every one
   good afternoon"""
print(g)
print(len(g))