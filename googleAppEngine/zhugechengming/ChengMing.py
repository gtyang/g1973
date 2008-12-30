# -*- coding: cp936 -*-
# 诸葛亮称命法V1.0

def fyear(year):    #处理年份重量
    while year<1941:
        year=year+60
    while year>2000:
        year=year-60
    if year==1941:
        numy=6
    if year==1942:
        numy=8
    if year==1943:
        numy=7
    if year==1944:
        numy=5
    if year==1945:
        numy=15
    if year==1946:
        numy=6
    if year==1947:
        numy=16
    if year==1948:
        numy=15
    if year==1949:
        numy=7
    if year==1950:
        numy=9
    if year==1951:
        numy=12
    if year==1952:
        numy=1
    if year==1953:
        numy=7
    if year==1954:
        numy=15
    if year==1955:
        numy=6
    if year==1956:
        numy=5
    if year==1957:
        numy=14
    if year==1958:
        numy=14
    if year==1959:
        numy=9
    if year==1960:
        numy=7
    if year==1961:
        numy=7
    if year==1962:
        numy=9
    if year==1963:
        numy=12
    if year==1964:
        numy=8
    if year==1965:
        numy=7
    if year==1966:
        numy=13
    if year==1967:
        numy=5
    if year==1968:
        numy=14
    if year==1969:
        numy=5
    if year==1970:
        numy=9
    if year==1971:
        numy=17
    if year==1972:
        numy=5
    if year==1973:
        numy=7
    if year==1974:
        numy=12
    if year==1975:
        numy=8
    if year==1976:
        numy=8
    if year==1977:
        numy=6
    if year==1978:
        numy=19
    if year==1979:
        numy=6
    if year==1980:
        numy=8
    if year==1981:
        numy=16
    if year==1982:
        numy=1
    if year==1983:
        numy=7
    if year==1984:
        numy=12
    if year==1985:
        numy=9
    if year==1986:
        numy=6
    if year==1987:
        numy=7
    if year==1988:
        numy=12
    if year==1989:
        numy=5
    if year==1990:
        numy=9
    if year==1991:
        numy=8
    if year==1992:
        numy=7
    if year==1993:
        numy=8
    if year==1994:
        numy=15
    if year==1995:
        numy=9
    if year==1996:
        numy=16
    if year==1997:
        numy=8
    if year==1998:
        numy=8
    if year==1999:
        numy=19
    if year==2000:
        numy=12
    return numy

def fmonth(months):
    if months==1:
        numm=6
    if months==2:
        numm=7
    if months==3:
        numm=18
    if months==4:
        numm=9
    if months==5:
        numm=5
    if months==6:
        numm=16
    if months==7:
        numm=9
    if months==8:
        numm=15
    if months==9:
        numm=18
    if months==10:
        numm=8
    if months==11:
        numm=9
    if months==12:
        numm=5
    return numm

def fday(days):
    if days==1:
        numd=5
    if days==2:
        numd=10
    if days==3:
        numd=8
    if days==4:
        numd=15
    if days==5:
        numd=16
    if days==6:
        numd=16
    if days==7:
        numd=8
    if days==8:
        numd=16
    if days==9:
        numd=8
    if days==10:
        numd=16
    if days==11:
        numd=9
    if days==12:
        numd=17
    if days==13:
        numd=8
    if days==14:
        numd=17
    if days==15:
        numd=10
    if days==16:
        numd=8
    if days==17:
        numd=9
    if days==18:
        numd=18
    if days==19:
        numd=5
    if days==20:
        numd=15
    if days==21:
        numd=10
    if days==22:
        numd=9
    if days==23:
        numd=8
    if days==24:
        numd=9
    if days==25:
        numd=15
    if days==26:
        numd=18
    if days==27:
        numd=7
    if days==28:
        numd=8
    if days==29:
        numd=16
    if days==30:
        numd=6
    return numd

def ftime(times):
    if times>=23 or times<=1:#子
        numt=16
    if times>=1 and times<=2:#丑
        numt=6
    if times>=3 and times<=4:#寅
        numt=7
    if times>=5 and times<=6:#卯
        numt=10
    if times>=7 and times<=8:#辰
        numt=9
    if times>=9 and times<=10:#巳
        numt=16
    if times>=11 and times<=12:#午
        numt=10
    if times>=13 and times<=14:#未
        numt=8
    if times>=15 and times<=16:#申
        numt=8
    if times>=17 and times<=18:#酉
        numt=9
    if times>=19 and times<=20:#戌
        numt=6
    if times>=21 and times<=22:#亥
        numt=6
    return numt

