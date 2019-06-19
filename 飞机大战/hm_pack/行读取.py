file=open("send_message.py")
while True:

    text=file.readline()
    if not  text:
        break
    print(text,end="")

file.close()