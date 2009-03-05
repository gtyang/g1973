# -*- coding: cp936 -*-
# �����������V1.0

def fyear(year):    #�����������
    while year<1941:
        year=year+60
    while year>2000:
        year=year-60
    weightYear ={
        1941: 6,
        1942: 8,
        1943: 7,
        1944: 5,
        1945: 15,
        1946: 6,
        1947: 16,
        1948: 15,
        1949: 7,
        1950: 9,
        1951: 12,
        1952: 1,
        1953: 7,
        1954: 15,
        1955: 6,
        1956: 5,
        1957: 14,
        1958: 14,
        1959: 9,
        1960: 7,
        1961: 7,
        1962: 9,
        1963: 12,
        1964: 8,
        1965: 7,
        1966: 13,
        1967: 5,
        1968: 14,
        1969: 5,
        1970: 9,
        1971: 17,
        1972: 5,
        1973: 7,
        1974: 12,
        1975: 8,
        1976: 8,
        1977: 6,
        1978: 19,
        1979: 6,
        1980: 8,
        1981: 16,
        1982: 1,
        1983: 7,
        1984: 12,
        1985: 9,
        1986: 6,
        1987: 7,
        1988: 12,
        1989: 5,
        1990: 9,
        1991: 8,
        1992: 7,
        1993: 8,
        1994: 15,
        1995: 9,
        1996: 16,
        1997: 8,
        1998: 8,
        1999: 19,
        2000: 12
    }

    return weightYear[year]

def fmonth(months):
    weightMonth = {
       1: 6,
       2: 7,
       3: 18,
       4: 9,
       5: 5,
       6: 16,
       7: 9,
       8: 15,
       9: 18,
       10: 8,
       11: 9,
       12: 5
    }
    return weightMonth[months]

def fday(days):
    weightDay = {
       1: 5,
       2: 10,
       3: 8,
       4: 15,
       5: 16,
       6: 16,
       7: 8,
       8: 16,
       9: 8,
       10: 16,
       11: 9,
       12: 17,
       13: 8,
       14: 17,
       15: 10,
       16: 8,
       17: 9,
       18: 18,
       19: 5,
       20: 15,
       21: 10,
       22: 9,
       23: 8,
       24: 9,
       25: 15,
       26: 18,
       27: 7,
       28: 8,
       29: 16,
       30: 6
    }
    return weightDay[days]

def ftime(times):
    if times>=23 or times<1:#��
        numt=16
    if times>=1 and times<=2:#��
        numt=6
    if times>=3 and times<=4:#��
        numt=7
    if times>=5 and times<=6:#î
        numt=10
    if times>=7 and times<=8:#��
        numt=9
    if times>=9 and times<=10:#��
        numt=16
    if times>=11 and times<=12:#��
        numt=10
    if times>=13 and times<=14:#δ
        numt=8
    if times>=15 and times<=16:#��
        numt=8
    if times>=17 and times<=18:#��
        numt=9
    if times>=19 and times<=20:#��
        numt=6
    if times>=21 and times<=22:#��
        numt=6
    return numt

