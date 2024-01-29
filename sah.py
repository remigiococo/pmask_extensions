from math import pow, fabs, fmod, sin, cos, pi
import random
from pmask.generator import *

# Sample-And-Hold
class SAH(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph
        self.r = random.random()
        self.flag = 1

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        if (evaluationTime < 0.9*t):
            if (evaluationTime > 0) and (self.flag == 0):
                self.r = random.random()
                self.flag = 1
        else:
            self.flag = 0
        return self.r

class Randi(Generator):
    def __init__(self, T = 1.0, ph = 0.0):
        Generator.__init__(self)
        self.T = T
        self.ph = ph
        self.r0 = random.random()
        self.r1 = random.random()
        self.flag = 1

    def valueAt(self, evaluationTime):
        t = evaluateAt(self.T, evaluationTime)
        evaluationTime += t * self.ph
        evaluationTime = fmod(evaluationTime, t)
        if evaluationTime < 0:
            evaluationTime += t
        if (evaluationTime < 0.9*t):
            if (evaluationTime > 0) and (self.flag == 0):
                self.r0 = self.r1
                self.r1 = random.random()
                self.flag = 1
        else:
            self.flag = 0
        return (evaluationTime/t) * (self.r1 - self.r0) + self.r0
