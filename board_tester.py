import point

def quick_populate(b, t1_pieces_notation_list, t2_pieces_notation_list):
  # Populates the board with t1 pieces
  for element in t1_pieces_notation_list:
    region_i, position = point.notation_to_coordinates(element)
    # p = point.Point(1, t1_pieces_notation_list, region_i, position)

    b.p1_make_move(region_i, position, 1)

  # Populates the board with t2 pieces
  for element in t2_pieces_notation_list:
    region_i, position = point.notation_to_coordinates(element)
    # p = point.Point(2, t1_pieces_notation_list, region_i, position)

    b.p1_make_move(region_i, position, 2)

  return b

def turn_to_notation(self, turn):
		o, m, r = turn
		if o is not None:
			o = o.notation
		if m is not None:
			m = m.notation
		if r is not None:
			r = r.notation
		return o, m, r 
    