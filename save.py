from block import Block
import csv
import pickle

class Save:
    def __init__(self,level):
        self.world_data = Block(54)
        self.data = self.world_data.world_data

        with open(f'Assest/level/{level}.csv', 'w', newline='') as csvf:
                    writer = csv.writer(csvf,delimiter=',')
                    for row in self.data:
                         writer.writerow(row)

        # pickle_out = open(f'Assest/level/{level}.csv','wb')
        # pickle.dump(self.world_data,pickle_out)
        # pickle_out.close()