import os
import time
import numpy as np


class GameOfLife:
    def __init__(self, N, start_size, iterations_number):
        self.N = N
        self.iterations_number = iterations_number
        self.table = np.zeros((N,N), dtype=np.int8)

        index = round((N - start_size)/2)
        self.table[index:(index + start_size), index:(index + start_size)] = 1


    def evolution(self):
        for i in range(self.iterations_number):
            for i, row in enumerate(self.table):
                for j, element in enumerate(row):
                    if element == 0 and self.neighbors_counter((i,j)) == 3:
                        self.table[i,j] = 1
                    elif not (element == 1 and (2 <= self.neighbors_counter((i,j)) <= 3)):
                        self.table[i,j] = 0
            time.sleep(0.05)
            if os.name =="nt":
                os.system("cls")
            else:
                os.system("clear")
            self.print_state(".")
                        

    def print_state(self, symbol):
        print("_"*self.N*2)
        for row in self.table:
            print("|", end="")
            print(" ".join(list(map(lambda x: " " if x==0 else symbol, row))), end="")
            print("|")
        print("_"*self.N*2)


    def neighbors_counter(self, position):
        counter = self.table[position[0] - 1, position[1] - 1] + \
                  self.table[position[0] - 1, position[1]] + \
                  self.table[position[0] - 1, (position[1] + 1) % self.N]    

        counter += self.table[position[0], position[1] - 1] + self.table[position[0], (position[1] + 1) % self.N]

        counter += self.table[(position[0] + 1) % self.N, position[1] - 1] + \
                   self.table[(position[0] + 1) % self.N, position[1]] + \
                   self.table[(position[0] + 1) % self.N, (position[1] + 1) % self.N] 
        return counter

if __name__ == "__main__":
    game= GameOfLife(30, 9, 1000)
    game.evolution()