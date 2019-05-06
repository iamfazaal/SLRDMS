from sklearn import tree
# import json
import codecs, json
from firebase import firebase
sourceFile = open("example.json", "rU")

json_data = json.load(sourceFile)

# 1 Row
d1= json_data['1']['Day']
s1= json_data['1']['Station']
d1 = 0
s1 = 0
# print(d1, s1)

# 2 Row
d2= json_data['2']['Day']
s2= json_data['2']['Station']
d2 = 0
s2 = 1
# print(d2, s2)

# 3 Row
d3= json_data['3']['Day']
s3= json_data['3']['Station']
d3 = 0
s3 = 2
#print(d3, s3)

# 4 Row
d4= json_data['4']['Day']
s4= json_data['4']['Station']
d4 = 0
s4 = 3
#print(d4, s4)

# 5 Row
d5= json_data['5']['Day']
s5= json_data['5']['Station']
d5 = 0
s5 = 4
#print(d5, s5)

# 6 Row
d6= json_data['6']['Day']
s6= json_data['6']['Station']
d6 = 0
s6 = 5
# print(d6, s6)

# 7 Row
d7= json_data['7']['Day']
s7= json_data['7']['Station']
d7 = 0
s7 = 6
#print(d7, s7)

# 8 Row
d8= json_data['8']['Day']
s8= json_data['8']['Station']
d8 = 0
s8 = 7
#print(d8, s8)

# 9 Row
d9= json_data['9']['Day']
s9= json_data['9']['Station']
d9 = 0
s9 = 8
# print(d9, s9)

# 10 Row
d10= json_data['10']['Day']
s10= json_data['10']['Station']
d10 = 0
s10 = 9
# print(d10, s10)

# 11 Row
d11= json_data['11']['Day']
s11= json_data['11']['Station']
d11 = 0
s11 = 10
# print(d11, s11)

# 12 Row
d12= json_data['12']['Day']
s12= json_data['12']['Station']
d12 = 1
s12 = 0
# print(d12, s12)

# 13 Row
d13= json_data['13']['Day']
s13= json_data['13']['Station']
d13 = 1
s13 = 1
# print(d13, s13)

# 14 Row
d14= json_data['14']['Day']
s14= json_data['14']['Station']
d14 = 1
s14 = 2
# print(d14, s14)

# 15 Row
d15= json_data['15']['Day']
s15= json_data['15']['Station']
d15 = 1
s15 = 3
# print(d15, s15)

# 16 Row
d16= json_data['16']['Day']
s16= json_data['16']['Station']
d16 = 1
s16 = 4
# print(d16, s16)

# 17 Row
d17= json_data['17']['Day']
s17= json_data['17']['Station']
d17 = 1
s17 = 5
# print(d17, s17)

# 18 Row
d18= json_data['18']['Day']
s18= json_data['18']['Station']
d18 = 1
s18 = 6
# print(d18, s18)

# 19 Row
d19= json_data['19']['Day']
s19= json_data['19']['Station']
d19 = 1
s19 = 7
# print(d19, s19)

# 20 Row
d20= json_data['20']['Day']
s20= json_data['20']['Station']
d20 = 1
s20 = 8
# print(d20, s20)

# 21 Row
d21= json_data['21']['Day']
s21= json_data['21']['Station']
d21 = 1
s21 = 9
# print(d21, s21)

# 22 Row
d22= json_data['22']['Day']
s22= json_data['22']['Station']
d22 = 1
s22 = 10
# print(d22, s22)

# 23 Row
d23= json_data['23']['Day']
s23= json_data['23']['Station']
d23 = 2
s23 = 0
# print(d23, s23)

# 24 Row
d24= json_data['24']['Day']
s24= json_data['24']['Station']
d24 = 2
s24 = 1
# print(d24, s24)

# 25 Row
d25= json_data['25']['Day']
s25= json_data['25']['Station']
d25 = 2
s25 = 2
# print(d25, s25)

# 26 Row
d26= json_data['26']['Day']
s26= json_data['26']['Station']
d26 = 2
s26 = 3
# print(d26, s26)

# 27 Row
d27= json_data['27']['Day']
s27= json_data['27']['Station']
d27 = 2
s27 = 4
# print(d27, s27)

# 28 Row
d28= json_data['28']['Day']
s28= json_data['28']['Station']
d28 = 2
s28 = 5
# print(d28, s28)

# 29 Row
d29= json_data['29']['Day']
s29= json_data['29']['Station']
d29 = 2
s29 = 6
# print(d29, s29)

# 30 Row
d30= json_data['30']['Day']
s30= json_data['30']['Station']
d30 = 2
s30 = 7
# print(d30, s30)

# 31 Row
d31= json_data['31']['Day']
s31= json_data['31']['Station']
d31 = 2
s31 = 8
# print(d31, s31)

# 32 Row
d32= json_data['32']['Day']
s32= json_data['32']['Station']
d32 = 2
s32 = 9
# print(d32, s32)

# 33 Row
d33= json_data['33']['Day']
s33= json_data['33']['Station']
d33 = 2
s33 = 10
# print(d33, s33)

# 34 Row
d34= json_data['34']['Day']
s34= json_data['34']['Station']
d34 = 3
s34 = 0
# print(d34, s34)

# 35 Row
d35= json_data['35']['Day']
s35= json_data['35']['Station']
d35 = 3
s35 = 1
# print(d35, s35)

# 36 Row
d36= json_data['36']['Day']
s36= json_data['36']['Station']
d36 = 3
s36 = 2
# print(d36, s36)

# 37 Row
d37= json_data['37']['Day']
s37= json_data['37']['Station']
d37 = 3
s37 = 3
# print(d37, s37)

# 38 Row
d38= json_data['38']['Day']
s38= json_data['38']['Station']
d38 = 3
s38 = 4
# print(d38, s38)

# 39 Row
d39= json_data['39']['Day']
s39= json_data['39']['Station']
d39 = 3
s39 = 5
# print(d39, s39)

# 40 Row
d40= json_data['40']['Day']
s40= json_data['40']['Station']
d40 = 3
s40 = 6
# print(d40, s40)

# 41 Row
d41= json_data['41']['Day']
s41= json_data['41']['Station']
d41 = 3
s41 = 7
# print(d41, s41)

# 42 Row
d42= json_data['42']['Day']
s42= json_data['42']['Station']
d42 = 3
s42 = 8
# print(d42, s42)

# 43 Row
d43= json_data['43']['Day']
s43= json_data['43']['Station']
d43 = 3
s43 = 9
# print(d43, s43)

# 44 Row
d44= json_data['44']['Day']
s44= json_data['44']['Station']
d44 = 3
s44 = 10
# print(d44, s44)

# 45 Row
d45= json_data['45']['Day']
s45= json_data['45']['Station']
d45 = 4
s45 = 0
# print(d45, s45)

# 46 Row
d46= json_data['46']['Day']
s46= json_data['46']['Station']
d46 = 4
s46 = 1
# print(d46, s46)

# 47 Row
d47= json_data['47']['Day']
s47= json_data['47']['Station']
d47 = 4
s47 = 2
# print(d47, s47)

# 48 Row
d48= json_data['48']['Day']
s48= json_data['48']['Station']
d48 = 4
s48 = 3
# print(d48, s48)

# 49 Row
d49= json_data['49']['Day']
s49= json_data['49']['Station']
d49 = 4
s49 = 4
# print(d49, s49)

# 50 Row
d50= json_data['50']['Day']
s50= json_data['50']['Station']
d50 = 4
s50 = 5
# print(d50, s50)

# 51 Row
d51= json_data['51']['Day']
s51= json_data['51']['Station']
d51 = 4
s51 = 6
# print(d51, s51)

# 52 Row
d52= json_data['52']['Day']
s52= json_data['52']['Station']
d52 = 4
s52 = 7
# print(d52, s52)

# 53 Row
d53= json_data['53']['Day']
s53= json_data['53']['Station']
d53 = 4
s53 = 8
# print(d53, s53)

# 54 Row
d54= json_data['54']['Day']
s54= json_data['54']['Station']
d54 = 4
s54 = 9
# print(d54, s54)

# 55 Row
d55= json_data['55']['Day']
s55= json_data['55']['Station']
d55 = 4
s55 = 10
# print(d55, s55)

# 56 Row
d56= json_data['56']['Day']
s56= json_data['56']['Station']
d56 = 5
s56 = 0
# print(d56, s56)

# 57 Row
d57= json_data['57']['Day']
s57= json_data['57']['Station']
d57 = 5
s57 = 1
# print(d57, s57)

# 58 Row
d58= json_data['58']['Day']
s58= json_data['58']['Station']
d58 = 5
s58 = 2
# print(d58, s58)

# 59 Row
d59= json_data['59']['Day']
s59= json_data['59']['Station']
d59 = 5
s59 = 3
# print(d59, s59)

# 60 Row
d60= json_data['60']['Day']
s60= json_data['60']['Station']
d60 = 5
s60 = 4
# print(d60, s60)

