
def write(fname,lname):
    with open('user.txt', 'a') as writer:
        writer.write(f"\n {fname}, {lname}")