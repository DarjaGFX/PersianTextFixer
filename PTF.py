import sys

def main():
    source = sys.argv[1]
    # print(source)
    r = open(source,'r')
    f = r.read()
    r.close()
    res = ""
    f = f.split('\n')
    for line in f:
        line = line.split(' ')
        tmp = ""
        for word in range(len(line)-1,-1,-1):
            tmp += line[word].replace('(','\(').replace(')','\)').replace('\(',')').replace('\)','(') + ' '
        tmp += '\n'
        res += tmp

    r = open(source,'w')
    r.write(res)
    r.close()

if __name__ == "__main__":
    main()