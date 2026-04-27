# Robot  Delivery Team  🤖
# You're responsible for preparing a fleet of autonomous delivery robots for a major city. Your program will:
# 1. Collect exactly 3 robot names and assign them one of three predefined delivery zones ("Downtown", "Suburbs", "Industrial").
# 2. Check the total distance to be covered (integer between 5 and 500 km).
# 3. Collect the weight of each robot’s cargo (must be between 1 and 50 kg).'
# 4 .Check if the weather conditions are safe ("Clear", "Rain", "Storm").
# 5. Determine if the fleet is ready for deployment.


# pseudocode:


# Make it store exactly 3 robot names and their assigned delivery zones ("Downtown", "Suburbs", "Industrial") in a dictionary.\

robots = {}
zones = ["Downtown", "Suburbs", "Industrial"]


for i in range(3):
    name = input("Enter robot name: ").strip().title()

    while True:
        zone = (
            input(
                f"Choose a delivery zone for {name} (Downtown, Suburbs, Industrial): "
            )
            .strip()
            .title()
        )

        if zone in zones:
            break
        print("Invalid zone. Choose from Downtown, Suburbs, or Industrial.")

    robots[name] = {"zone": zone}


# Gets the total delivery distance (integer 5-500 km).
while True:
    try:
        distance = int(input("Enter total delivery distance (5-500 km): "))
        if 5 <= distance <= 500:
            print(f"Distance Check: Within Range ({distance} km)")
            break
        else:
            print("Error: Distance must be between 5 and 500 km.")
    except ValueError:
        print("Error: Please enter a valid integer.")


# Gets the cargo weight for each robot (between 1 and 50 kg).
for robot_name in robots:
    while True:
        try:
            weight = int(input(f"Enter cargo weight for {robot_name} (1-50 kg): "))
            if 1 <= weight <= 50:
                robots[robot_name]["weight"] = weight
                break
            else:
                print("Error: Weight must be between 1 and 50 kg.")
        except ValueError:
            print("Error: Please enter a valid integer.")


# Gets the weather condition ("Clear", "Rain", "Storm").
valid_weather = ["Clear", "Rain", "Storm"]


while True:
    weather = input("Enter weather conditions (Clear, Rain, Storm): ").strip().title()
    if weather in valid_weather:
        if weather == "Storm":
            print("Weather Check: Unsafe")
        else:
            print("Weather Check: Safe")
        break
    else:
        print("Invalid weather condition.")


print()


# If distance is over 300 km, any robot carries more than 50 kg, or the weather is "Storm", print "🚨 Deployment Unsafe!".
unsafe = False


if distance > 300:
    unsafe = True


if weather == "Storm":
    unsafe = True


for robot in robots:
    if robots[robot]["weight"] > 50:
        unsafe = True


# Otherwise, print a summary of robot names, zones, and cargo weights with the message: "🤖 Robots Ready for Delivery!".
if unsafe:
    print("🚨 Deployment Unsafe!")
else:
    for robot, data in robots.items():
        print(f"{robot}: {data['zone']}, {data['weight']}kg")
    print("🤖Robots Ready for Delivery!")
