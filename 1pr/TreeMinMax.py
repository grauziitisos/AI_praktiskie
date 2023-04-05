from typing import Tuple


class node:
    status : str
    letter: str
    parents: list#[node]
    children: list#[node]
    level: int
    location: int
    def __init__(self):
        self.parents = []
        self.children = []

def ord(num: int) -> str:
    upperalphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if(num <0): return "TOOSMALL"
    if(num < len(upperalphabet)): return upperalphabet[num]
    """
    var a="[";for(let j=0; j<26; j++) for (let i = 0; i < 26; i++)
    a+= ("\""+String.fromCharCode(65+j)+String.fromCharCode(65+i)+"\", "); a+="]"
    """
    followingcols = ["AA", "AB", "AC", "AD", "AE", "AF", "AG", "AH", "AI", "AJ", "AK", "AL", "AM", "AN", "AO", "AP", "AQ", "AR", "AS", "AT", "AU", "AV", "AW", "AX", "AY", "AZ", 
                     "BA", "BB", "BC", "BD", "BE", "BF", "BG", "BH", "BI", "BJ", "BK", "BL", "BM", "BN", "BO", "BP", "BQ", "BR", "BS", "BT", "BU", "BV", "BW", "BX", "BY", "BZ", 
                     "CA", "CB", "CC", "CD", "CE", "CF", "CG", "CH", "CI", "CJ", "CK", "CL", "CM", "CN", "CO", "CP", "CQ", "CR", "CS", "CT", "CU", "CV", "CW", "CX", "CY", "CZ", 
                     "DA", "DB", "DC", "DD", "DE", "DF", "DG", "DH", "DI", "DJ", "DK", "DL", "DM", "DN", "DO", "DP", "DQ", "DR", "DS", "DT", "DU", "DV", "DW", "DX", "DY", "DZ", 
                     "EA", "EB", "EC", "ED", "EE", "EF", "EG", "EH", "EI", "EJ", "EK", "EL", "EM", "EN", "EO", "EP", "EQ", "ER", "ES", "ET", "EU", "EV", "EW", "EX", "EY", "EZ", 
                     "FA", "FB", "FC", "FD", "FE", "FF", "FG", "FH", "FI", "FJ", "FK", "FL", "FM", "FN", "FO", "FP", "FQ", "FR", "FS", "FT", "FU", "FV", "FW", "FX", "FY", "FZ", 
                     "GA", "GB", "GC", "GD", "GE", "GF", "GG", "GH", "GI", "GJ", "GK", "GL", "GM", "GN", "GO", "GP", "GQ", "GR", "GS", "GT", "GU", "GV", "GW", "GX", "GY", "GZ", 
                     "HA", "HB", "HC", "HD", "HE", "HF", "HG", "HH", "HI", "HJ", "HK", "HL", "HM", "HN", "HO", "HP", "HQ", "HR", "HS", "HT", "HU", "HV", "HW", "HX", "HY", "HZ", 
                     "IA", "IB", "IC", "ID", "IE", "IF", "IG", "IH", "II", "IJ", "IK", "IL", "IM", "IN", "IO", "IP", "IQ", "IR", "IS", "IT", "IU", "IV", "IW", "IX", "IY", "IZ", 
                     "JA", "JB", "JC", "JD", "JE", "JF", "JG", "JH", "JI", "JJ", "JK", "JL", "JM", "JN", "JO", "JP", "JQ", "JR", "JS", "JT", "JU", "JV", "JW", "JX", "JY", "JZ", 
                     "KA", "KB", "KC", "KD", "KE", "KF", "KG", "KH", "KI", "KJ", "KK", "KL", "KM", "KN", "KO", "KP", "KQ", "KR", "KS", "KT", "KU", "KV", "KW", "KX", "KY", "KZ", 
                     "LA", "LB", "LC", "LD", "LE", "LF", "LG", "LH", "LI", "LJ", "LK", "LL", "LM", "LN", "LO", "LP", "LQ", "LR", "LS", "LT", "LU", "LV", "LW", "LX", "LY", "LZ", 
                     "MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MI", "MJ", "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", 
                     "NA", "NB", "NC", "ND", "NE", "NF", "NG", "NH", "NI", "NJ", "NK", "NL", "NM", "NN", "NO", "NP", "NQ", "NR", "NS", "NT", "NU", "NV", "NW", "NX", "NY", "NZ", 
                     "OA", "OB", "OC", "OD", "OE", "OF", "OG", "OH", "OI", "OJ", "OK", "OL", "OM", "ON", "OO", "OP", "OQ", "OR", "OS", "OT", "OU", "OV", "OW", "OX", "OY", "OZ", 
                     "PA", "PB", "PC", "PD", "PE", "PF", "PG", "PH", "PI", "PJ", "PK", "PL", "PM", "PN", "PO", "PP", "PQ", "PR", "PS", "PT", "PU", "PV", "PW", "PX", "PY", "PZ", 
                     "QA", "QB", "QC", "QD", "QE", "QF", "QG", "QH", "QI", "QJ", "QK", "QL", "QM", "QN", "QO", "QP", "QQ", "QR", "QS", "QT", "QU", "QV", "QW", "QX", "QY", "QZ", 
                     "RA", "RB", "RC", "RD", "RE", "RF", "RG", "RH", "RI", "RJ", "RK", "RL", "RM", "RN", "RO", "RP", "RQ", "RR", "RS", "RT", "RU", "RV", "RW", "RX", "RY", "RZ", 
                     "SA", "SB", "SC", "SD", "SE", "SF", "SG", "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SP", "SQ", "SR", "SS", "ST", "SU", "SV", "SW", "SX", "SY", "SZ", 
                     "TA", "TB", "TC", "TD", "TE", "TF", "TG", "TH", "TI", "TJ", "TK", "TL", "TM", "TN", "TO", "TP", "TQ", "TR", "TS", "TT", "TU", "TV", "TW", "TX", "TY", "TZ", 
                     "UA", "UB", "UC", "UD", "UE", "UF", "UG", "UH", "UI", "UJ", "UK", "UL", "UM", "UN", "UO", "UP", "UQ", "UR", "US", "UT", "UU", "UV", "UW", "UX", "UY", "UZ", 
                     "VA", "VB", "VC", "VD", "VE", "VF", "VG", "VH", "VI", "VJ", "VK", "VL", "VM", "VN", "VO", "VP", "VQ", "VR", "VS", "VT", "VU", "VV", "VW", "VX", "VY", "VZ", 
                     "WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WI", "WJ", "WK", "WL", "WM", "WN", "WO", "WP", "WQ", "WR", "WS", "WT", "WU", "WV", "WW", "WX", "WY", "WZ", 
                     "XA", "XB", "XC", "XD", "XE", "XF", "XG", "XH", "XI", "XJ", "XK", "XL", "XM", "XN", "XO", "XP", "XQ", "XR", "XS", "XT", "XU", "XV", "XW", "XX", "XY", "XZ", 
                     "YA", "YB", "YC", "YD", "YE", "YF", "YG", "YH", "YI", "YJ", "YK", "YL", "YM", "YN", "YO", "YP", "YQ", "YR", "YS", "YT", "YU", "YV", "YW", "YX", "YY", "YZ", 
                     "ZA", "ZB", "ZC", "ZD", "ZE", "ZF", "ZG", "ZH", "ZI", "ZJ", "ZK", "ZL", "ZM", "ZN", "ZO", "ZP", "ZQ", "ZR", "ZS", "ZT", "ZU", "ZV", "ZW", "ZX", "ZY", "ZZ", ]
    if (num > 26+len(followingcols)): return "TOOBIG"
    return followingcols[num-26]
