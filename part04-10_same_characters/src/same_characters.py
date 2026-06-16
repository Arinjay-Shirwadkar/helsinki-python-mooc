def same_chars(s,p1,p2):
    if p1>=len(s) or p1<0 or p2>=len(s) or p2<0:
        return False
    if s[p1] ==s[p2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 11))