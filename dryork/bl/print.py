name =['a1','a2','a3']
seq=['seq11111','seqs22222','seq33333']
f = open("c:/test.txt", "w+")
f.write("name\tseq\n")
for i in range(0, len(name)):
    f.write(name[i] + "\t" + seq[i] + "\n")
f.close()