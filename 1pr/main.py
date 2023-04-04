from typing import Tuple


class node:
    status : str
    letter: str
    parents: list
    children: list
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

def isvalidmove(state: str, frm: int, to: int)  -> bool:
    if len(state) < to: return False
    if frm <0: return False
    if to<=frm: return False
    return state[frm:to] == "00" or state[frm:to] == "10" or state[frm:to] == "01"

def do_move(state: str, frm: int, to: int) -> str:
    if len(state) < to: return "ERROR"
    if frm <0: return "ERROR"
    if to<=frm: return "ERROR"
    reslt = "1" if state[frm:to] == "00" else "0" if state[frm:to] == "10" else "0" if state[frm:to] == "01" else state[frm:to]
    return state[0:frm]+reslt+state[to:len(state)]
#oh no cannot define a method inside class (node) that returns a list of this class objects?        
def populate(st: node) -> tree:
        ans = tree()
        node_counter =0
        st.level = 0
        st.location = 0
        st.letter=ord(node_counter)
        node_counter = node_counter+1
        ans.struct[0] = {0: st}
        #TODO: move the counters to the inside of the tree...
        populate_next_level(ans,st,node_counter, {})
        return ans

def find_by_status(t: tree, state: str, lvl: int):
    for num, st in t.struct[lvl].items():
        if(st.status == state):
            return st
    return None

def populate_next_level(t: tree, st: node, ncounter: int, lookupHashTable: dict[str, tuple[int,int]]) -> Tuple[int,  dict[str, tuple[int,int]]]:
    lvlndcnt = 0
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
                    st.children.append(st)
                    newnode.letter = ord(ncounter)
                    ncounter = ncounter+1
                    if st.level+1 not in t.struct:
                        t.struct[st.level+1]={}
                    t.struct[st.level+1][lvlndcnt] = newnode
                    lvlndcnt = lvlndcnt+1
                else:
                   nd =find_by_status(t,new_status,st.level+1)
                   if st not in nd.parents:
                        nd.parents.append(st)
                        thisIterHashTable[new_status] = (st.level+1, lvlndcnt)
                        
    return (lvlndcnt, lookupHashTable)
    
def main():
    n = node()
    n.letter = ord(0)
    n.status="110010"
    thetree = populate(n)
    for nd, kv in thetree.struct.items():
        for k, v in kv.items():
            print(v.letter+" -> "+v.status)
    
if __name__ == "__main__":
    main()