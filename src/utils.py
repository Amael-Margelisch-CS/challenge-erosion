
def img2ascii(img_data: list[list[int]], black: str, white: str) -> str:    
    result = ''
    for row in range(len(img)):
        if row > 0:
          result += '\n'    
        for elem in img[row]:
            if elem == 1:
                result += black
            else:
                result += white
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def load_pbm(filename: str) -> list[list[int]]:
    ...