
def img2ascii(img_data: list[list[int]], black: str, white: str) -> str:    
    result = ''
    for row in range(len(img_data)):
        if row > 0:
          result += '\n'    
        for elem in img_data[row]:
            if elem == 1:
                result += black
            else:
                result += white
    return result

def load_pbm(filename: str) -> list[list[int]]:
    with open(filename,'r') as f:
        for entry, info in enumerate (f):
            if entry == 1:
                img_dim = list((info.strip("\n")).split(" "))                    
    f.close()
    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()