
def readIndex():
  index = input()
    return int(index)


def printIndex(index):
  print index


def countFibonacci(index):
    fibFirst = 0
    fibSecond = 1
    if index < 2:
        return index
    else:
        step = 1
        while step < index:
            fibSum = fibFirst + fibSecond
            fibFirst = fibSecond
            fibSecond = fibSum
            step += 1
    
      return fibSum


def main():
    indexFibonacci = readIndex()
    element = countFibonacci(indexFibonacci)
    printIndex(element)


main()
