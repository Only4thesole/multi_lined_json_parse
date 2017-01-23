import json

def main():
    f = open('j.text')
    r = f.read()
    f.close()
    lines = r.split(',{')
    products = []
    products.append(json.loads(lines[0]))
    for p in lines[1:]:
        p = '{%s' % p
        products.append(json.loads(p))
    print products

if __name == '__main__':
    main()
