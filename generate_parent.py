import numpy as np
import copy
import heapq_max

mesin1 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 7, 12, 13] #buat ngetes generate aja
mesin2 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7]

parent = []
parent2 = []
unique = set(mesin2)
total_Mwatt = 0
# point = {1:20, 2:15, 3:35, 4:40, 5:15, 6:15, 7:10}
point = {}
for i in unique:
    point[i] = int(input("masukkan listrik dalam generator " + str(i) + ": "))
    total_Mwatt+=point[i]

minimum_Mwatt = int(input("masukkan jumlah minimum listrik yang di butuhkan : "))
max_Mwatt_off = total_Mwatt-minimum_Mwatt

#generate chromosome ultimate super mega no limit terserah panjang brp
def generate_parent(mesin):
    mesinpt2 = copy.deepcopy(mesin)
    first_half = []
    second_half = []
    counter = 0
    while len(mesin) != 0:
        gen = int(np.random.choice(mesin, size=1))
        if counter>=6:
            infinite_loop_handling = 0
            while gen in first_half[counter%6]:
                gen = int(np.random.choice(mesin, size=1))
                infinite_loop_handling+=1
                if infinite_loop_handling > 5:
                    counter+=1
            first_half[counter%6].append(gen)

        else :
            first_half.append([gen])
        mesin.remove(gen)
        counter = counter + 1

    counter = 0
    while len(mesinpt2) != 0:
        gen = int(np.random.choice(mesinpt2, size=1))
        if counter >= 6:
            infinite_loop_handling = 0
            while gen in second_half[counter%6]:
                gen = int(np.random.choice(mesinpt2, size=1))
                infinite_loop_handling+=1
                if infinite_loop_handling > 5:
                    counter+=1
            second_half[counter%6].append(gen)

        else :
            second_half.append([gen])
        mesinpt2.remove(gen)
        counter = counter + 1

    first_half = first_half + second_half

    return first_half

def count_fitness_point(chromosome,point,max_Mwatt_off):
    fitness_point = 0
    for i in chromosome:
        child_fitness_point = 0
        for j in i:
            child_fitness_point+=point[j]
        if child_fitness_point > max_Mwatt_off:
            fitness_point+=(child_fitness_point-max_Mwatt_off)
    return fitness_point

def crossover(parent1,parent2):
    copy_parent1 = copy.deepcopy(parent1)
    copy_parent2 = copy.deepcopy(parent2)
    c1 = copy_parent1[0:6]+copy_parent2[6:12]
    c2 = copy_parent2[0:6]+copy_parent1[6:12]
    return c1,c2
# parent = generate_parent(mesin1)
# print(parent)

def mutation(chromosome):
    chromosome_pt1 = copy.deepcopy(chromosome[0:6])
    chromosome_pt2 = copy.deepcopy(chromosome[6:12])
    maxLength = max(map(len, chromosome))
    temp = []
    counter = 0
    for i in chromosome_pt1:
        if len(i) == maxLength:
            temp.append(i.pop())
    while temp:
        gen = int(np.random.choice(temp, size=1))
        infinite_loop_handling = 0
        while gen in chromosome_pt1[counter%6]:
            gen = int(np.random.choice(temp, size=1))
            infinite_loop_handling += 1
            if infinite_loop_handling > 5:
                counter += 1
        chromosome_pt1[counter % 6].append(gen)
        counter+=1
        temp.remove(gen)

    counter = 0

    for i in chromosome_pt2:
        if len(i) == maxLength:
            temp.append(i.pop())
    while temp:
        gen = int(np.random.choice(temp, size=1))
        infinite_loop_handling = 0
        while gen in chromosome_pt2[counter % 6]:
            gen = int(np.random.choice(temp, size=1))
            infinite_loop_handling += 1
            if infinite_loop_handling > 5:
                counter += 1
        chromosome_pt2[counter % 6].append(gen)
        counter += 1
        temp.remove(gen)

    chromosome_pt1 = chromosome_pt1 + chromosome_pt2
    return chromosome_pt1

class population:
    def __init__(self):
        self.heap = []
        heapq_max.heapify_max(self.heap)

    def add(self,fitness_point,chromosome):
        data = (fitness_point,chromosome)
        heapq_max.heappush_max(self.heap,data)
    def kick(self):
        value = heapq_max.heappop_max(self.heap)
        return value


pop =population()
for i in range(100):
    mesin2_pt2 = copy.deepcopy(mesin2)
    parent = generate_parent(mesin2_pt2)
    if parent not in pop.heap:
        pop.add(count_fitness_point(parent,point,max_Mwatt_off),parent)
        print(parent)
        print(count_fitness_point(parent,point,max_Mwatt_off))

print(pop.kick())

# parent2 = generate_parent(mesin2_pt2)
# print(parent2)
# print(count_fitness_point(parent2,point,max_Mwatt_off))
#
# c1,c2 = crossover(parent,parent2)
# print(c1)
# print(c2)