def chengMing(y,m,d,t): 
    pishi = {21:"短命非业谓大凶，平生灾难事重重，凶祸频临限逆境，终世困苦事不成", \
          22:"身寒骨冷苦伶仃，此命推来行乞人，劳劳碌碌无度日，中年打拱过平生",\
          23:"此命推来骨轻轻，求谋做事事难成，妻儿兄弟应难许，别处他乡作散人",\
          24:"此命推来福禄无，门庭困苦总难荣，六亲骨肉皆无靠，流到他乡作老人",\
          25:"此命推来祖业微，门庭营度似希奇，六亲骨肉如水炭，一世勤劳自把持",\
          26:"平生一路苦中求，独自营谋事不休，离祖出门宜早计，晚来衣禄自无忧",\
          27:"一生做事少商量，难靠祖宗作主张，独马单枪空作去，早年晚岁总无长",\
          28:"一生作事似飘蓬，祖宗产业在梦中，若不过房并改姓，也当移徒二三通",\
          29:"初年运限未曾亨，纵有功名在后成，须过四旬方可上，移居改姓使为良",\
          30:"劳劳碌碌苦中求，东走西奔何日休，若能终身勤与俭，老来稍可免忧愁",\
          31:"忙忙碌碌苦中求，何日云开见日头，难得祖基家可立，中年衣食渐无忧",\
          32:"初年运错事难谋，渐有财源如水流，到的中年衣食旺，那时名利一齐来",\
          33:"早年做事事难成，百计徒劳枉费心，半世自如流水去，后来运到始得金",\
          34:"此命福气果如何，僧道门中衣禄多，离祖出家方得妙，终朝拜佛念弥陀",\
          35:"生平福量不周全，祖业根基觉少传，营事生涯宜守旧，时来衣食胜从前",\
          36:"不须劳碌过平生，独自成家福不轻，早有福星常照命，任君行去百般成",\
          37:"此命般般事不成，弟兄少力自孤成，虽然祖业须微有，来的明时去的暗",\
          38:"一生骨肉最清高，早入学门姓名标，待看年将三十六，蓝衣脱去换红袍",\
          39:"此命少年运不通，劳劳做事尽皆空，苦心竭力成家计，到得那时在梦中",\
          40:"平生衣禄是绵长，件件心中自主张，前面风霜都受过，从来必定享安泰",\
          41:"此命推来事不同，为人能干异凡庸，中年还有逍遥福，不比前年云未通",\
          42:"得宽怀处且宽怀，何用双眉总不开，若使中年命运济，那时名利一齐来",\
          43:"为人心性最聪明，做事轩昂近贵人，衣禄一生天数定，不须劳碌是丰亨",\
          44:"来事由天莫苦求，须知福禄胜前途，当年财帛难如意，晚景欣然便不忧",\
          45:"福中取贵格求真，明敏才华志自伸，福禄寿全家道吉，桂兰毓秀晚荣臻",\
          46:"东西南北尽皆通，出姓移名更觉隆，衣禄无亏天数定，中年晚景一般同",\
          47:"此命推来旺末年，妻荣子贵自怡然，平生原有滔滔福，可有财源如水流",\
          48:"幼年运道未曾享，苦是蹉跎再不兴，兄弟六亲皆无靠，一身事业晚年成",\
          49:"此命推来福不轻，自立自成显门庭，从来富贵人亲近，使婢差奴过一生",\
          50:"为利为名终日劳，中年福禄也多遭，老来是有财星照，不比前番目下高",\
          51:"一世荣华事事通，不须劳碌自亨通，兄弟叔侄皆如意，家业成时福禄宏",\
          52:"一世亨通事事能，不须劳思自然能，宗施欣然心皆好，家业丰亨自称心",\
          53:"此格推来气象真，兴家发达在其中，一生福禄安排定，却是人间一富翁",\
          54:"此命推来厚且清，诗书满腹看功成，丰衣足食自然稳，正是人间有福人",\
          55:"走马扬鞭争名利，少年做事废筹论，一朝福禄源源至，富贵荣华显六亲",\
          56:"此格推来礼仪通，一生福禄用无穷，甜酸苦辣皆尝过，财源滚滚稳且丰",\
          57:"福禄盈盈万事全，一生荣耀显双亲，名扬威震人钦敬，处世逍遥似遇春",\
          58:"平生福禄自然来，名利兼全福禄偕，雁塔提名为贵客，紫袍金带走金鞋",\
          59:"细推此格妙且清，必定才高礼仪通，甲第之中应有分，扬鞭走马显威荣",\
          60:"一朝金榜快提名，显祖荣宗立大功，衣食定然原欲足，田园财帛更丰盈",\
          61:"不做朝中金榜客，定为世上一财翁，聪明天赋经书熟，名显高克自是荣",\
          62:"此名生来福不穷，读书必定显亲荣，紫衣金带为卿相，富贵荣华皆可同",\
          63:"命主为官福禄长，得来富贵定非常，名题金塔传金榜，定中高科天下扬",\
          64:"此格权威不可当，紫袍金带坐高堂，荣华富贵谁能及，积玉堆金满储仓",\
          65:"细推此命福不轻，安国安邦极品人，文绣雕梁政富贵，威声照耀四方闻",\
          66:"此格人间一福人，堆金积玉满堂春，从来富贵由天定，正笏垂绅谒圣君",\
          67:"此名生来福自宏，田园家业最高隆，平生衣禄丰盈足，一世荣华万事通",\
          68:"富贵由天莫苦求，万金家计不须谋，十年不比前番事，祖业根基水上舟",\
          69:"君是人间衣禄星，一生福贵众人钦，纵然福禄由天定，安享荣华过一生",\
          70:"此命推来福不轻，不须愁虑苦劳心，一生天定衣与禄，富贵荣华过一生",\
          71:"此名生来大不同，公侯卿相在其中，一生自有逍遥福，富贵荣华极品隆",\
          72:"此格世界罕有生，十代积善产此人，天上紫微来照命，统治万民乐太平"}
    your_num = fyear(int(y)) + fmonth(int(m)) + fday(int(d)) + ftime(int(t))
    return [your_num, pishi[your_num]]

def test():
  y = raw_input("Input the year of your birth:\n")
  m = raw_input("Input the month of your birth:\n")
  d = raw_input("Input the day of your birth:\n")
  t = raw_input("Input the time of your birth:\n")
  print chengMing(y,m,d,t)[1]