# 61 Row
d61= json_data['61']['Day']
s61= json_data['61']['Station']
d61 = 5
s61 = 5
# print(d61, s61)

# 62 Row
d62= json_data['62']['Day']
s62= json_data['62']['Station']
d62 = 5
s62 = 6
# print(d62, s62)

# 63 Row
d63= json_data['63']['Day']
s63= json_data['63']['Station']
d63 = 5
s63 = 7
# print(d63, s63)

# 64 Row
d64= json_data['64']['Day']
s64= json_data['64']['Station']
d64 = 5
s64 = 8
# print(d64, s64)

# 65 Row
d65= json_data['65']['Day']
s65= json_data['65']['Station']
d65 = 5
s65 = 9
# print(d65, s65)

# 66 Row
d66= json_data['66']['Day']
s66= json_data['66']['Station']
d66 = 5
s66 = 10
# print(d66, s66)

# 67 Row
d67= json_data['67']['Day']
s67= json_data['67']['Station']
d67 = 6
s67 = 0
# print(d67, s67)

# 68 Row
d68= json_data['68']['Day']
s68= json_data['68']['Station']
d68 = 6
s68 = 1
# print(d68, s68)

# 69 Row
d69= json_data['69']['Day']
s69= json_data['69']['Station']
d69 = 6
s69 = 2
# print(d69, s69)

# 70 Row
d70= json_data['70']['Day']
s70= json_data['70']['Station']
d70 = 6
s70 = 3
# print(d70, s70)

# 71 Row
d71= json_data['71']['Day']
s71= json_data['71']['Station']
d71 = 6
s71 = 4
# print(d71, s71)

# 72 Row
d72= json_data['72']['Day']
s72= json_data['72']['Station']
d72 = 6
s72 = 5
# print(d72, s72)

# 73 Row
d73= json_data['73']['Day']
s73= json_data['73']['Station']
d73 = 6
s73 = 6
# print(d73, s73)

# 74 Row
d74= json_data['74']['Day']
s74= json_data['74']['Station']
d74 = 6
s74 = 7
# print(d74, s74)

# 75 Row
d75= json_data['75']['Day']
s75= json_data['75']['Station']
d75 = 6
s75 = 8
# print(d75, s75)

# 76 Row
d76= json_data['76']['Day']
s76= json_data['76']['Station']
d76 = 6
s76 = 9
# print(d76, s76)

# 77 Row
d77= json_data['77']['Day']
s77= json_data['77']['Station']
d77 = 6
s77 = 10
# print(d77, s77)

# 78 Row
d78= json_data['78']['Day']
s78= json_data['78']['Station']
d78 = 0
s78 = 0
# print(d78, s78)

# 79 Row
d79= json_data['79']['Day']
s79= json_data['79']['Station']
d79 = 0
s79 = 1
# print(d79, s79)

# 80 Row
d80= json_data['80']['Day']
s80= json_data['80']['Station']
d80 = 0
s80 = 2
# print(d80, s80)

# 81 Row
d81= json_data['81']['Day']
s81= json_data['81']['Station']
d81 = 0
s81 = 3
# print(d81, s81)

# 82 Row
d82= json_data['82']['Day']
s82= json_data['82']['Station']
d82 = 0
s82 = 4
# print(d82, s82)

# 83 Row
d83= json_data['83']['Day']
s83= json_data['83']['Station']
d83 = 0
s83 = 5
# print(d83, s83)

# 84 Row
d84= json_data['84']['Day']
s84= json_data['84']['Station']
d84 = 0
s84 = 6
# print(d84, s84)

# 85 Row
d85= json_data['85']['Day']
s85= json_data['85']['Station']
d85 = 0
s85 = 7
# print(d85, s85)

# 86 Row
d86= json_data['86']['Day']
s86= json_data['86']['Station']
d86 = 0
s86 = 8
# print(d86, s86)

# 87 Row
d87= json_data['87']['Day']
s87= json_data['87']['Station']
d87 = 0
s87 = 9
# print(d87, s87)

# 88 Row
d88= json_data['88']['Day']
s88= json_data['88']['Station']
d88 = 0
s88 = 10
# print(d88, s88)

# 89 Row
d89= json_data['89']['Day']
s89= json_data['89']['Station']
d89 = 1
s89 = 0
# print(d89, s89)

# 90 Row
d90= json_data['90']['Day']
s90= json_data['90']['Station']
d90 = 1
s90 = 1
# print(d90, s90)

# 91 Row
d91= json_data['91']['Day']
s91= json_data['91']['Station']
d91 = 1
s91 = 2
# print(d91, s91)

# 92 Row
d92= json_data['92']['Day']
s92= json_data['92']['Station']
d92 = 1
s92 = 3
# print(d92, s92)

# 93 Row
d93= json_data['93']['Day']
s93= json_data['93']['Station']
d93 = 1
s93 = 4
# print(d93, s93)

# 94 Row
d94= json_data['94']['Day']
s94= json_data['94']['Station']
d94 = 1
s94 = 5
# print(d94, s94)

# 95 Row
d95= json_data['95']['Day']
s95= json_data['95']['Station']
d95 = 1
s95 = 6
# print(d95, s95)

# 96 Row
d96= json_data['96']['Day']
s96= json_data['96']['Station']
d96 = 1
s96 = 7
# print(d96, s96)

# 97 Row
d97= json_data['97']['Day']
s97= json_data['97']['Station']
d97 = 1
s97 = 8
# print(d97, s97)

# 98 Row
d98= json_data['98']['Day']
s98= json_data['98']['Station']
d98 = 1
s98 = 9
# print(d98, s98)

# 99 Row
d99= json_data['99']['Day']
s99= json_data['99']['Station']
d99 = 1
s99 = 10
# print(d99, s99)

# 100 Row
d100= json_data['100']['Day']
s100= json_data['100']['Station']
d100 = 2
s100 = 0
# print(d100, s100)

# 101 Row
d101= json_data['101']['Day']
s101= json_data['101']['Station']
d101 = 2
s101 = 1
# print(d101, s101)

# 102 Row
d102= json_data['102']['Day']
s102= json_data['102']['Station']
d102 = 2
s102 = 2
# print(d102, s102)

# 103 Row
d103= json_data['103']['Day']
s103= json_data['103']['Station']
d103 = 2
s103 = 3
# print(d103, s103)

# 104 Row
d104= json_data['104']['Day']
s104= json_data['104']['Station']
d104 = 2
s104 = 4
# print(d104, s104)

# 105 Row
d105= json_data['105']['Day']
s105= json_data['105']['Station']
d105 = 2
s105 = 5
# print(d105, s105)

# 106 Row
d106= json_data['106']['Day']
s106= json_data['106']['Station']
d106 = 2
s106 = 6
# print(d106, s106)

# 107 Row
d107= json_data['107']['Day']
s107= json_data['107']['Station']
d107 = 2
s107 = 7
# print(d107, s107)

# 108 Row
d108= json_data['108']['Day']
s108= json_data['108']['Station']
d108 = 2
s108 = 8
# print(d108, s108)

# 109 Row
d109= json_data['109']['Day']
s109= json_data['109']['Station']
d109 = 2
s109 = 9
# print(d109, s109)

# 110 Row
d110= json_data['110']['Day']
s110= json_data['110']['Station']
d110 = 2
s110 = 10
# print(d110, s110)

# 111 Row
d111= json_data['111']['Day']
s111= json_data['111']['Station']
d111 = 3
s111 = 0
# print(d111, s111)

# 112 Row
d112= json_data['112']['Day']
s112= json_data['112']['Station']
d112 = 3
s112 = 1
# print(d112, s112)

# 113 Row
d113= json_data['113']['Day']
s113= json_data['113']['Station']
d113 = 3
s113 = 2
# print(d113, s113)

# 114 Row
d114= json_data['114']['Day']
s114= json_data['114']['Station']
d114 = 3
s114 = 3
# print(d114, s114)

# 115 Row
d115= json_data['115']['Day']
s115= json_data['115']['Station']
d115 = 3
s115 = 4
# print(d115, s115)

# 116 Row
d116= json_data['116']['Day']
s116= json_data['116']['Station']
d116 = 3
s116 = 5
# print(d116, s116)

# 117 Row
d117= json_data['117']['Day']
s117= json_data['117']['Station']
d117 = 3
s117 = 6
# print(d117, s117)

# 118 Row
d118= json_data['118']['Day']
s118= json_data['118']['Station']
d118 = 3
s118 = 7
# print(d118, s118)

# 119 Row
d119= json_data['119']['Day']
s119= json_data['119']['Station']
d119 = 3
s119 = 8
# print(d119, s119)

# 120 Row
d120= json_data['120']['Day']
s120= json_data['120']['Station']
d120 = 3
s120 = 9
# print(d120, s120)

# 121 Row
d121= json_data['121']['Day']
s121= json_data['121']['Station']
d121 = 3
s121 = 10
# print(d121, s121)

