def cor_bin(num):
    n = format(num, 'b')
    if len(str(n))<3:
        if len(str(n))<2:
            n = "00"+n
        else:
            n = "0"+n
    
    new_ind = n.find("1")
    res = ' '*(new_ind-1) + n[new_ind:]
    
    return res
    
def print_formatted(number):
    x=number
    count="  "

    # your code goes here
    for i in range(number):
        print(f"{i:>count}{oct(i)[2:]:>count}{hex(i)[2:].upper():>count}{bin(i)[2:]:>count}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)