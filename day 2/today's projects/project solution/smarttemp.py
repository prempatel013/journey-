print("\n" + "="*50 + "\n🌡️ SMART TEMPERATURE ADVISOR\n" + "="*50)

while True:
    try:
        temp = float(input("Enter current temperature (°C): "))
        
        if temp > 40:
            advice = "🚨 Heat warning! Stay indoors."
        elif 30 < temp <= 40:
            advice = "🔥 Hot! Drink plenty of water."
        elif 20 <= temp <= 30:
            advice = "😊 Perfect weather for a walk."
        elif 10 <= temp < 20:
            advice = "🧥 Slightly cool. Wear a light jacket."
        else:
            advice = "❄️ Cold! Bundle up."
        
        print(advice)
        break  # Exit after valid input
        
    except ValueError:
        print("⚠️ Please enter a valid number (e.g., 25.5)")

# Add-ons to try later:
# 1. Add humidity input for more accurate advice
# 2. Convert to Fahrenheit option