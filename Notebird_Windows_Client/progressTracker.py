import sys, time

# sys.stdout.write("here is the first string")
print("here is FIRST text")
sys.stdout.flush()
time.sleep(2)
sys.stdout.seek(0)
print("\r")
# sys.stdout.write("here is the second thing")
print("Second text")