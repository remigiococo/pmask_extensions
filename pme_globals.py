#
# PME - PMask Extension
#

# PMASK standard imports
from pmask import Accumulator
from pmask.exception import *
from pmask import List
from pmask import Mask
from pmask import Sine, Cosine, SawUp, SawDown, PowerUp, PowerDown, Square, Triangle
from pmask import TET12
from pmask import Quantizer, Attractor
from pmask import Range
from pmask import UniformRandom, LinearRandom, InverseLinearRandom, TriangularRandom
from pmask import InverseTriangularRandom, ExponentialRandom, ReverseExponentialRandom
from pmask import BilateralExponentialRandom, GaussRandom, CauchyRandom, BetaRandom, WeibullRandom
from pmask.score import *
from pmask import LinearSegment, HalfCosineSegment, PowerSegment, NoInterpolationSegment

# PMASK extensions import
from ProbList import *
from WalkList import *
from sah import *


# utility functions
def save_score(nomefile, sz) :
	ff = file(nomefile, 'w+')
	ff.write(sz)
	ff.close()

# some global objects

# density
p2_rhy = Range(0.066, 0.07) # rhythm < 15 gr/sec
p2_flu = Range(0.04, 0.066) # fluttering 15-25 gr/sec
p2_cha = Range(0.02, 0.04) # chaos 25-50 gr/sec
p2_tex = Range(0.01, 0.02) # texture 50-100 gr/sec
p2_ban = Range(0.0025, 0.01) # band > 100 gr/sec (100-400)
	
# duration
p3_noi = Range(0.0002, 0.0005)	# 200 us noisy
								# 500 us
p3_unp = Range(0.0005, 0.001)	# 1 ms loss of pitch (unpitched)
p3_flu = Range(0.001, 0.01)		# 10 ms fluttering
p3_pit = Range(0.01, 0.05)		# 50 ms pitch formation
								# 100 ms
p3_tre = Range(0.1, 0.2)		# 200 ms tremolo, jittering

A_CAPO = "\n"
FINE_SEZIONE = "s\n"
