level_one = [
    "0000000000ı000000ı0000",
    "0.....................",
    "0.....................",
    "0..................000",
    "x............000.....0",
    "0....................0",
    "0....................0",
    "0......000000000000000",
    "0....................0",
    "x  ....0.....X0x.....0",
    "00ı000ı000ı000ı000...0",
    ".....................0",
    "P....................0",
    "0000I000I000I000I00000",
]

FPS = 60

SIZE = 48

WIDTH = len(level_one[0]) * SIZE
HEIGHT = len(level_one) * SIZE

laser_direction = {'ı':0,'x':1,'I':2,'X':3}

level_two = [
    "000000000000ııııııııı0",
    "0....................0",
    "0....................0",
    "x.........00.........0",
    "0.......0000.........0",
    "0.........00.........0",
    "0.........00.........0",
    "000.......00.........0",
    "0.........00.........0",
    "x.........00.........0",
    "0.......0000.........0",
    "..........00......... ",
    "P.........00......... ",
    "0000000000000000000000",
]

level_three = [
    "000000ı0000000000ı0000",
    "0.....................",
    "0.....................",
    "0..............0000..0",
    "0......0..00.........0",
    "0.00......Xx.........0",
    "0.........00.........0",
    "0....................0",
    "0.....00.............0",
    "0...............00...0",
    "0....................0",
    "..........00.........0",
    "P....................0",
    "0000000000000000000000",
]

level_four = [
    "0ıııııııııııııııııııı0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    "0....................0",
    ".........0000........ ",
    "P.................... ",
    "0000000000000000000000",
]

level_five = [
    "00000ı0ı0ı0ı0ı0ı0ı0ı00",
    "0.....................",
    "0.....................",
    "0....................0",
    "0.................0..0",
    "0....................0",
    "0...000000000000000000",
    "0....................0",
    "00...................0",
    "00...................0",
    "000000IIII0IIII00....0",
    "....................00",
    "P..0x....00....X0...00",
    "0000000000000000000000",
]

level_one_updated = [
    "00000ı0ı0ı0ı0ı0ı0ı0ı00",
    "0.....................",
    "0.....................",
    "0....................0",
    "0.................0..0",
    "0.................0..0",  
    "0...000000000000000000",
    "0.................ı..0", 
    "00...................0",
    "00...................0",
    "000000IIII0IIII00....0",
    "...............I....00", 
    "P..0x....00....X0...00",
    "0000000000000000000000",
]
level_dic = {1:level_one,2:level_two,3:level_three,4:level_four,5:level_five}