# 122 Row
d122= json_data['122']['Day']
s122= json_data['122']['Station']
d122 = 4
s122 = 0
# print(d122, s122)

# 123 Row
d123= json_data['123']['Day']
s123= json_data['123']['Station']
d123 = 4
s123 = 1
# print(d123, s123)

# 124 Row
d124= json_data['124']['Day']
s124= json_data['124']['Station']
d124 = 4
s124 = 2
# print(d124, s124)

# 125 Row
d125= json_data['125']['Day']
s125= json_data['125']['Station']
d125 = 4
s125 = 3
# print(d125, s125)

# 126 Row
d126= json_data['126']['Day']
s126= json_data['126']['Station']
d126 = 4
s126 = 4
# print(d126, s126)

# 127 Row
d127= json_data['127']['Day']
s127= json_data['127']['Station']
d127 = 4
s127 = 5
# print(d127, s127)

# 128 Row
d128= json_data['128']['Day']
s128= json_data['128']['Station']
d128 = 4
s128 = 6
# print(d128, s128)

# 129 Row
d129= json_data['129']['Day']
s129= json_data['129']['Station']
d129 = 4
s129 = 7
# print(d129, s129)

# 130 Row
d130= json_data['130']['Day']
s130= json_data['130']['Station']
d130 = 4
s130 = 8
# print(d130, s130)

# 131 Row
d131= json_data['131']['Day']
s131= json_data['131']['Station']
d131 = 4
s131 = 9
# print(d131, s131)

# 132 Row
d132= json_data['132']['Day']
s132= json_data['132']['Station']
d132 = 4
s132 = 10
# print(d132, s132)

# 133 Row
d133= json_data['133']['Day']
s133= json_data['133']['Station']
d133 = 5
s133 = 0
# print(d133, s133)

# 134 Row
d134= json_data['134']['Day']
s134= json_data['134']['Station']
d134 = 5
s134 = 1
# print(d134, s134)

# 135 Row
d135= json_data['135']['Day']
s135= json_data['135']['Station']
d135 = 5
s135 = 2
# print(d135, s135)

# 136 Row
d136= json_data['136']['Day']
s136= json_data['136']['Station']
d136 = 5
s136 = 3
# print(d136, s136)

# 137 Row
d137= json_data['137']['Day']
s137= json_data['137']['Station']
d137 = 5
s137 = 4
# print(d137, s137)

# 138 Row
d138= json_data['138']['Day']
s138= json_data['138']['Station']
d138 = 5
s138 = 5
# print(d138, s138)

# 139 Row
d139= json_data['139']['Day']
s139= json_data['139']['Station']
d139 = 5
s139 = 6
# print(d139, s139)

# 140 Row
d140= json_data['140']['Day']
s140= json_data['140']['Station']
d140 = 5
s140 = 7
# print(d140, s140)

# 141 Row
d141= json_data['141']['Day']
s141= json_data['141']['Station']
d141 = 5
s141 = 8
# print(d141, s141)

# 142 Row
d142= json_data['142']['Day']
s142= json_data['142']['Station']
d142 = 5
s142 = 9
# print(d142, s142)

# 143 Row
d143= json_data['143']['Day']
s143= json_data['143']['Station']
d143 = 5
s143 = 10
# print(d143, s143)

# 144 Row
d144= json_data['144']['Day']
s144= json_data['144']['Station']
d144 = 6
s144 = 0
# print(d144, s144)

# 145 Row
d145= json_data['145']['Day']
s145= json_data['145']['Station']
d145 = 6
s145 = 1
# print(d145, s145)

# 146 Row
d146= json_data['146']['Day']
s146= json_data['146']['Station']
d146 = 6
s146 = 2
# print(d146, s146)

# 147 Row
d147= json_data['147']['Day']
s147= json_data['147']['Station']
d147 = 6
s147 = 3
# print(d147, s147)

# 148 Row
d148= json_data['148']['Day']
s148= json_data['148']['Station']
d148 = 6
s148 = 4
# print(d148, s148)

# 149 Row
d149= json_data['149']['Day']
s149= json_data['149']['Station']
d149 = 6
s149 = 5
# print(d149, s149)

# 150 Row
d150= json_data['150']['Day']
s150= json_data['150']['Station']
d150 = 6
s150 = 6
# print(d150, s150)

# 151 Row
d151= json_data['151']['Day']
s151= json_data['151']['Station']
d151 = 6
s151 = 7
# print(d151, s151)

# 152 Row
d152= json_data['152']['Day']
s152= json_data['152']['Station']
d152 = 6
s152 = 8
# print(d152, s152)

# 153 Row
d153= json_data['153']['Day']
s153= json_data['153']['Station']
d153 = 6
s153 = 9
# print(d153, s153)

# 154 Row
d154= json_data['154']['Day']
s154= json_data['154']['Station']
d154 = 6
s154 = 10
# print(d154, s154)

# 155 Row
d155= json_data['155']['Day']
s155= json_data['155']['Station']
d155 = 0
s155 = 0
#print(d155, s155)

# 156 Row
d156= json_data['156']['Day']
s156= json_data['156']['Station']
d156 = 0
s156 = 1
#print(d156, s156)

# 157 Row
d157= json_data['157']['Day']
s157= json_data['157']['Station']
d157 = 0
s157 = 2
#print(d157, s157)

# 158 Row
d158= json_data['158']['Day']
s158= json_data['158']['Station']
d158 = 0
s158 = 3
#print(d158, s158)

# 159 Row
d159= json_data['159']['Day']
s159= json_data['159']['Station']
d159 = 0
s159 = 4
#print(d159, s159)

# 160 Row
d160= json_data['160']['Day']
s160= json_data['160']['Station']
d160 = 0
s160 = 5
# print(d160, s160)

# 161 Row
d161= json_data['161']['Day']
s161= json_data['161']['Station']
d161 = 0
s161 = 6
#print(d161, s161)

# 162 Row
d162= json_data['162']['Day']
s162= json_data['162']['Station']
d162 = 0
s162 = 7
#print(d162, s162)

# 163 Row
d163= json_data['163']['Day']
s163= json_data['163']['Station']
d163 = 0
s163 = 8
# print(d163, s163)

# 164 Row
d164= json_data['164']['Day']
s164= json_data['164']['Station']
d164 = 0
s164 = 9
# print(d164, s164)

# 165 Row
d165= json_data['165']['Day']
s165= json_data['165']['Station']
d165 = 0
s165 = 10
# print(d165, s165)

# 166 Row
d166= json_data['166']['Day']
s166= json_data['166']['Station']
d166 = 1
s166 = 0
# print(d166, s166)

# 167 Row
d167= json_data['167']['Day']
s167= json_data['167']['Station']
d167 = 1
s167 = 1
# print(d167, s167)

# 168 Row
d168= json_data['168']['Day']
s168= json_data['168']['Station']
d168 = 1
s168 = 2
# print(d168, s168)

# 169 Row
d169= json_data['169']['Day']
s169= json_data['169']['Station']
d169 = 1
s169 = 3
# print(d169, s169)

# 170 Row
d170= json_data['170']['Day']
s170= json_data['170']['Station']
d170 = 1
s170 = 4
# print(d170, s170)

# 171 Row
d171= json_data['171']['Day']
s171= json_data['171']['Station']
d171 = 1
s171 = 5
# print(d171, s171)

# 172 Row
d172= json_data['172']['Day']
s172= json_data['172']['Station']
d172 = 1
s172 = 6
# print(d172, s172)

# 173 Row
d173= json_data['173']['Day']
s173= json_data['173']['Station']
d173 = 1
s173 = 7
# print(d173, s173)

# 174 Row
d174= json_data['174']['Day']
s174= json_data['174']['Station']
d174 = 1
s174 = 8
# print(d174, s174)

# 175 Row
d175= json_data['175']['Day']
s175= json_data['175']['Station']
d175 = 1
s175 = 9
# print(d175, s175)

# 176 Row
d176= json_data['176']['Day']
s176= json_data['176']['Station']
d176 = 1
s176 = 10
# print(d176, s176)

# 177 Row
d177= json_data['177']['Day']
s177= json_data['177']['Station']
d177 = 2
s177 = 0
# print(d177, s177)

# 178 Row
d178= json_data['178']['Day']
s178= json_data['178']['Station']
d178 = 2
s178 = 1
# print(d178, s178)

# 179 Row
d179= json_data['179']['Day']
s179= json_data['179']['Station']
d179 = 2
s179 = 2
# print(d179, s179)

# 180 Row
d180= json_data['180']['Day']
s180= json_data['180']['Station']
d180 = 2
s180 = 3
# print(d180, s180)

# 181 Row
d181= json_data['181']['Day']
s181= json_data['181']['Station']
d181 = 2
s181 = 4
# print(d181, s181)

# 182 Row
d182= json_data['182']['Day']
s182= json_data['182']['Station']
d182 = 2
s182 = 5
# print(d182, s182)

