//=IF(A2<40000, "<40 000", IF(A2<50000, "40 000-50 000", IF(A2<60000, "60 000-70 000", IF(A2<70000, "70 000-80 000", ">=2000"))))
//~~~~~~~~~~~~~~~~~~~~~~~~massive gen
var a="var d = [";
for(var i=500000; i<15000000-500000; i+=500000)
a+=i+", "
a+=(15000000-500000)+"];"
console.log(a);
copy(a);

//=IF(L2<100, 1900+L2, IF(L2<1000, 2019-L2, IF(L2>2025, 2025, L2)))

//~~~~~~~~~~~~~~~~~~~~~~~~~~~~~excel formula gen

var d = [40000, 60000, 70000, 80000, 100000, 125000, 148000, 158000, 168000, 185000, 195000, 205000, 210000, 220000, 230000, 240000, 250000, 260000, 270000, 280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000, 360000, 370000, 380000, 390000, 400000, 410000, 420000, 430000, 440000, 450000, 460000, 470000, 480000];


var d = [40000, 60000, 70000, 80000, 100000, 125000, 148000, 168000, 185000, 
    195000, 205000, 210000, 220000, 230000, 240000, 250000, 260000, 270000, 
    280000, 290000, 300000, 310000, 320000, 330000, 340000, 350000, 360000, 
    370000, 380000, 390000, 400000, 410000, 420000, 430000, 440000, 450000, 
    460000, 470000, 480000];
	
var d = [100000, 168000, 205000, 250000, 310000, 370000, 430000];

var d = [168000, 260000];

var d = [450000, 630000];

var column = "H";

var a="=IF("+column+"2<"+d[0]+", \"<"+d[0]+"\",";
for(var i=1; i<d.length; i++)
a+="IF("+column+"2<"+d[i]+", \""+d[i-1]+"-"+d[i]+"\",";
a+="\">="+d[d.length-1]+"\"";
for(var i=0; i<d.length; i++)
	a+=")";
console.log(a);
copy(a);
