class LinkedList:
    
    def __init__(self):
        self.list = []
    
    def get(self, index: int) -> int:
        if index < len(self.list):
            return self.list[index]
        return -1

    def insertHead(self, val: int) -> None:
        new_list = [val]
        for num in self.list:
            new_list.append(num)
        self.list = new_list
        

    def insertTail(self, val: int) -> None:
        self.list.append(val)

    def remove(self, index: int) -> bool:
        if index < len(self.list):
            self.list.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        array = []
        for num in self.list:
            array.append(num)
        return array
        