# 183 Row
d183= json_data['183']['Day']
s183= json_data['183']['Station']
d183 = 2
s183 = 6
# print(d183, s183)

# 184 Row
d184= json_data['184']['Day']
s184= json_data['184']['Station']
d184 = 2
s184 = 7
# print(d184, s184)

# 185 Row
d185= json_data['185']['Day']
s185= json_data['185']['Station']
d185 = 2
s185 = 8
# print(d185, s185)

# 186 Row
d186= json_data['186']['Day']
s186= json_data['186']['Station']
d186 = 2
s186 = 9
# print(d186, s186)

# 187 Row
d187= json_data['187']['Day']
s187= json_data['187']['Station']
d187 = 2
s187 = 10
# print(d187, s187)

# 188 Row
d188= json_data['188']['Day']
s188= json_data['188']['Station']
d188 = 3
s188 = 0
# print(188, s188)

# 189 Row
d189= json_data['189']['Day']
s189= json_data['189']['Station']
d189 = 3
s189 = 1
# print(d189, s189)

# 190 Row
d190= json_data['190']['Day']
s190= json_data['190']['Station']
d190 = 3
s190 = 2
# print(d190, s190)

# 191 Row
d191= json_data['191']['Day']
s191= json_data['191']['Station']
d191 = 3
s191 = 3
# print(d191, s191)

# 192 Row
d192= json_data['192']['Day']
s192= json_data['192']['Station']
d192 = 3
s192 = 4
# print(d192, s192)

# 193 Row
d193= json_data['193']['Day']
s193= json_data['193']['Station']
d193 = 3
s193 = 5
# print(d193, s193)

# 194 Row
d194= json_data['194']['Day']
s194= json_data['194']['Station']
d194 = 3
s194 = 6
# print(d194, s194)

# 195 Row
d195= json_data['195']['Day']
s195= json_data['195']['Station']
d195 = 3
s195 = 7
# print(d195, s195)

# 196 Row
d196= json_data['196']['Day']
s196= json_data['196']['Station']
d196 = 3
s196 = 8
# print(d196, s196)

# 197 Row
d197= json_data['197']['Day']
s197= json_data['197']['Station']
d197 = 3
s197 = 9
# print(d197, s197)

# 198 Row
d198= json_data['198']['Day']
s198= json_data['198']['Station']
d198 = 3
s198 = 10
# print(d198, s198)

# 199 Row
d199= json_data['199']['Day']
s199= json_data['199']['Station']
d199 = 4
s199 = 0
# print(d199, s199)

# 200 Row
d200= json_data['200']['Day']
s200= json_data['200']['Station']
d200 = 4
s200 = 1
# print(d200, s200)

# 201 Row
d201= json_data['201']['Day']
s201= json_data['201']['Station']
d201 = 4
s201 = 2
# print(d201, s201)

# 202 Row
d202= json_data['202']['Day']
s202= json_data['202']['Station']
d202 = 4
s202 = 3
# print(d202, s202)

# 203 Row
d203= json_data['203']['Day']
s203= json_data['203']['Station']
d203 = 4
s203 = 4
# print(d203, s203)

# 204 Row
d204= json_data['204']['Day']
s204= json_data['204']['Station']
d204 = 4
s204 = 5
# print(d204, s204)

# 205 Row
d205= json_data['205']['Day']
s205= json_data['205']['Station']
d205 = 4
s205 = 6
# print(d205, s205)

# 206 Row
d206= json_data['206']['Day']
s206= json_data['206']['Station']
d206 = 4
s206 = 7
# print(d206, s206)

# 207 Row
d207= json_data['207']['Day']
s207= json_data['207']['Station']
d207 = 4
s207 = 8
# print(d207, s207)

# 208 Row
d208= json_data['208']['Day']
s208= json_data['208']['Station']
d208 = 4
s208 = 9
# print(d208, s208)

# 209 Row
d209= json_data['209']['Day']
s209= json_data['209']['Station']
d209 = 4
s209 = 10
# print(d209, s209)

# 210 Row
d210= json_data['210']['Day']
s210= json_data['210']['Station']
d210 = 5
s210 = 0
# print(d210, s210)

# 211 Row
d211= json_data['211']['Day']
s211= json_data['211']['Station']
d211 = 5
s211 = 1
# print(d211, s211)

# 212 Row
d212= json_data['212']['Day']
s212= json_data['212']['Station']
d212 = 5
s212 = 2
# print(d212, s212)

# 213 Row
d213= json_data['213']['Day']
s213= json_data['213']['Station']
d213 = 5
s213 = 3
# print(d213, s213)

# 214 Row
d214= json_data['214']['Day']
s214= json_data['214']['Station']
d214 = 5
s214 = 4
# print(d214, s214)

# 215 Row
d215= json_data['215']['Day']
s215= json_data['215']['Station']
d215 = 5
s215 = 5
# print(d215, s215)

# 216 Row
d216= json_data['216']['Day']
s216= json_data['216']['Station']
d216 = 5
s216 = 6
# print(d216, s216)

# 217 Row
d217= json_data['217']['Day']
s217= json_data['217']['Station']
d217 = 5
s217 = 7
# print(d217, s217)

# 218 Row
d218= json_data['218']['Day']
s218= json_data['218']['Station']
d218 = 5
s218 = 8
# print(d218, s218)

# 219 Row
d219= json_data['219']['Day']
s219= json_data['219']['Station']
d219 = 5
s219 = 9
# print(d219, s219)

# 220 Row
d220= json_data['220']['Day']
s220= json_data['220']['Station']
d220 = 5
s220 = 10
# print(d220, s220)

# 221 Row
d221= json_data['221']['Day']
s221= json_data['221']['Station']
d221 = 6
s221 = 0
# print(d221, s221)

# 222 Row
d222= json_data['222']['Day']
s222= json_data['222']['Station']
d222 = 6
s222 = 1
# print(d222, s222)

# 223 Row
d223= json_data['223']['Day']
s223= json_data['223']['Station']
d223 = 6
s223 = 2
# print(d223, s223)

# 224 Row
d224= json_data['224']['Day']
s224= json_data['224']['Station']
d224 = 6
s224 = 3
# print(d224, s224)

# 225 Row
d225= json_data['225']['Day']
s225= json_data['225']['Station']
d225 = 6
s225 = 4
# print(d225, s225)

# 226 Row
d226= json_data['226']['Day']
s226= json_data['226']['Station']
d226 = 6
s226 = 5
# print(d226, s226)

# 227 Row
d227= json_data['227']['Day']
s227= json_data['227']['Station']
d227 = 6
s227 = 6
# print(d227, s227)

# 228 Row
d228= json_data['228']['Day']
s228= json_data['228']['Station']
d228 = 6
s228 = 7
# print(d228, s228)

# 229 Row
d229= json_data['229']['Day']
s229= json_data['229']['Station']
d229 = 6
s229 = 8
# print(d229, s229)

# 230 Row
d230= json_data['230']['Day']
s230= json_data['230']['Station']
d230 = 6
s230 = 9
# print(d230, s230)

# 231 Row
d231= json_data['231']['Day']
s231= json_data['231']['Station']
d231 = 6
s231 = 10
# print(d231, s231)

# 232 Row
d232= json_data['232']['Day']
s232= json_data['232']['Station']
d232 = 0
s232 = 0
#print(d232, s232)

# 233 Row
d233= json_data['233']['Day']
s233= json_data['233']['Station']
d233 = 0
s233 = 1
#print(d233, s233)

# 234 Row
d234= json_data['234']['Day']
s234= json_data['234']['Station']
d234 = 0
s234 = 2
#print(d234, s234)

# 235 Row
d235= json_data['235']['Day']
s235= json_data['235']['Station']
d235 = 0
s235 = 3
#print(d235, s235)

# 236 Row
d236= json_data['236']['Day']
s236= json_data['236']['Station']
d236 = 0
s236 = 4
#print(d236, s236)

# 237 Row
d237= json_data['237']['Day']
s237= json_data['237']['Station']
d237 = 0
s237 = 5
# print(d237, s237)

# 238 Row
d238= json_data['238']['Day']
s238= json_data['238']['Station']
d238 = 0
s238 = 6
#print(d238, s238)

# 239 Row
d239= json_data['239']['Day']
s239= json_data['239']['Station']
d239 = 0
s239 = 7
#print(d239, s239)

# 240 Row
d240= json_data['240']['Day']
s240= json_data['240']['Station']
d240 = 0
s240 = 8
# print(d240, s240)

# 241 Row
d241= json_data['241']['Day']
s241= json_data['241']['Station']
d241 = 0
s241 = 9
# print(d241, s241)

# 242 Row
d242= json_data['242']['Day']
s242= json_data['242']['Station']
d242 = 0
s242 = 10
# print(d242, s242)

# 243 Row
d243= json_data['243']['Day']
s243= json_data['243']['Station']
d243 = 1
s243 = 0
# print(d243, s243)