class tree:
    #would be nice to have a setter that autoincreases last letter counter on set...
    struct: dict[int, dict[int, node]]
    def __init__(self):
        self.struct = {}
        
    def root_node_factory(status: str) -> node:
        n = node()
        n.letter = ord(0)
        n.status=status
        return n
    
    def a_log_of_tree(self):
        for nd, kv in self.struct.items():
            for k, v in kv.items():
                a =""
                for cn in v.children:
                    a+= " ("+str(cn.level)+":"+str(cn.location)+") "
                print(v.letter+"|"+str(v.level)+":"+str(v.location)+"|"+" -> "+v.status+" "+("["+str(v.evaluation)+"]" if hasattr(v, 'evaluation') else "")+a)

def isvalidmove(state: str, frm: int, to: int)  -> bool:
    if len(state) < to: return False
    if frm <0: return False
    if to<=frm: return False
    return state[frm:to] == "00" or state[frm:to] == "10" #or state[frm:to] == "01"

def do_move(state: str, frm: int, to: int) -> str:
    if len(state) < to: return "ERROR"
    if frm <0: return "ERROR"
    if to<=frm: return "ERROR"
    reslt = "1" if state[frm:to] == "00" else "0" if state[frm:to] == "10" else "0" if state[frm:to] == "01" else state[frm:to]
    return state[0:frm]+reslt+state[to:len(state)]

#fail to overload.. missing positional argument...
def is_game_over_for_node(st: node) -> bool:
    return len(st.status) <= 3

def is_game_over(tr: tree, lvl: int) -> bool:
    for nr, st in tr.struct[lvl].items():
        if( not is_game_over_for_node(st)):
            return False
    return True
    
