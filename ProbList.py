import random
from pmask.exception import *
from pmask.generator import *

class ProbList(Generator):
    def __init__(self, list, listp):
        Generator.__init__(self)
        if len(list) == 0:
            raise TooFewElements
        if len(list) != len(listp) :
            raise BadArgument
        self.list = list
        self.listp = listp

    def valueAt(self, evaluationTime):
        r = random.random()
        ndx = -1
        sum = 0.0
        prevsum = 0.0
        for i in range(len(self.listp)) :
            sum += self.listp[i]
            if ( (r < sum) and (r >= prevsum) ) :
                ndx = i
                break
            prevsum = sum
        if( ndx == -1 ):
            raise BadArgument
        return self.list[ndx]


class ProbListList(Generator):
    def __init__(self, list, listp):
        Generator.__init__(self)
        if len(list) == 0:
            raise TooFewElements
        if len(list) != len(listp) :
            raise BadArgument
        self.list = list
        self.listp = listp
        self.ndx = -1
        self.subindex = -1

    def valueAt(self, evaluationTime):
        if( self.subindex == -1 ):
            r = random.random()
            self.ndx = -1
            sum = 0.0
            prevsum = 0.0
            for i in range(len(self.listp)) :
                sum += self.listp[i]
                if ( (r < sum) and (r >= prevsum) ) :
                    self.ndx = i
                    break
                prevsum = sum
            if( self.ndx == -1 ):
                raise BadArgument
            self.subindex = 0
        else:
            self.subindex = self.subindex + 1
        item = self.list[self.ndx][self.subindex]
        if( self.subindex == (len(self.list[self.ndx])-1) ):
            self.subindex = -1 # pronto per ri-estrarre la lista successiva
        return item
