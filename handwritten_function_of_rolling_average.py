import random as rn

rn.seed(3)

lista_to_mean = []

for a in range(10):
    b = rn.randint(1,150)
    lista_to_mean.append(b)

def walking_mean(x):
    num = 0
    caluclating_mean = []
    while num <= (len(lista_to_mean) - x):
        f_l = lista_to_mean[num:(num+x)]
        mean_calc = sum(f_l)/len(f_l)
        caluclating_mean.append(mean_calc)
        num += 1
        
    return caluclating_mean

print(lista_to_mean)
print("***********")
print(walking_mean(2))

