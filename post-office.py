'''
Auther Eaton Holden
Date 10/23/2025
bugs none
Sources Ms Marciano
'''

def zone(zipcode):
    if 1 <= zipcode and zipcode <= 6999:
        return 1
    elif zipcode >= 7000 and zipcode <= 19999:
        return 2
    elif zipcode >= 20000 and zipcode <= 35999:
        return 3
    elif zipcode >= 36000 and zipcode <= 62999:
        return 4
    elif zipcode >= 63000 and zipcode <= 84999:
        return 5
    elif zipcode >= 85000 and zipcode <= 99999:
        return 6
    else:
        return 'UNMAILABLE'

def find_distince(startzip, endzip):
    startzone = zone(startzip)
    endzone = zone(endzip)

    if startzone == 'UNMAILABLE' or endzone == 'UNMAILABLE':
        return 'UNMAILABLE'
    return abs(startzone - endzone)

def get_type(length,height,thickness):
    perimiter = length + 2*(height + thickness)

    if 3.5 <= length <= 4.25 and 3.5 <= height <= 6 and .007 <= thickness <= .016:
        return 'Regular Post Card'
    elif 4.25 <= length <= 6 and 6 <= height <= 11.5 and .007 <= thickness <= 0.15:
        return 'Large Post Card'
    elif 3.5 <= length <= 6.125 and 5 <= height <= 11.5 and 0.16 <= thickness <= .24:
        return 'Envelope'
    elif 6.125 <= length <= 24 and 11 <= height <= 18 and 0.25 <= thickness <= 0.5:
        return 'Large Envelope'
    elif length > 24 or height > 18 or thickness > .5 and perimiter <= 84:
        return 'Package'
    elif length > 24 or height > 18 or thickness > .5 and 84 < perimiter <= 130:
        return 'Large Package'
    else:
        return 'UNMAILABLE'
    
def find_cost(post_type, total_zones):    
    if post_type == 'Regular Post Card':
        return .20 + .03*total_zones
    elif post_type == 'Large Post Card':
        return .37 + .03* total_zones
    elif post_type == 'Envelope':
        return .37 + .04* total_zones
    elif post_type == 'Large Envelope':
        return .60 + .05* total_zones
    elif post_type == 'Package':
        return 2.95 + .25* total_zones
    elif post_type == 'Large Package':
        return 3.95 + .35* total_zones

def main():
    info = input('what is the length, height and thickness of your card and what zip code are you mailing from and to')
    length, height, thickness, startzip, endzip = info.split(',')
    length = float(length)
    height = float(height)
    thickness = float(thickness)
    startzip = int(startzip)
    endzip = int(endzip)
    post_type = get_type(length,height,thickness)
    total_zones = find_distince(startzip, endzip)
    cost = find_cost(post_type, total_zones)
    print(cost)
main()