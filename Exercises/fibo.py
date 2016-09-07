def fib(n):
    a,b=0,1;
    while(a<n):
        print(a,end=' ');
        a,b=b,a+b;
        
def fib2(n):
    a,b=0,1;
    result=[];
    while(a<n):
        result.append(a);
        a,b=b,a+b;
    return result;


if __name__ == "__main__":
    import sys
    fib(int(sys.argv[2]))
    print(sys.path)