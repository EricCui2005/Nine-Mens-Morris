class Point:
    def __init__(self, occupied, notation, region, position):
        # 0 is unoccupied, 1 is occupied by white, 2 is occupied by black
        self.occupied = occupied
        # Chess-esque point-notating scheme with key (square [0 - 2])(position[0 - 7])
        self.notation = notation
        # Describes the "square" the point is located on (0 - 2)
        self.region = region
        # Describes the position on the square the point is located
        self.position = position

    # Returns a printable representation of the piece to be plaed on the board
    def __str__ (self):
        if self.occupied == 1:
          return "\x1b[1;34;40m" + "@" + "\x1b[0m"
        elif self.occupied == 2:
          return "\x1b[1;31;40m" + "@" + "\x1b[0m"
        return "o"

    # Exception handling function  
    def __repr__(self):
        if self.occupied == 1:
          return "\x1b[1;34;40m" + "@" + "\x1b[0m"
        elif self.occupied == 2:
          return "\x1b[1;31;40m" + "@" + "\x1b[0m"
        return "o"
          

# Check if two points are on the same team
def same_team(p1:Point, p2:Point):
      return p1.occupied == p2.occupied and p1.occupied

def opposing_team(team_num):
  # 1 % 1 + 1 = 2 (team 1)
  # 2 % 2 + 1 = 1 (team 2)
  return (team_num % 2) + 1

# Map the region character into a region index
region_map = {"o" : 0, "m": 1, "i": 2}
def notation_to_coordinates(notation):
  region, position = notation
  region_i = region_map[region]
  position_i = int(position)
  return region_i, position_i

region_i_map = {0: "o", 1: "m", 2: "i"}


def coordinates_to_notation(region_i, position):
  return region_i_map[region_i] + str(position)
  