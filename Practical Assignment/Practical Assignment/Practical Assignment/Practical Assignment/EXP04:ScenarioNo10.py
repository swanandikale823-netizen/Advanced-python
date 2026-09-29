import random


traffic = [random.randint(80, 200) for i in range(48)]

print("Traffic Data:", traffic)


day = traffic[:24]
night = traffic[24:]

print("Day Average:", sum(day) / 24)
print("Night Average:", sum(night) / 24)


window = 3
dp = []
s = sum(traffic[:window])
dp.append(s / window)

for i in range(window, 48):
    s = s + traffic[i] - traffic[i-window]
    dp.append(s / window)

print("Moving Average:", dp)

# Congestion hours
congestion = [x for x in traffic if x > 150]

print("Congestion Hours:", congestion)
