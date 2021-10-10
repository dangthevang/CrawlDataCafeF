import pandas as pd

class MergeData():
  
  def __init__(self, totalIndexTime):
    self.totalIndexTime = totalIndexTime

  def codeTimeToIndex(self, codeTime):
    s = codeTime.split("/")
    return self.totalIndexTime - ((int(s[0])-2008)*4+int(s[1]))

  def indexToCodeTime(self,index):
    return str(2008+index//4)+"/"+str(index%4+1)+"/0/0"

  def timeToCodeTimeBuy(self,time):
    s = [int(i) for i in time.split("/")]
    if s[1] == 2:
      return "y/q/0/0".replace("y",str(s[2]-1)).replace("q","4")
    return "y/q/0/0".replace("y",str(s[2])).replace("q",str(s[1]//3))
  
  def timeToCodeTimeSale(self,time):
    s = [int(i) for i in time.split("/")]
    y = s[2]
    if s[1] == 2:
      y -= 1
    time = "01/m/y".replace("m",str((s[1]+9)%12)).replace("y",str(y))
    return self.timeToCodeTimeBuy(time)
  

# m = MergeData(54)

# print(m.timeToCodeTimeSale("02/02/2023"))
