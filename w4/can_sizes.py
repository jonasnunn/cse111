import math


def main():
    for i in range(12):
        r = radi[i]
        h = heights[i]
        cost = costs[i]
        se = storage_efficency(compute_volume(r,h), compute_surface_area(r,h))
        ce = compute_cost(cost, compute_volume(r,h))
        print(f'#{numbers[i]} {names[i]} {se:.2f} ${ce:.2f}')


def compute_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume


def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def storage_efficency(volumne, surface_area):
    effiecncy = volumne/surface_area
    return effiecncy

def compute_cost(cost,volume):
    ce = volume/cost
    return ce

numbers = [1,1,2,2.5,3,5,'6Z','8Z',10,211,300,303]
names = ['Picnic','Tall','','','Cylinder','','','Short','','','','']
radi = [6.83,7.78,8.73,10.32,10.79,13.02,5.40,6.83,15.72,6.83,7.62,8.10]
heights = [10.16,11.91,11.59,11.91,17.78,14.29,8.89,7.62,17.78,12.38,11.27,11.11]
costs = [.28,.43,.45,.61,.86,.83,.22,.26,1.53,.34,.38,.42]
main()