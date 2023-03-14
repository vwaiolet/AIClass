
#find strobogrammatic in multi digit numbers
#each digit number you will be able to find some rule 
#916  180 deegree  916
#818  180 deegree  818
# tip : 9 and 6 need to be paired 
# n = 1 {0, 1, 8}
# n = 2 {11, 88, 69, 96}
# n = 3 {}
def gen_strobogrammatic(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = recursive(n, n)
    return result

def recursive(n, length):
    if n == 0:
        return ['']
    if n == 1:
        return ['1', '0', '8']
    middle = recursive(n-2, length)
    result = []
    for mid in middle:
        if n != length:
            result.append('0' + mid + '0')
        result.append('8' + mid + '8')
        result.append('1' + mid + '1')
        result.append('6' + mid + '9')
        result.append('9' + mid + '6')
    return result

print(gen_strobogrammatic(3))
print(gen_strobogrammatic(4))


#101, 609, 808, 906
#111, 619, 818, 916
#181, 689, 888, 986
          

          
          
          
          
          
          
          
          
