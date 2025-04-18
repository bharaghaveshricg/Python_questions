temperature = int(input())

if temperature < 0:

    print("Freezing weather")

elif 0 <= temperature < 10:

    print("Very cold weather")

elif 10 <= temperature < 20:

    print("Cold weather")

elif 20 <= temperature < 30:

    print("Normal in temperature")

elif 30 <= temperature < 40:

    print("It's hot")

elif temperature >= 40:

    print("It's very hot")
