class node:
    status : str
    letter: str
    parents: list
    children: list
    def __init__(self):
        self.parents = []
        self.children = []
        
#oh no cannot define a method inside class that returns a list of this class objects?        
def populate(st: node) -> list[node]:
        ans = list[node]()
        ans.append(st)
        return ans
    
def main():
    n = node()
    n.letter = "A"
    n.status="110010"
    lst = populate(n)
    for nd in lst:
        print(nd.letter)
    print(n.letter)
    
if __name__ == "__main__":
    main()