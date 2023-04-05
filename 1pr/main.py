import TreeMinMax as t

def main():
    n = t.node()
    n.letter = t.ord(0)
    n.status="110010"
    thetree = t.populate(n)
    t.do_action_to_subnodes_and_this(n, t.try_set_novertejumu, True)
    for nd, kv in thetree.struct.items():
        for k, v in kv.items():
            a =""
            for cn in v.children:
                a+= " ("+str(cn.level)+":"+str(cn.location)+") "
            print(v.letter+"|"+str(v.level)+":"+str(v.location)+"|"+" -> "+v.status+" "+("["+str(v.evaluation)+"]" if hasattr(v, 'evaluation') else "")+a)
    
if __name__ == "__main__":
    main()