# 244 Row
d244= json_data['244']['Day']
s244= json_data['244']['Station']
d244 = 1
s244 = 1
# print(d244, s244)

# 245 Row
d245= json_data['245']['Day']
s245= json_data['245']['Station']
d245 = 1
s245 = 2
# print(d245, s245)

# 246 Row
d246= json_data['246']['Day']
s246= json_data['246']['Station']
d246 = 1
s246 = 3
# print(d246, s246)

# 247 Row
d247= json_data['247']['Day']
s247= json_data['247']['Station']
d247 = 1
s247 = 4
# print(d247, s247)

# 248 Row
d248= json_data['248']['Day']
s248= json_data['248']['Station']
d248 = 1
s248 = 5
# print(d248, s248)

# 249 Row
d249= json_data['249']['Day']
s249= json_data['249']['Station']
d249 = 1
s249 = 6
# print(d249, s249)

# 250 Row
d250= json_data['250']['Day']
s250= json_data['250']['Station']
d250 = 1
s250 = 7
# print(d250, s250)

# 251 Row
d251= json_data['251']['Day']
s251= json_data['251']['Station']
d251 = 1
s251 = 8
# print(d251, s251)

# 252 Row
d252= json_data['252']['Day']
s252= json_data['252']['Station']
d252 = 1
s252 = 9
# print(d252, s252)

# 253 Row
d253= json_data['253']['Day']
s253= json_data['253']['Station']
d253 = 1
s253 = 10
# print(d253, s253)

# 254 Row
d254= json_data['254']['Day']
s254= json_data['254']['Station']
d254 = 2
s254 = 0
# print(d254, s254)

# 255 Row
d255= json_data['255']['Day']
s255= json_data['255']['Station']
d255 = 2
s255 = 1
# print(d255, s255)

# 256 Row
d256= json_data['256']['Day']
s256= json_data['256']['Station']
d256 = 2
s256 = 2
# print(d256, s256)

# 257 Row
d257= json_data['257']['Day']
s257= json_data['257']['Station']
d257 = 2
s257 = 3
# print(d257, s257)

# 258 Row
d258= json_data['258']['Day']
s258= json_data['258']['Station']
d258 = 2
s258 = 4
# print(d258, s258)

# 259 Row
d259= json_data['259']['Day']
s259= json_data['259']['Station']
d259 = 2
s259 = 5
# print(d259, s259)

# 260 Row
d260= json_data['260']['Day']
s260= json_data['260']['Station']
d260 = 2
s260 = 6
# print(d260, s260)

# 261 Row
d261= json_data['261']['Day']
s261= json_data['261']['Station']
d261 = 2
s261 = 7
# print(d261, s261)

# 262 Row
d262= json_data['262']['Day']
s262= json_data['262']['Station']
d262 = 2
s262 = 8
# print(d262, s262)

# 263 Row
d263= json_data['263']['Day']
s263= json_data['263']['Station']
d263 = 2
s263 = 9
# print(d263, s263)

# 264 Row
d264= json_data['264']['Day']
s264= json_data['264']['Station']
d264 = 2
s264 = 10
# print(d264, s264)

# 265 Row
d265= json_data['265']['Day']
s265= json_data['265']['Station']
d265 = 3
s265 = 0
# print(d265, s265)

# 266 Row
d266= json_data['266']['Day']
s266= json_data['266']['Station']
d266 = 3
s266 = 1
# print(d266, s266)

# 267 Row
d267= json_data['267']['Day']
s267= json_data['267']['Station']
d267 = 3
s267 = 2
# print(d267, s267)

# 268 Row
d268= json_data['268']['Day']
s268= json_data['268']['Station']
d268 = 3
s268 = 3
# print(d268, s268)

# 269 Row
d269= json_data['269']['Day']
s269= json_data['269']['Station']
d269 = 3
s269 = 4
# print(d269, s269)

# 270 Row
d270= json_data['270']['Day']
s270= json_data['270']['Station']
d270 = 3
s270 = 5
# print(d270, s270)

# 271 Row
d271= json_data['271']['Day']
s271= json_data['271']['Station']
d271 = 3
s271 = 6
# print(d271, s271)

# 272 Row
d272= json_data['272']['Day']
s272= json_data['272']['Station']
d272 = 3
s272 = 7
# print(d272, s272)

# 273 Row
d273= json_data['273']['Day']
s273= json_data['273']['Station']
d273 = 3
s273 = 8
# print(d273, s273)

# 274 Row
d274= json_data['274']['Day']
s274= json_data['274']['Station']
d274 = 3
s274 = 9
# print(d274, s274)

# 275 Row
d275= json_data['275']['Day']
s275= json_data['275']['Station']
d275 = 3
s275 = 10
# print(d275, s275)

# 276 Row
d276= json_data['276']['Day']
s276= json_data['276']['Station']
d276 = 4
s276 = 0
# print(d276, s276)

# 277 Row
d277= json_data['277']['Day']
s277= json_data['277']['Station']
d277 = 4
s277 = 1
# print(d277, s277)

# 278 Row
d278= json_data['278']['Day']
s278= json_data['278']['Station']
d278 = 4
s278 = 2
# print(d278, s278)

# 279 Row
d279= json_data['279']['Day']
s279= json_data['279']['Station']
d279 = 4
s279 = 3
# print(d279, s279)

# 280 Row
d280= json_data['280']['Day']
s280= json_data['280']['Station']
d280 = 4
s280 = 4
# print(d280, s280)

# 281 Row
d281= json_data['281']['Day']
s281= json_data['281']['Station']
d281 = 4
s281 = 5
# print(d281, s281)

# 282 Row
d282= json_data['282']['Day']
s282= json_data['282']['Station']
d282 = 4
s282 = 6
# print(d282, s282)

# 283 Row
d283= json_data['283']['Day']
s283= json_data['283']['Station']
d283 = 4
s283 = 7
# print(d283, s283)

# 284 Row
d284= json_data['284']['Day']
s284= json_data['284']['Station']
d284 = 4
s284 = 8
# print(d284, s284)

# 285 Row
d285= json_data['285']['Day']
s285= json_data['285']['Station']
d285 = 4
s285 = 9
# print(d285, s285)

# 286 Row
d286= json_data['286']['Day']
s286= json_data['286']['Station']
d286 = 4
s286 = 10
# print(d286, s286)

# 287 Row
d287= json_data['287']['Day']
s287= json_data['287']['Station']
d287 = 5
s287 = 0
# print(d287, s287)

# 288 Row
d288= json_data['288']['Day']
s288= json_data['288']['Station']
d288 = 5
s288 = 1
# print(d288, s288)

# 289 Row
d289= json_data['289']['Day']
s289= json_data['289']['Station']
d289 = 5
s289 = 2
# print(d289, s289)

# 290 Row
d290= json_data['290']['Day']
s290= json_data['290']['Station']
d290 = 5
s290 = 3
# print(d290, s290)

# 291 Row
d291= json_data['291']['Day']
s291= json_data['291']['Station']
d291 = 5
s291 = 4
# print(d291, s291)

# 292 Row
d292= json_data['292']['Day']
s292= json_data['292']['Station']
d292 = 5
s292 = 5
# print(d292, s292)

# 293 Row
d293= json_data['293']['Day']
s293= json_data['293']['Station']
d293 = 5
s293 = 6
# print(d293, s293)

# 294 Row
d294= json_data['294']['Day']
s294= json_data['294']['Station']
d294 = 5
s294 = 7
# print(d294, s294)

# 295 Row
d295= json_data['295']['Day']
s295= json_data['295']['Station']
d295 = 5
s295 = 8
# print(d295, s295)

# 296 Row
d296= json_data['296']['Day']
s296= json_data['296']['Station']
d296 = 5
s296 = 9
# print(d296, s296)

# 297 Row
d297= json_data['297']['Day']
s297= json_data['297']['Station']
d297 = 5
s297 = 10
# print(d297, s297)

# 298 Row
d298= json_data['298']['Day']
s298= json_data['298']['Station']
d298 = 6
s298 = 0
# print(d298, s298)

# 299 Row
d299= json_data['299']['Day']
s299= json_data['299']['Station']
d299 = 6
s299 = 1
# print(d299, s299)

# 300 Row
d300= json_data['300']['Day']
s300= json_data['300']['Station']
d300 = 6
s300 = 2
# print(d300, s300)

# 301 Row
d301= json_data['301']['Day']
s301= json_data['301']['Station']
d301 = 6
s301 = 3
# print(d301, s301)

# 302 Row
d302= json_data['302']['Day']
s302= json_data['302']['Station']
d302 = 6
s302 = 4
# print(d302, s302)

# 303 Row
d303= json_data['303']['Day']
s303= json_data['303']['Station']
d303 = 6
s303 = 5
# print(d303, s303)

# 304 Row
d304= json_data['304']['Day']
s304= json_data['304']['Station']
d304 = 6
s304 = 6
# print(d304, s304)