#oh no cannot define a method inside class (node) that returns a list of this class objects?        
def populate(st: node) -> tree:
        current_level = 0
        ans = tree()
        node_counter =0
        st.level = current_level
        st.location = 0
        st.letter=ord(node_counter)
        node_counter = node_counter+1
        ans.struct[0] = {0: st}
        #TODO: move the counters to the inside of the tree...
        while(not is_game_over(ans, current_level)):
            ndcount = 0
            lasthashtable = {}
            for nr, nd in ans.struct[current_level].items():
                if(not is_game_over_for_node(nd)):
                    (node_counter,ndcount, lasthashtable) = populate_next_level(ans,nd,node_counter, ndcount, lasthashtable)
            current_level = current_level +1
        return ans

def find_by_status(t: tree, state: str, lvl: int):
    for num, st in t.struct[lvl].items():
        if(st.status == state):
            return st
    return None

def populate_next_level(t: tree, st: node, ncounter: int, lvlndcnt: int, lookupHashTable: dict[str, tuple[int,int]]) -> Tuple[int, int,  dict[str, tuple[int,int]]]:
    thisIterHashTable ={}
    for i in range(len(st.status)-1):
        if(isvalidmove(st.status, i, i+2)):
            new_status = do_move(st.status, i, i+2)
            if new_status not in thisIterHashTable:
                if new_status not in lookupHashTable:
                    #print(new_status)
                    thisIterHashTable[new_status] = (st.level+1, lvlndcnt)
                    lookupHashTable[new_status] = (st.level+1, lvlndcnt)
                    newnode = node()
                    newnode.level = st.level+1
                    newnode.status = new_status
                    newnode.parents.append(newnode)
                    st.children.append(newnode)
                    newnode.letter = ord(ncounter)
                    newnode.location = lvlndcnt
                    ncounter = ncounter+1
                    if st.level+1 not in t.struct:
                        t.struct[st.level+1]={}
                    t.struct[st.level+1][lvlndcnt] = newnode
                    lvlndcnt = lvlndcnt+1
                else:
                   nd =find_by_status(t,new_status,st.level+1)
                   if st not in nd.parents:
                        nd.parents.append(st)
                        st.children.append(nd)
                        thisIterHashTable[new_status] = (st.level+1, lvlndcnt)
                        
    return (ncounter, lvlndcnt, lookupHashTable)

def do_action_to_subnodes_and_this(nod : node, cl: callable, *args):
    for nd in nod.children:
        do_action_to_subnodes_and_this(nd, cl, *args)
    cl(nod, *args)

def all_childs_has_novertejums(nod: node) -> bool:
    for nd in nod.children:
        if not hasattr(nd, 'evaluation'):
            return False
    return True

def get_childs_min_novertejums(nod: node) -> int:
    if(len(nod.children)<1): return None
    minnov = nod.children[0].evaluation
    for nd in nod.children:
        if(nd.evaluation < minnov):
            minnov = nd.evaluation
    return minnov

def get_a_child_from_childs_with_min_novertejums(nod: node) -> node:
    if(len(nod.children)<1): return None
    minchild = nod.children[0]
    minnov = nod.children[0].evaluation
    for nd in nod.children:
        if(nd.evaluation < minnov):
            minnov = nd.evaluation
            minchild = nd
    return minchild

def get_childs_max_novertejums(nod: node) -> int:
    if(len(nod.children)<1): return None
    maxnov = nod.children[0].evaluation
    for nd in nod.children:
        if(nd.evaluation > maxnov):
            maxnov = nd.evaluation
    return maxnov

def get_a_child_from_childs_with_max_novertejums(nod: node) -> node:
    if(len(nod.children)<1): return None
    maxchild = nod.children[0]
    maxnov = nod.children[0].evaluation
    for nd in nod.children:
        if(nd.evaluation > maxnov):
            maxnov = nd.evaluation
            maxchild = nd
    return maxchild

def try_set_novertejumu(nod: node, *args):
    ismaxstart = args[0]
    if not hasattr(nod, 'evaluation'):
        if(len(nod.status) <= 3):
           # if(nod.level % 2 ==0):
                if(ismaxstart):
                    nod.evaluation = 1 if(nod.status[0:2]=="11") else -1 if (nod.status[0:2]=="00") else 0
                else:
                    nod.evaluation = -1 if(nod.status[0:2]=="11") else 1 if (nod.status[0:2]=="00") else 0
            #else:
            #    if(not ismaxstart):
            #        nod.evaluation = 1 if(nod.status[0:2]=="11") else -1 if (nod.status[0:2]=="00") else 0
            #    else:
            #        nod.evaluation = -1 if(nod.status[0:2]=="11") else 1 if (nod.status[0:2]=="00") else 0
        else:
            if(all_childs_has_novertejums(nod)):
                if(nod.level % 2 ==0):
                    nod.evaluation = get_childs_max_novertejums(nod) if ismaxstart else get_childs_min_novertejums(nod)
                else:
                    nod.evaluation = get_childs_max_novertejums(nod) if not ismaxstart else get_childs_min_novertejums(nod)
                

def testprint(nd: node):
    print(nd.status)
