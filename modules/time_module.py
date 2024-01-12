import time 

i = 0
start = time.time()
while i < 100000000:
  i+=1
print(i)

end = time.time()
elapsed = end - start
print(f"Elapsed time: {elapsed} seconds")