# 305 Row
d305= json_data['305']['Day']
s305= json_data['305']['Station']
d305 = 6
s305 = 7
# print(d305, s305)

# 306 Row
d306= json_data['306']['Day']
s306= json_data['306']['Station']
d306 = 6
s306 = 8
# print(d306, s306)

# 307 Row
d307= json_data['307']['Day']
s307= json_data['307']['Station']
d307 = 6
s307 = 9
# print(d307, s307)

# 308 Row
d308= json_data['308']['Day']
s308= json_data['308']['Station']
d308 = 6
s308 = 10
# print(d308, s308)

# 309 Row
d309= json_data['309']['Day']
s309= json_data['309']['Station']
d309 = 0
s309 = 0
#print(d309, s309)

# 310 Row
d310= json_data['310']['Day']
s310= json_data['310']['Station']
d310 = 0
s310 = 1
#print(d310, s310)

# 311 Row
d311= json_data['311']['Day']
s311= json_data['311']['Station']
d311 = 0
s311 = 2
#print(d311, s311)

# 312 Row
d312= json_data['312']['Day']
s312= json_data['312']['Station']
d312 = 0
s312 = 3
#print(d312, s312)

# 313 Row
d313= json_data['313']['Day']
s313= json_data['313']['Station']
d313 = 0
s313 = 4
#print(d313, s313)

# 314 Row
d314= json_data['314']['Day']
s314= json_data['314']['Station']
d314 = 0
s314 = 5
# print(d314, s314)

# 315 Row
d315= json_data['315']['Day']
s315= json_data['315']['Station']
d315 = 0
s315 = 6
#print(d315, s315)

# 316 Row
d316= json_data['316']['Day']
s316= json_data['316']['Station']
d316 = 0
s316 = 7
#print(d316, s316)

# 317 Row
d317= json_data['317']['Day']
s317= json_data['317']['Station']
d317 = 0
s317 = 8
# print(d317, s317)

# 318 Row
d318= json_data['318']['Day']
s318= json_data['318']['Station']
d318 = 0
s318 = 9
# print(d318, s318)

# 319 Row
d319= json_data['319']['Day']
s319= json_data['319']['Station']
d319 = 0
s319 = 10
# print(d319, s319)

# 320 Row
d320= json_data['320']['Day']
s320= json_data['320']['Station']
d320 = 1
s320 = 0
# print(d320, s320)

# 321 Row
d321= json_data['321']['Day']
s321= json_data['321']['Station']
d321 = 1
s321 = 1
# print(d321, s321)

# 322 Row
d322= json_data['322']['Day']
s322= json_data['322']['Station']
d322 = 1
s322 = 2
# print(d322, s322)

# 323 Row
d323= json_data['323']['Day']
s323= json_data['323']['Station']
d323 = 1
s323 = 3
# print(d323, s323)

# 324 Row
d324= json_data['324']['Day']
s324= json_data['324']['Station']
d324 = 1
s324 = 4
# print(d324, s324)

# 325 Row
d325= json_data['325']['Day']
s325= json_data['325']['Station']
d325 = 1
s325 = 5
# print(d325, s325)

# 326 Row
d326= json_data['326']['Day']
s326= json_data['326']['Station']
d326 = 1
s326 = 6
# print(d326, s326)

# 327 Row
d327= json_data['327']['Day']
s327= json_data['327']['Station']
d327 = 1
s327 = 7
# print(d327, s327)

# 328 Row
d328= json_data['328']['Day']
s328= json_data['328']['Station']
d328 = 1
s328 = 8
# print(d328, s328)

# 329 Row
d329= json_data['329']['Day']
s329= json_data['329']['Station']
d329 = 1
s329 = 9
# print(d329, s329)

# 330 Row
d330= json_data['330']['Day']
s330= json_data['330']['Station']
d330 = 1
s330 = 10
# print(d330, s330)

features = [[d1,s1], [d2,s2], [d3,s3], [d4,s4], [d5,s5], [d6,s6], [d7,s7], [d8,s8], [d9,s9], [d10,s10],
            [d11,s11], [d12,s12], [d13,s13], [d14,s14], [d15,s15], [d16,s16], [d17,s17], [d18,s18], [d19,s19], [d20,s20],
            [d21,s21], [d22,s22], [d23,s23], [d24,s24], [d25,s25], [d26,s26], [d27,s27], [d28,s28], [d29,s29], [d30,s30],
            [d31,s31], [d32,s32], [d33,s33], [d34,s34], [d35,s35], [d36,s36], [d37,s37], [d38,s38], [d39,s39], [d40,s40],
            [d41,s41], [d42,s42], [d43,s43], [d44,s44], [d45,s45], [d46,s46], [d47,s47], [d48,s48], [d49,s49], [d50,s50],
            [d51,s51], [d52,s52], [d53,s53], [d54,s54], [d55,s55], [d56,s56], [d57,s57], [d58,s58], [d59,s59], [d60,s60],
            [d61,s61], [d62,s62], [d63,s63], [d64,s64], [d65,s65], [d66,s66], [d67,s67], [d68,s68], [d69,s69], [d70,s70],
            [d71,s71], [d72,s72], [d73,s73], [d74,s74], [d75,s75], [d76,s76], [d77,s77], [d78,s78], [d79,s79], [d80,s80],
            [d81,s81], [d82,s82], [d83,s83], [d84,s84], [d85,s85], [d86,s86], [d87,s87], [d88,s88], [d89,s89], [d90,s90],
            [d91,s91], [d92,s92], [d93,s93], [d94,s94], [d95,s95], [d96,s96], [d97,s97], [d98,s98], [d99,s99], [d100,s100],
            [d101,s101], [d102,s102], [d103,s103], [d104,s104], [d105,s105], [d106,s106], [d107,s107], [d108,s108], [d109,s109], [d110,s110],
            [d111,s111], [d112,s112], [d113,s113], [d114,s114], [d115,s115], [d116,s116], [d117,s117], [d118,s118], [d119,s119], [d120,s120],
            [d121,s121], [d122,s122], [d123,s123], [d124,s124], [d125,s125], [d126,s126], [d127,s127], [d128,s128], [d129,s129], [d130,s130],
            [d131,s131], [d132,s132], [d133,s133], [d134,s134], [d135,s135], [d136,s136], [d137,s137], [d138,s138], [d139,s139], [d140,s140],
            [d141,s141], [d142,s142], [d143,s143], [d144,s144], [d145,s145], [d146,s146], [d147,s147], [d148,s148], [d149,s149], [d150,s150],
            [d151,s151], [d152,s152], [d153,s153], [d154,s154], [d155,s155], [d156,s156], [d157,s157], [d158,s158], [d159,s159], [d160,s160],
            [d161,s161], [d162,s162], [d163,s163], [d164,s164], [d165,s165], [d166,s166], [d167,s167], [d168,s168], [d169,s169], [d170,s170],
            [d171,s171], [d172,s172], [d173,s173], [d174,s174], [d175,s175], [d176,s176], [d177,s177], [d178,s178], [d179,s179], [d180,s180],
            [d181,s181], [d182,s182], [d183,s183], [d184,s184], [d185,s185], [d186,s186], [d187,s187], [d188,s188], [d189,s189], [d190,s190],
            [d191,s191], [d192,s192], [d193,s193], [d194,s194], [d195,s195], [d196,s196], [d197,s197], [d198,s198], [d199,s199], [d200,s200],
            [d201,s201], [d202,s202], [d203,s203], [d204,s204], [d205,s205], [d206,s206], [d207,s207], [d208,s208], [d209,s209], [d210,s210],
            [d211,s211], [d212,s212], [d213,s213], [d214,s214], [d215,s215], [d216,s216], [d217,s217], [d218,s218], [d219,s219], [d220,s220],
            [d221,s221], [d222,s222], [d223,s223], [d224,s224], [d225,s225], [d226,s226], [d227,s227], [d228,s228], [d229,s229], [d230,s230],
            [d231,s231], [d232,s232], [d233,s233], [d234,s234], [d235,s235], [d236,s236], [d237,s237], [d238,s238], [d239,s239], [d240,s240],
            [d241,s241], [d242,s242], [d243,s243], [d244,s244], [d245,s245], [d246,s246], [d247,s247], [d248,s248], [d249,s249], [d250,s250],
            [d251,s251], [d252,s252], [d253,s253], [d254,s254], [d255,s255], [d256,s256], [d257,s257], [d258,s258], [d259,s259], [d260,s260],
            [d261,s261], [d262,s262], [d263,s263], [d264,s264], [d265,s265], [d266,s266], [d267,s267], [d268,s268], [d269,s269], [d270,s270],
            [d271,s271], [d272,s272], [d273,s273], [d274,s274], [d275,s275], [d276,s276], [d277,s277], [d278,s278], [d279,s279], [d280,s280],
            [d281,s281], [d282,s282], [d283,s283], [d284,s284], [d285,s285], [d286,s286], [d287,s287], [d288,s288], [d289,s289], [d290,s290],
            [d291,s291], [d292,s292], [d293,s293], [d294,s294], [d295,s295], [d296,s296], [d297,s297], [d298,s298], [d299,s299], [d300,s300],
            [d301,s301], [d302,s302], [d303,s303], [d304,s304], [d305,s305], [d306,s306], [d307,s307], [d308,s308], [d309,s309], [d310,s310],
            [d311,s311], [d312,s312], [d313,s313], [d314,s314], [d315,s315], [d316,s316], [d317,s317], [d318,s318], [d319,s319], [d320,s320],
            [d321,s321], [d322,s322], [d323,s323], [d324,s324], [d325,s325], [d326,s326], [d327,s327], [d328,s328], [d329,s329], [d330,s330]]

