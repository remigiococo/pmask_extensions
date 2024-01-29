#
# imports
#
import random
from pmask import List, Range, ScoreSection, LinearSegment
from pmask import Attractor, Mask, ExponentialRandom
from pmask.pitch import *
from pmask.score import *
from ProbList import *
from sah import *

def save_score(nomefile, sz) :
	ff = file(nomefile, 'w')
	ff.write(sz)
	ff.close()
	
# density
p2_rhy = Range(0.066, 0.07) # rhythm < 15 gr/sec
p2_flu = Range(0.04, 0.066) # fluttering 15-25 gr/sec
p2_cha = Range(0.02, 0.04) # chaos 25-50 gr/sec
p2_tex = Range(0.01, 0.02) # texture 50-100 gr/sec
p2_ban = Range(0.0025, 0.01) # band > 100 gr/sec (100-400)
	
# duration
p3_noi = Range(0.0002, 0.0005)							# 200 us noisy
																						# 500 us
p3_unp = Range(0.0005, 0.001)								# 1 ms loss of pitch (unpitched)
p3_flu = Range(0.001, 0.01)									# 10 ms fluttering
p3_pit = Range(0.01, 0.05)									# 50 ms pitch formation
																						# 100 ms
p3_tre = Range(0.1, 0.2)										# 200 ms tremolo, jittering

