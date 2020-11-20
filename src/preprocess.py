f_in = open("data/groundtruth.txt", "r")
f_out = open("data/groundtruth_out.txt", "w")

txt = f_in.read()
txt = txt.lower()
txt = txt.replace('\n','')
print(txt)

punc = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for ele in txt:
    if ele in punc:
        txt = txt.replace(ele, " ")  

f_out.write(txt)

f_in.close()
f_out.close()