labels = ["6:05","06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42","07:56:07:58","08:43:08:45",
          "8:49","6:08","06:21:06:22","06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35","07:44:07:45","07:59:08:01",
          "08:46:08:48","8:52","6:05","06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42",
          "07:56:07:58","08:43:08:45","8:49","6:08","06:21:06:22","06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35",
          "07:44:07:45","07:59:08:01","08:46:08:48","8:52","6:06","06:19:06:20","06:27:06:28","06:46:06:56","07:10:07:11","07:21:07:22",
          "07:32:07:33","07:42:07:43","07:57:07:59","08:44:08:46","8:50","6:07","06:20:06:21","06:28:06:29","06:47:06:57","07:11:07:12",
          "07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47","8:51","6:08","06:21:06:22","06:29:06:30","06:48:06:58",
          "07:12:07:13","07:23:07:24","07:34:07:35","07:44:07:45","07:59:08:01","08:46:08:48","8:52","6:06","06:19:06:20","06:27:06:28",
          "06:46:06:56","07:10:07:11","07:21:07:22","07:32:07:33","07:42:07:43","07:57:07:59","08:44:08:46","8:50","6:07","06:20:06:21",
          "06:28:06:29","06:47:06:57","07:11:07:12","07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47","8:51","6:06",
          "06:19:06:20","06:27:06:28","06:46:06:56","07:10:07:11","07:21:07:22","07:32:07:33","07:42:07:43","07:57:07:59","08:44:08:46","8:50",
          "6:07","06:20:06:21","06:28:06:29","06:47:06:57","07:11:07:12","07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47",
          "8:51","6:05","06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42","07:56:07:58",
          "08:43:08:45","8:49","6:08","06:21:06:22","06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35","07:44:07:45",
          "07:59:08:01","08:46:08:48","8:52","6:06","06:19:06:20","06:27:06:28","06:46:06:56","07:10:07:11","07:21:07:22","07:32:07:33",
          "07:42:07:43","07:57:07:59","08:44:08:46","8:50","6:04","06:17:06:18","06:25:06:26","06:44:06:54","07:08:07:09","07:19:07:20",
          "07:30:07:31","07:40:07:41","07:55:07:57","08:42:08:44","8:48","6:04","06:17:06:18","06:25:06:26","06:44:06:54","07:08:07:09",
          "07:19:07:20","07:30:07:31","07:40:07:41","07:55:07:57","08:42:08:44","8:48","6:07","06:20:06:21","06:28:06:29","06:47:06:57",
          "07:11:07:12","07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47","8:51","6:06","06:19:06:20","06:27:06:28",
          "06:46:06:56","07:10:07:11","07:21:07:22","07:32:07:33","07:42:07:43","07:57:07:59","08:44:08:46","8:50","6:08","06:21:06:22",
          "06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35","07:44:07:45","07:59:08:01","08:46:08:48","8:52","6:05",
          "06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42","07:56:07:58","08:43:08:45","8:49",
          "6:07","06:20:06:21","06:28:06:29","06:47:06:57","07:11:07:12","07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47",
          "8:51","6:07","06:20:06:21","06:28:06:29","06:47:06:57","07:11:07:12","07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00",
          "08:45:08:47","8:51","6:06","06:19:06:20","06:27:06:28","06:46:06:56","07:10:07:11","07:21:07:22","07:32:07:33","07:42:07:43",
          "07:57:07:59","08:44:08:46","8:50","6:08","06:21:06:22","06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35",
          "07:44:07:45","07:59:08:01","08:46:08:48","8:52","6:05","06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21",
          "07:31:07:32","07:41:07:42","07:56:07:58","08:43:08:45","8:49","6:07","06:20:06:21","06:28:06:29","06:47:06:57","07:11:07:12",
          "07:22:07:23","07:33:07:34","07:43:07:44","07:58:08:00","08:45:08:47","8:51","6:06","06:19:06:20","06:27:06:28","06:46:06:56",
          "07:10:07:11","07:21:07:22","07:32:07:33","07:42:07:43","07:57:07:59","08:44:08:46","8:50","6:05","06:18:06:19","06:26:06:27",
          "06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42","07:56:07:58","08:43:08:45","8:49","6:08","06:21:06:22",
          "06:29:06:30","06:48:06:58","07:12:07:13","07:23:07:24","07:34:07:35","07:44:07:45","07:59:08:01","08:46:08:48","8:52","6:05",
          "06:18:06:19","06:26:06:27","06:45:06:55","07:09:07:10","07:20:07:21","07:31:07:32","07:41:07:42","07:56:07:58","08:43:08:45","8:49"]

# ML
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# Monday results
mon_matara = clf.predict([[0,0]])
# coverting nd array to a str
mon_matara = ''.join(mon_matara)

mon_weligama = clf.predict([[0,1]])
mon_weligama = ''.join(mon_weligama)

mon_ahangama = clf.predict([[0,2]])
mon_ahangama = ''.join(mon_ahangama)

mon_galle = clf.predict([[0,3]])
mon_galle = ''.join(mon_galle)

mon_hikkaduwa = clf.predict([[0,4]])
mon_hikkaduwa = ''.join(mon_hikkaduwa)

mon_ambalangoda = clf.predict([[0,5]])
mon_ambalangoda = ''.join(mon_ambalangoda)

mon_kosgoda = clf.predict([[0,6]])
mon_kosgoda = ''.join(mon_kosgoda)

mon_aluthgama = clf.predict([[0,7]])
mon_aluthgama = ''.join(mon_aluthgama)

mon_kaluthara_south = clf.predict([[0,8]])
mon_kaluthara_south = ''.join(mon_kaluthara_south)

mon_colombo_fort = clf.predict([[0,9]])
mon_colombo_fort = ''.join(mon_colombo_fort)

mon_maradana = clf.predict([[0,10]])
mon_maradana = ''.join(mon_maradana)

# Tuesday results
tue_matara = clf.predict([[1,0]])
tue_matara = ''.join(tue_matara)

tue_weligama = clf.predict([[1,1]])
tue_weligama = ''.join(tue_weligama)

tue_ahangama = clf.predict([[1,2]])
tue_ahangama = ''.join(tue_ahangama)

tue_galle = clf.predict([[1,3]])
tue_galle = ''.join(tue_galle)

tue_hikkaduwa = clf.predict([[1,4]])
tue_hikkaduwa = ''.join(tue_hikkaduwa)

tue_ambalangoda = clf.predict([[1,5]])
tue_ambalangoda = ''.join(tue_ambalangoda)

tue_kosgoda = clf.predict([[1,6]])
tue_kosgoda = ''.join(tue_kosgoda)

tue_aluthgama = clf.predict([[1,7]])
tue_aluthgama = ''.join(tue_aluthgama)

tue_kaluthara_south = clf.predict([[1,8]])
tue_kaluthara_south = ''.join(tue_kaluthara_south)

tue_colombo_fort = clf.predict([[1,9]])
tue_colombo_fort = ''.join(tue_colombo_fort)

tue_maradana = clf.predict([[1,10]])
tue_maradana = ''.join(tue_maradana)

# Wednesday results
wed_matara = clf.predict([[2,0]])
wed_matara = ''.join(wed_matara)

wed_weligama = clf.predict([[2,1]])
wed_weligama = ''.join(wed_weligama)

wed_ahangama = clf.predict([[2,2]])
wed_ahangama = ''.join(wed_ahangama)

wed_galle = clf.predict([[2,3]])
wed_galle = ''.join(wed_galle)

wed_hikkaduwa = clf.predict([[2,4]])
wed_hikkaduwa = ''.join(wed_hikkaduwa)

wed_ambalangoda = clf.predict([[2,5]])
wed_ambalangoda = ''.join(wed_ambalangoda)

wed_kosgoda = clf.predict([[2,6]])
wed_kosgoda = ''.join(wed_kosgoda)

wed_aluthgama = clf.predict([[2,7]])
wed_aluthgama = ''.join(wed_aluthgama)

wed_kaluthara_south = clf.predict([[2,8]])
wed_kaluthara_south = ''.join(wed_kaluthara_south)

wed_colombo_fort = clf.predict([[2,9]])
wed_colombo_fort = ''.join(wed_colombo_fort)

wed_maradana = clf.predict([[2,10]])
wed_maradana = ''.join(wed_maradana)

