n = int(input())
waiting_room = input().split()

if n == 1:
    suffix = 'st'
elif n == 2:
    suffix = 'nd'
elif n == 3:
    suffix = 'rd'
else:
    suffix = 'th'

print(f"The {n}{suffix} client is {waiting_room[n - 1]}.")