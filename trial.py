import os
files=os.listdir("static\images")
for i in files:
    os.remove(f"static/images/{i}")
    # print(i)