import hashlib

m2 = hashlib.md5()
scc = "this is a md5 test."
m2.update(scc.encode("utf-8"))
print("output:", m2.hexdigest())
























