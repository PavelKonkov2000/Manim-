# Даны координаты трёх точек произвольного треугольника. Необходимо найти координаты трёх замечательных точек треугольника ABC по отдельности, а также провести замечательные прямые в треугольнике ABC

# Задаём координаты вершин треугольника ABC

point_A=[-1, 2, 0]
point_B=[-3, -3, 0]
point_C=[4, 1, 0]

#создаём класс Triangle_Points

class Triangle_Points:
  # создаём функцию определения центра тяжести треугольника
  def intersection_of_medians(point1, point2, point3):
    return()
  def points_for_medians(point1, point2, point3):
    return([(point2[0]+point3[0])/2, (point2[1]+point3[1])/2, (point2[2]+point3[2])/2],
              [(point1[0]+point3[0])/2, (point1[1]+point3[1])/2, (point1[2]+point3[2])/2],
              [(point2[0]+point1[0])/2, (point2[1]+point1[1])/2, (point2[2]+point1[2])/2])
