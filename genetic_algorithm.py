import random
import numpy as np
import copy
import heapq_max


#generate chromosome ultimate super mega no limit terserah panjang brp
#fungsi generate parent untuk genetic algorithm
def generate_parent(mesin):
    jmlh_maintenance = len(mesin)
    mesinpt2 = copy.deepcopy(mesin)
    first_half = []
    second_half = []
    counter = 0
    bool = True
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

        # jika jumlah total perbaikan mesin adalah <6 maka terdapat bulan tanpa perbaikan mesin
        else :
            if jmlh_maintenance<6:
                if bool:
                    bool = False
                    for i in range(6-jmlh_maintenance):
                        first_half.append([])
            first_half.append([gen])
        mesin.remove(gen)
        counter = counter + 1


    bool = True


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
            if jmlh_maintenance < 6:
                if bool:
                    bool = False
                    for i in range(6 - jmlh_maintenance):
                        second_half.append([])
            second_half.append([gen])
        mesinpt2.remove(gen)
        counter = counter + 1


    first_half = first_half + second_half


    return first_half

#fungsi untuk menghitung fitness poin
def count_fitness_point(chromosome,point,max_Mwatt_off):
    fitness_point = 0
    for i in chromosome:
        child_fitness_point = 0
        for j in i:
            child_fitness_point+=point[j]
        if child_fitness_point > max_Mwatt_off:
            fitness_point+=(child_fitness_point-max_Mwatt_off)
    return fitness_point


# fungsi untuk melakukan crossover dengan pembagian crossover 50% (50:50)
def crossover(parent1,parent2):
    copy_parent1 = copy.deepcopy(parent1)
    copy_parent2 = copy.deepcopy(parent2)
    c1 = copy_parent1[0:6]+copy_parent2[6:12]
    c2 = copy_parent2[0:6]+copy_parent1[6:12]
    return c1,c2


# gajadi pake
# def mutation_rate(chromosome):
#     mutation_rate = 0.2
#     random_value = random.random()
#     if random_value <= mutation_rate:
#         mutation(chromosome)
#     if random_value > mutation_rate:
#         return chromosome


# fungsi untuk melakukan mutasi chromosome
def mutation(chromosome):
    chromosome_pt1 = copy.deepcopy(chromosome[0:6])
    chromosome_pt2 = copy.deepcopy(chromosome[6:12])
    maxLength = max(map(len, chromosome))
    temp = []
    counter = 0
    mutation_rate = 0.2
    random_value = random.random()
    if random_value <= mutation_rate:
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


# populasi digunakan untuk menyimpan chromosome yang ada
class population:
    def __init__(self):
        self.heap = []
        heapq_max.heapify_max(self.heap)


    def add(self,fitness_point,chromosome):
        data = (fitness_point,chromosome)
        if data not in self.heap:
            heapq_max.heappush_max(self.heap,data)
    def kick(self):
        value = heapq_max.heappop_max(self.heap)
        return value


    # def peek_fit(self):
    #     val = heapq_max.heappop_max(self.heap)
    #     heapq_max.heappush_max(self.heap,val)
    #     return val[0]


# fungsi seleksi dengan metode roulette
def roulette_wheel_selection(pop):
    total_fitness = 0
    for i in pop.heap:
        total_fitness+=i[0]


    r = random.randint(0,total_fitness)


    cumulative_fitness = 0
    for i in pop.heap:
        cumulative_fitness += i[0]
        if r <= cumulative_fitness:
            pop.heap.remove(i)
            return i

# fungsi untuk menghitung jumlah listrik total dari generator
def hitung_total():
    global  total_watt
    for i in jumlah_watt:
        total_watt+=i

# variable
jumlah = 0
min_maintenance = []
min_watt = 0
jumlah_watt = []
hasil_iterasi = []
total_watt=0

# driver code
def main():
    mesin2=[]
    jumlah_mesin = jumlah
    print("\n")
    print(jumlah)
    print("\n")
    jumlah_maintenance = min_maintenance
    # jumlah_mesin=int(input("Masukan Jumlah Mesin : "))
    for i in range (jumlah_mesin):
        # jumlah_maintenance=int(input("masukkan Berapa kali mesin  " + str(i+1) + " diperbaiki : "))
        for j in range (jumlah_maintenance[i]):
             mesin2.append(i+1)


    print(mesin2)
    # mesin1 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 7, 12, 13]  # buat ngetes generate aja
    # mesin2 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7]


    parent = []
    parent2 = []
    unique = set(mesin2)
    total_Mwatt = 0

    # point = {1:20, 2:15, 3:35, 4:40, 5:15, 6:15, 7:10}
    point = {}
    for i in unique:
        # point[i] = int(input("masukkan listrik dalam generator " + str(i) + ": "))
        point[i] = jumlah_watt[i-1]
        total_Mwatt += point[i]


    print("Total Listrik yang dapat dihasilkan : %d"%total_Mwatt)
    minimum_Mwatt =  min_watt
    # minimum_Mwatt = int(input("masukkan jumlah minimum listrik yang di butuhkan : "))
    check = False
    if minimum_Mwatt >= total_Mwatt:
        while check == False:
            print("Jumlah Listrik minimum melibihi total jumlah listrik")
            # minimum_Mwatt = int(input("masukkan jumlah minimum listrik yang di butuhkan : "))
            if minimum_Mwatt >= total_Mwatt:
                continue
            else:
                check = True


    max_Mwatt_off = total_Mwatt - minimum_Mwatt


    print("Listrik Maksimal Mati: %d"%max_Mwatt_off)


    pop = population()
    for i in range(10):
        mesin2_pt2 = copy.deepcopy(mesin2)
        parent = generate_parent(mesin2_pt2)
        if (count_fitness_point(parent,point,max_Mwatt_off),parent) not in pop.heap:
            pop.add(count_fitness_point(parent,point,max_Mwatt_off),parent)
            # print(parent)
            # print(count_fitness_point(parent,point,max_Mwatt_off))


    print("populasi awal")
    for i in pop.heap:
        print(i)


    for i in range(len(unique)*10):
        parent1 = roulette_wheel_selection(pop)
        parent2 = roulette_wheel_selection(pop)
        pop.add(parent1[0],parent1[1])
        pop.add(parent2[0], parent2[1])
        # while parent1 == parent2:
        #     parent1 = roulette_wheel_selection(pop)
        #     parent2 = roulette_wheel_selection(pop)
        c1,c2 = crossover(parent1[1],parent2[1])
        c1 = mutation(c1)
        c2 = mutation(c2)
        pop.add(count_fitness_point(c1,point,max_Mwatt_off),c1)
        pop.add(count_fitness_point(c2,point,max_Mwatt_off),c2)
        while len(pop.heap) > 10:
            pop.kick()
        print("\niterasi ke ",i)
        tmp_iterasi = []
        for j in pop.heap:
            tmp_iterasi.append(j)
            print(j)
        hasil_iterasi.append(tmp_iterasi)

    print("\nhasil akhir")

    while pop.heap:
        val = pop.kick()
        if val[0] == 0:
            print(val)
    # mesin2_pt2 = copy.deepcopy(mesin2)
    # parent2 = generate_parent(mesin2_pt2)
    # print(parent2)
    # print(count_fitness_point(parent2,point,max_Mwatt_off))
    #
    # c1,c2 = crossover(parent,parent2)
    #
    # print(c1)
    # print(c2)
