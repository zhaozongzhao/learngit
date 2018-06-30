import pickle
d = dict(name = 'Bob',age=20,score =88)
print(pickle.dumps(d))

f =open('dump.txt','wb')
pickle.dump(d,f)
f.close()

with open('dump.txt','rb') as f:
    d = pickle.load(f)
    f.close()

print(d)