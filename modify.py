import os 
import sys
p='./'
if len(sys.argv)>1:
    p=sys.argv[1]
    
g = os.walk(p)  

# print(os.path.join(path,'convert/', dir_name))
i=0
for path,dir_list,file_list in g: 
    if i==0:
        try:
            os.mkdir(p+'convert')
        except:
            pass
    for dir_name in file_list:
        if not dir_name.startswith('.'):
            with open(os.path.join(path, dir_name),'r',encoding='utf-8') as f:
                content=''
                for ch in f.read():
                    if '\u4e00'<= ch <= '\u9fff':
                        content=content+'**'
                    else:
                        content=content+ch
                with open(os.path.join(path,'convert/', dir_name),'w') as f2:
                    f2.write(content)
    i=i+1
                
#         print(os.path.join(path, dir_name) )

# with open('./data_test/tt.txt','r',encoding='utf-8') as f:
#     print(f.read())
