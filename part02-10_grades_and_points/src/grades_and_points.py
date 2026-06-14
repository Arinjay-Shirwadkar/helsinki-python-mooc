m = int(input("Enter your grade"))
gr = ""
if m<0 or m>100:
    gr="impossible!"
elif m<50:
    gr="fail"
elif m<60:
    gr="1"
elif m<70:
    gr="2"
elif m<80:
    gr="3"
elif m<90:
    gr="4"
else:
    gr="5"

print("Grade:",gr)