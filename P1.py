from zipfile import ZipFile
import patoolib as p
f="names.zip"
z=ZipFile(f)
z=z.namelist()
p.extract_archive("names.zip")
t=[]
for i in z:
    a=open("names/"+i,'r')
    b=a.read()
    print(b)
    b=str(b)
    t.append(b)
a.close()
op=open("output.txt",'w')
for i in t:
    op.write(i)
op.close()
p.create_archive("final_output.zip",("output.txt",))

