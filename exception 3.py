try:
    a=open("exception.py","w+")
    try:
        a.write("xyzthis is s17 section")
    finally:
        a.close()
except IOError:
    print("file not found")
else:
    print("the file opened successfully")
    a.close()