# Thursday results
thu_matara = clf.predict([[3,0]])
thu_matara = ''.join(thu_matara)

thu_weligama = clf.predict([[3,1]])
thu_weligama = ''.join(thu_weligama)

thu_ahangama = clf.predict([[3,2]])
thu_ahangama = ''.join(thu_ahangama)

thu_galle = clf.predict([[3,3]])
thu_galle = ''.join(thu_galle)

thu_hikkaduwa = clf.predict([[3,4]])
thu_hikkaduwa = ''.join(thu_hikkaduwa)

thu_ambalangoda = clf.predict([[3,5]])
thu_ambalangoda = ''.join(thu_ambalangoda)

thu_kosgoda = clf.predict([[3,6]])
thu_kosgoda = ''.join(thu_kosgoda)

thu_aluthgama = clf.predict([[3,7]])
thu_aluthgama = ''.join(thu_aluthgama)

thu_kaluthara_south = clf.predict([[3,8]])
thu_kaluthara_south = ''.join(thu_kaluthara_south)

thu_colombo_fort = clf.predict([[3,9]])
thu_colombo_fort = ''.join(thu_colombo_fort)

thu_maradana = clf.predict([[3,10]])
thu_maradana = ''.join(thu_maradana)

# Friday results
fri_matara = clf.predict([[4,0]])
fri_matara = ''.join(fri_matara)

fri_weligama = clf.predict([[4,1]])
fri_weligama = ''.join(fri_weligama)

fri_ahangama = clf.predict([[4,2]])
fri_ahangama = ''.join(fri_ahangama)

fri_galle = clf.predict([[4,3]])
fri_galle = ''.join(fri_galle)

fri_hikkaduwa = clf.predict([[4,4]])
fri_hikkaduwa = ''.join(fri_hikkaduwa)

fri_ambalangoda = clf.predict([[4,5]])
fri_ambalangoda = ''.join(fri_ambalangoda)

fri_kosgoda = clf.predict([[4,6]])
fri_kosgoda = ''.join(fri_kosgoda)

fri_aluthgama = clf.predict([[4,7]])
fri_aluthgama = ''.join(fri_aluthgama)

fri_kaluthara_south = clf.predict([[4,8]])
fri_kaluthara_south = ''.join(fri_kaluthara_south)

fri_colombo_fort = clf.predict([[4,9]])
fri_colombo_fort = ''.join(fri_colombo_fort)

fri_maradana = clf.predict([[4,10]])
fri_maradana = ''.join(fri_maradana)

# saturday results
sat_matara = clf.predict([[5,0]])
sat_matara = ''.join(sat_matara)

sat_weligama = clf.predict([[5,1]])
sat_weligama = ''.join(sat_weligama)

sat_ahangama = clf.predict([[5,2]])
sat_ahangama = ''.join(sat_ahangama)

sat_galle = clf.predict([[5,3]])
sat_galle = ''.join(sat_galle)

sat_hikkaduwa = clf.predict([[5,4]])
sat_hikkaduwa = ''.join(sat_hikkaduwa)

sat_ambalangoda = clf.predict([[5,5]])
sat_ambalangoda = ''.join(sat_ambalangoda)

sat_kosgoda = clf.predict([[5,6]])
sat_kosgoda = ''.join(sat_kosgoda)

sat_aluthgama = clf.predict([[5,7]])
sat_aluthgama = ''.join(sat_aluthgama)

sat_kaluthara_south = clf.predict([[5,8]])
sat_kaluthara_south = ''.join(sat_kaluthara_south)

sat_colombo_fort = clf.predict([[5,9]])
sat_colombo_fort = ''.join(sat_colombo_fort)

sat_maradana = clf.predict([[5,10]])
sat_maradana = ''.join(sat_maradana)

# sunday results
sun_matara = clf.predict([[6,0]])
sun_matara = ''.join(sun_matara)

sun_weligama = clf.predict([[6,1]])
sun_weligama = ''.join(sun_weligama)

sun_ahangama = clf.predict([[6,2]])
sun_ahangama = ''.join(sun_ahangama)

sun_galle = clf.predict([[6,3]])
sun_galle = ''.join(sun_galle)

sun_hikkaduwa = clf.predict([[6,4]])
sun_hikkaduwa = ''.join(sun_hikkaduwa)

sun_ambalangoda = clf.predict([[6,5]])
sun_ambalangoda = ''.join(sun_ambalangoda)

sun_kosgoda = clf.predict([[6,6]])
sun_kosgoda = ''.join(sun_kosgoda)

sun_aluthgama = clf.predict([[6,7]])
sun_aluthgama = ''.join(sun_aluthgama)

sun_kaluthara_south = clf.predict([[6,8]])
sun_kaluthara_south = ''.join(sun_kaluthara_south)

sun_colombo_fort = clf.predict([[6,9]])
sun_colombo_fort = ''.join(sun_colombo_fort)

sun_maradana = clf.predict([[6,10]])
sun_maradana = ''.join(sun_maradana)

#json data
data = {
    "Monday": {
        "Matara": mon_matara,
        "Weligama": mon_weligama,
        "Ahangama": mon_ahangama,
        "Galle": mon_galle,
        "Hikkaduwa": mon_hikkaduwa,
        "Ambalangoda": mon_ambalangoda,
        "Kosgoda": mon_kosgoda,
        "Aluthgama": mon_aluthgama,
        "Kaluthara South": mon_kaluthara_south,
        "Colombo Fort": mon_colombo_fort,
        "Maradana": mon_maradana
    },
    "Tuesday": {
        "Matara": tue_matara,
        "Weligama": tue_weligama,
        "Ahangama": tue_ahangama,
        "Galle": tue_galle,
        "Hikkaduwa": tue_hikkaduwa,
        "Ambalangoda": tue_ambalangoda,
        "Kosgoda": tue_kosgoda,
        "Aluthgama": tue_aluthgama,
        "Kaluthara South": tue_kaluthara_south,
        "Colombo Fort": tue_colombo_fort,
        "Maradana": tue_maradana
    },
    "Wednesday": {
        "Matara": wed_matara,
        "Weligama": wed_weligama,
        "Ahangama": wed_ahangama,
        "Galle": wed_galle,
        "Hikkaduwa": wed_hikkaduwa,
        "Ambalangoda": wed_ambalangoda,
        "Kosgoda": wed_kosgoda,
        "Aluthgama": wed_aluthgama,
        "Kaluthara South": wed_kaluthara_south,
        "Colombo Fort": wed_colombo_fort,
        "Maradana": wed_maradana
    },
    "Thursday": {
        "Matara": thu_matara,
        "Weligama": thu_weligama,
        "Ahangama": thu_ahangama,
        "Galle": thu_galle,
        "Hikkaduwa": thu_hikkaduwa,
        "Ambalangoda": thu_ambalangoda,
        "Kosgoda": thu_kosgoda,
        "Aluthgama": thu_aluthgama,
        "Kaluthara South": thu_kaluthara_south,
        "Colombo Fort": thu_colombo_fort,
        "Maradana": thu_maradana
    },
    "Friday": {
        "Matara": fri_matara,
        "Weligama": fri_weligama,
        "Ahangama": fri_ahangama,
        "Galle": fri_galle,
        "Hikkaduwa": fri_hikkaduwa,
        "Ambalangoda": fri_ambalangoda,
        "Kosgoda": fri_kosgoda,
        "Aluthgama": fri_aluthgama,
        "Kaluthara South": fri_kaluthara_south,
        "Colombo Fort": fri_colombo_fort,
        "Maradana": fri_maradana
    },
    "Saturday": {
        "Matara": sat_matara,
        "Weligama": sat_weligama,
        "Ahangama": sat_ahangama,
        "Galle": sat_galle,
        "Hikkaduwa": sat_hikkaduwa,
        "Ambalangoda": sat_ambalangoda,
        "Kosgoda": sat_kosgoda,
        "Aluthgama": sat_aluthgama,
        "Kaluthara South": sat_kaluthara_south,
        "Colombo Fort": sat_colombo_fort,
        "Maradana": sat_maradana
    },
    "Sunday": {
        "Matara": sun_matara,
        "Weligama": sun_weligama,
        "Ahangama": sun_ahangama,
        "Galle": sun_galle,
        "Hikkaduwa": sun_hikkaduwa,
        "Ambalangoda": sun_ambalangoda,
        "Kosgoda": sun_kosgoda,
        "Aluthgama": sun_aluthgama,
        "Kaluthara South": sun_kaluthara_south,
        "Colombo Fort": sun_colombo_fort,
        "Maradana": sun_maradana
    }
}

#write data to a json file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
#connecting firebase
firebase = firebase.FirebaseApplication('https://ruhunukumari-237d4.firebaseio.com/', None)
# post data to firebase
result = firebase.post('',data)

print('Data has been uploaded to the firebase')
print(result)

# get data from firebase
result = firebase.get('', '')
print(result)

