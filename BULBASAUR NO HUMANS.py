import matplotlib.pyplot as plt
import random

plt.xlabel("ticks")
plt.ylabel("population")
plt.title("1 Female to 7 Males")
def sim(male, female):
  #"Rendering"
  MalePop = male*2
  FemalePop = female*2
  tick = 0
  eggs = [0]*21
  
  
  x=[]
  yAll = []
  yMales = []
  yFemales = []
  
  while tick < 300:
      x.append(tick)
      yAll.append(MalePop+FemalePop)
      yMales.append(MalePop)
      yFemales.append(FemalePop)
  
      tick += 1
      print(f"tick: {tick}\n{yAll[-1]}")
      #The Death Chamber TM
      for i in range(MalePop):
          isDeath = random.randint(1, 10000) <= 243
          if isDeath:
              MalePop -= 1
      for i in range(FemalePop):
          isDeath = random.randint(1, 10000) <= 243
          if isDeath:
              FemalePop -= 1
      if eggs[0] > 0:
          for i in range(eggs[0]):
              genderroll = random.randint(1, female+male)
              if genderroll >= female:
                  FemalePop += 1
              else:
                  MalePop += 1
      eggs.pop(0)
      eggs.append(0)
  
      #Reproduction
      if MalePop>=1:
          for i in range(FemalePop):
              isEgg = random.randint(1, 10) <= 5
              if isEgg:
                  eggs[-1] += 1
      elif FemalePop>=1:
          for i in range(FemalePop):
              isEgg = random.randint(1, 10) <= 1
              if isEgg:
                  eggs[-1] += 1
      
      #exit point
      if FemalePop+MalePop + sum(eggs) == 0:
          print("Extinction")
          break
  
  print(f"all: {FemalePop+MalePop}\nmale: {MalePop}\nfemale: {FemalePop}\nRatio: {male}:{female}")
  return yAll
x = []
for i in range(1,301):
  x.append(i) 
eighthFemales = sim(7, 1)

forthFemales = sim(6, 2)

halfHalf = sim(4, 4)

forthMales =sim(2, 6)

EighthMales = sim(1, 7)



plt.plot(x, EighthMales, label = "1:7")
plt.plot(x, forthMales, label = "2:6")
plt.plot(x, halfHalf, label = "4:4")
plt.plot(x, forthFemales, label = "6:2")
plt.plot(x, eighthFemales, label = "7:1")
plt.legend()
plt.show()
print("done")
print("no, really")