def chengMing(y,m,d,t): 
    pishi = {21:"������ҵν���ף�ƽ�����������أ��׻�Ƶ�����澳�����������²���", 
          22:"������������꣬�������������ˣ�����µµ�޶��գ�����򹰹�ƽ��",
          23:"�������������ᣬ��ı�������ѳɣ��޶��ֵ�Ӧ��������������ɢ��",
          24:"����������»�ޣ���ͥ���������٣����׹�����޿�����������������",
          25:"����������ҵ΢����ͥӪ����ϣ�棬���׹�����ˮ̿��һ�������԰ѳ�",
          26:"ƽ��һ·�����󣬶���Ӫı�²��ݣ������������ƣ�������»������",
          27:"һ���������������ѿ����������ţ�������ǹ����ȥ�������������޳�",
          28:"һ��������Ʈ����ڲ�ҵ�����У��������������գ�Ҳ����ͽ����ͨ",
          29:"��������δ���࣬���й����ں�ɣ������Ѯ�����ϣ��ƾӸ���ʹΪ��",
          30:"����µµ�����󣬶������������ݣ�������������������Կ����ǳ�",
          31:"ææµµ�����󣬺����ƿ�����ͷ���ѵ�����ҿ�����������ʳ������",
          32:"�����˴�����ı�����в�Դ��ˮ��������������ʳ������ʱ����һ����",
          33:"�����������ѳɣ��ټ�ͽ�������ģ�����������ˮȥ�������˵�ʼ�ý�",
          34:"������������Σ�ɮ��������»�࣬������ҷ�����ճ��ݷ�������",
          35:"��ƽ��������ȫ����ҵ�������ٴ���Ӫ���������ؾɣ�ʱ����ʳʤ��ǰ",
          36:"������µ��ƽ�������ԳɼҸ����ᣬ���и��ǳ��������ξ���ȥ�ٰ��",
          37:"��������²��ɣ����������Թ³ɣ���Ȼ��ҵ��΢�У�������ʱȥ�İ�",
          38:"һ����������ߣ�����ѧ�������꣬�����꽫��ʮ����������ȥ������",
          39:"���������˲�ͨ���������¾��Կգ����Ľ����ɼҼƣ�������ʱ������",
          40:"ƽ����»���೤���������������ţ�ǰ���˪���ܹ��������ض�����̩",
          41:"���������²�ͬ��Ϊ���ܸ��췲ӹ�����껹����ң��������ǰ����δͨ",
          42:"�ÿ������ҿ���������˫ü�ܲ�������ʹ�������˼ã���ʱ����һ����",
          43:"Ϊ��������������������������ˣ���»һ����������������µ�Ƿ��",
          44:"��������Ī������֪��»ʤǰ;������Ʋ������⣬������Ȼ�㲻��",
          45:"����ȡ������棬�����Ż�־���죬��»��ȫ�ҵ���������ع��������",
          46:"�����ϱ�����ͨ��������������¡����»�޿�����������������һ��ͬ",
          47:"����������ĩ�꣬�����ӹ�����Ȼ��ƽ��ԭ�����ϸ������в�Դ��ˮ��",
          48:"�����˵�δ���������������ٲ��ˣ��ֵ����׽��޿���һ����ҵ�����",
          49:"�������������ᣬ�����Գ�����ͥ�������������׽���ʹ澲�ū��һ��",
          50:"Ϊ��Ϊ�������ͣ����긣»Ҳ���⣬�������в����գ�����ǰ��Ŀ�¸�",
          51:"һ���ٻ�����ͨ��������µ�Ժ�ͨ���ֵ���ֶ�����⣬��ҵ��ʱ��»��",
          52:"һ����ͨ�����ܣ�������˼��Ȼ�ܣ���ʩ��Ȼ�ĽԺã���ҵ����Գ���",
          53:"�˸����������棬�˼ҷ��������У�һ����»���Ŷ���ȴ���˼�һ����",
          54:"�������������壬ʫ�����������ɣ�������ʳ��Ȼ�ȣ������˼��и���",
          55:"����������������������·ϳ��ۣ�һ����»ԴԴ���������ٻ�������",
          56:"�˸���������ͨ��һ����»�������������Գ�������Դ�������ҷ�",
          57:"��»ӯӯ����ȫ��һ����ҫ��˫�ף������������վ���������ң������",
          58:"ƽ����»��Ȼ����������ȫ��»�ɣ���������Ϊ��ͣ����۽���߽�Ь",
          59:"ϸ�ƴ˸������壬�ض��Ÿ�����ͨ���׵�֮��Ӧ�з֣��������������",
          60:"һ�����������������������󹦣���ʳ��Ȼԭ���㣬��԰�Ʋ�����ӯ",
          61:"�������н��ͣ���Ϊ����һ���̣������츳�����죬���Ը߿�������",
          62:"�����������������ض������٣����½��Ϊ���࣬�����ٻ��Կ�ͬ",
          63:"����Ϊ�ٸ�»�����������󶨷ǳ��������������񣬶��и߿�������",
          64:"�˸�Ȩ�����ɵ������۽�������ã��ٻ�����˭�ܼ�������ѽ�������",
          65:"ϸ�ƴ��������ᣬ�������Ʒ�ˣ��������������������ҫ�ķ���",
          66:"�˸��˼�һ���ˣ��ѽ�������ô��������������춨�����˴�����ʥ��",
          67:"�����������Ժ꣬��԰��ҵ���¡��ƽ����»��ӯ�㣬һ���ٻ�����ͨ",
          68:"��������Ī�������ҼƲ���ı��ʮ�겻��ǰ���£���ҵ����ˮ����",
          69:"�����˼���»�ǣ�һ�����������գ���Ȼ��»���춨�������ٻ���һ��",
          70:"�������������ᣬ������ǿ����ģ�һ���춨����»�������ٻ���һ��",
          71:"����������ͬ���������������У�һ��������ң���������ٻ���Ʒ¡",
          72:"�˸����纱������ʮ�����Ʋ����ˣ�������΢��������ͳ��������̫ƽ"}
    your_num = fyear(int(y)) + fmonth(int(m)) + fday(int(d)) + ftime(int(t))
    return [your_num, pishi[your_num]]

def test():
  y = raw_input("Input the year of your birth:\n")
  m = raw_input("Input the month of your birth:\n")
  d = raw_input("Input the day of your birth:\n")
  t = raw_input("Input the time of your birth:\n")
  print chengMing(y,m,d,t)[1]