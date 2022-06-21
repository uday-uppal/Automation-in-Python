import hub
import subprocess as sp
dataset=input("Enter the name of the datasset")
first=f"ds = hub.load('hub://activeloop/{dataset}')"
f = open("demofile2.py", "w")
f.write("import hub\n"+ first + "\nprint(ds)")
f.close()
third = sp. getoutput('python demofile2.py')
second_aux=third
s=second_aux.find("[")
second_aux=second_aux[s+1:len(second_aux)-2]
second_aux=second_aux.replace("'","")
second_aux=second_aux.replace(" ","")
sec_l=second_aux.split(",")
idx=-1
for i in range(len(sec_l)):
    if(sec_l[i]=="images"):
        idx=i
        break
if (idx!=-1):
    del sec_l[idx]     
t=third.find("Dataset")
third=third[t:len(third)]
l=sec_l
l1=[]
for i in range(len(sec_l)):
    l1.append(l[i] + " : " + " {ds."+l[i]+"[0].numpy()}")
l2=""
for i in range(len(sec_l)):
    if(i!=len(sec_l)-1):
        l2=l2+l1[i]+","
    else:
        l2=l2+l1[i]
second=l2
print('''

### How to use with Hub
A simple way of using this dataset is with [Activeloop](https://activeloop.ai)'s python package [Hub](https://github.com/activeloopai/Hub)!

First, run `pip install hub` (or `pip3 install hub`). 

```python
import hub \n'''+first
+
'''
\n#check out the first image and all of its details!
import matplotlib.pyplot as plt\n''' +
      
'''plt.imshow(ds.images[0].numpy()) \n''' +
      
'''plt.title(f" ''' + second+'''")'''
+'''\nplt.show() \n '''
+'''
# train a model in pytorch
for sample in ds.pytorch():
    # ... model code here ...
    
# train a model in tensorflow
for sample in ds.tensorflow():
    # ... model code here ...
```
available tensors can be shown by printing dataset:

```python
print(ds) \n
# prints: ''' + third +

'''\n```

\nFor more information, check out the [hub documentation](https://docs.activeloop.ai/).
      ''')
