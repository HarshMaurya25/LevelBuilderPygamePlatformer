from block import Block
import csv

class Save:
    def __init__(self,level):
        self.world_data = Block(54)
        # self.world_data.give()
        self.data = self.world_data.world_seed

        with open(f'Assest/level/{level}.csv', 'w', newline='') as csvf:
                    writer = csv.writer(csvf,delimiter=',')
                    for row in self.data:
                         writer.writerow(row)
