side = int(input('enter the value of side'))

peri_sq = 4 * side
area_sq = side ** 2
area_cube = 6 * (side ** 2)
vol_cube = side ** 3

print("\nThe perimeter of square is : ", peri_sq,
      "\nThe area of square is : ", area_sq,
      "\nThe area of cube is : ", area_cube,
     "\nThe volume of cube is : ", vol_cube)

radius = int(input('enter the value of radius'))

peri_cir = 2 *(22/7) * radius
area_cir = (22/7) * (radius) ** 2
area_sph = 4 * (22/7) * (radius) ** 2
vol_sph = (4/3) * (22/7) * (radius) ** 3

print("\nThe perimeter of circle is : ", peri_cir,
      "\nThe area of circle is : ", area_cir,
      "\nThe area of sphere is : ", area_sph,
     "\nThe volume of sphere is : ", vol_sph)

area_cone = (22/7) * side * radius

print("\nThe area of cone is : ", area_cone)



