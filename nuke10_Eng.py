import os;

def nuke(n):
    a=[];
    for i in range(10):
        if(n>1):
            a.append(nuke(n-1));
        else:
            a.append(i);
    return a;
print(nuke(int(input("Enter a number (never more than 10)"))));

os.system("pause");