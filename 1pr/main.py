class node:
    status : str
    letter: str
    parents: list
    children: list
    def __init__(self):
        self.parents = []
        self.children = []

class tree:
    struct: dict[int, dict[int, node]]
    def __init__(self):
        self.struct = {}
        
#oh no cannot define a method inside class (node) that returns a list of this class objects?        
def populate(st: node) -> tree:
        ans = tree()
        ans.struct[1] = {1: st}
        return ans
    
def main():
    n = node()
    n.letter = "A"
    n.status="110010"
    thetree = populate(n)
    for nd, kv in thetree.struct.items():
        for k, v in kv.items():
            print(v.letter)
    print(n.letter)
    
if __name__ == "__main__":
    main()