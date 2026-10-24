import json
A='''a_station 1 but 1 aanaa
a_exactly 1 exactly 1 sariyaa
a_five 1 five 1 anju
a_seven 1 seven 1 ezhu
a_how 2 how 2 epdi
a_counter 3 counter 3 counter
a_conveyor 4 conveyor 4 conveyor
a_box 4 box 4 box
a_sensor 4 sensor 4 sensor
a_assume 5 assume 5 correct
a_off 6 off 6 off
a_b1 6 arrives 6 vandhaa
a_off2 6 past 6 kadandhu
a_b2 7 next 7 on
a_events 7 events 8 count
a_first 8 first 9 mudhal
a_second 9 second 10 rendaavadhu
a_b3 10 three 11 moonu
a_adds 11 adds 12 adhigarikkum
a_ctu 12 ctu 13 ctu
a_brands 12 brands 13 brand
a_two_values 13 two 14 rendu
a_preset 14 preset 15 preset
a_six 14 six 15 aaru
a_acc 15 accumulated 16 accumulated
a_accl 15 acc 16 acc
a_two_ex 16 after 17 rendu
a_done_def 17 done 18 done
a_question 18 question 19 question
a_hold 19 stops 20 ninnuduchunu
a_twosec 19 two 20 rendu
a_overover 20 over 21 thirumba
a_shouldnot 21 should 22 pannakoodaadhu
a_edge 22 rising 23 rising
a_stay 23 staying 24 appadiye
a_onecount 24 one 25 onnu
a_resume 24 off 25 off
a_b5 24 again 25 marubadi
b_follow 25 follow 26 full
b_empty 26 empty 27 empty
b_zero 26 zero 27 zero
b_start 26 start 27 start
b_runbit 27 packing 28 packing
b_conv 27 conveyor 28 conveyor
b_hold 27 holding 29 holding
b_b1 28 reaches 30 input
b_cnt1 28 becomes 30 count
b_clear 29 clears 31 kadandha
b_stays 29 stays 31 appadiye
b_b2 30 new 32 pudhusaa
b_b3 31 three 33 moonu
b_b4 31 four 33 naalu
b_b5 31 five 33 anju
b_still 32 still 34 odudhu
b_b6 33 detected 35 detect
b_doneon 33 done 35 done
b_runoff 34 packing 36 packing
b_notmotor 35 disconnect 37 motor
b_beyond 36 beyond 38 mela
b_more 37 more 39 valid
b_dist 38 stopping 40 .1
b_seventh 38 seventh 40 .45
b_spacing 39 spacing 41 spacing
b_complete 40 contains 42 irukku
b_q_start 41 should 43 marubadi
b_blocked 42 blocks 44 .55
b_remove 43 removes 45 eduthuttu
b_reset 44 reset 46 reset
b_zero2 45 zero 47 zero
b_nostart 46 must 48 koodaadhu
b_fresh 47 start 49 start
c_situation 48 different 50 innoru
c_stop 49 stop 51 stop
c_stays 50 three 52 moonu
c_retain 50 retains 52 retain
c_same 51 same 53 moonu
c_start 51 start 53 start
c_b4 51 four 53 naalu
c_b5 52 five 53 anju
c_b6 52 six 53 aaru
c_three_more 53 three 54 moonu
c_jobs 54 stop 55 stop
c_stopdef 55 interrupts 56 niruthuradhu
c_resetdef 55 clears 56 clear
c_whatif 56 resets 57 zero
c_nine 57 nine 58 onbadhu
c_agree 58 agree 59 match
c_batch 58 batch 59 batch
d_sensor 59 sensor 60 sensor
d_false 60 false 60 false
d_touch 60 touching 60 gap
d_missed 60 missed 60 pogalaam
d_reliable 61 reliable 61 signal
d_timer 62 measures 62 timer
d_counter 62 counts 62 events
e_ctu 63 ctu 63 ctu
e_byone 63 one 63 adhigarichadhu
e_other 64 other 64 concepts
e_ctd 65 ctd 65 ctd
e_six 66 six 66 aaru
e_five 66 five 66 anju
e_four 66 four 66 naalu
e_zero 66 zero 66 zero
e_ctud 67 ctud 67 ctud
e_in 68 adds 68 plus
e_out 68 subtracts 68 minus
e_match 68 matches 68 match
e_hsc 69 hsc 69 hsc
e_encoder 70 encoder 70 .03
e_hw 70 hardware 70 .72
e_class 71 classification 71 difference
e_dir 71 direction 71 direction
e_cap 71 ability 71 capability
e_updown 72 up 72 up
e_notfour 72 four 72 naalu
e_back 73 ctu 73 ctu
f_q 74 question 74 question
f_scen 75 packing 75 six
f_three 75 three 75 moonu
f_stop 75 stop 75 stop
f_noreset 75 reset 75 reset
f_start 75 start 75 start
f_how 76 how 76 ethana
f_A 77 option 77 option
f_B 78 option 78 option
f_C 79 option 79 option
f_comment 80 comment 80 comment
g_stop 81 stop 81 stop
g_missing 81 missing 81 illa
g_startq 81 start 81 start
g_next 82 interlocks 82 interlock
g_sub 83 subscribe 83 subscribe'''
def load(key):
    W=json.load(open(key+'.wordtimes.json'));P=json.load(open(key+'.paras.json'))
    return W,P
out={}
for li,key in [(0,'en_long'),(1,'ta_long')]:
    W,P=load(key);res={};miss=[]
    for line in A.split('\n'):
        f=line.split();name=f[0];para=int(f[1+2*li]);tok=f[2+2*li]
        try: fr=float(tok);res[name]=round(P[para][0]+(P[para][1]-P[para][0])*fr,2);continue
        except: pass
        c=[w for w in W if w[3]==para and w[0].startswith(tok)]
        if not c: miss.append((name,para,tok));res[name]=round(P[para][0],2);continue
        res[name]=round(c[0][1],2)
    # speech windows: merge words with gap<.3
    sp=[];
    for w,a,b,p in sorted(W,key=lambda x:x[1]):
        if sp and a-sp[-1][1]<.3: sp[-1][1]=b
        else: sp.append([a,b])
    for i,(s,e,t,*r) in enumerate(P):
        if not any(w[3]==i for w in W): sp.append([s,e])
    sp.sort()
    paras=[[round(p[0],2),round(p[1],2)] for p in P]
    out[key]={'A':res,'speak':[[round(a,2),round(b,2)] for a,b in sp],'P':paras}
    print(key,'missing',miss)
json.dump(out,open('ep6data.json','w'))
