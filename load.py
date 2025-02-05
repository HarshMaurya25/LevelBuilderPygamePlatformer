from block import Block
import csv

class Load:
    def __init__(self,level):
        world_data= 0
        with open(f'Assest/level/{level}.csv', newline='') as csvf:
              reader= csv.reader(csvf,delimiter=',')
              for x , row in enumerate (reader):
                     for y , tile in enumerate(row):
                            # world_data[x][y]= int(tile)
                            pass

        block = Block(54)
        block.load(world_data)
                                  