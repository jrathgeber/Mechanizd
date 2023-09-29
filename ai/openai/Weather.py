# Import the weather2 package

# https://www.datacamp.com/tutorial/using-gpt-models-via-the-openai-api-in-python

import weather

# Get the forecast for Miami
location = "Miami"
forecast = weather.forecast(location)

# Pull out forecast data for midday tomorrow
fcast = forecast.tomorrow["12:00"]

# Create a prompt
user_msg_weather = f"In {location} at midday tomorrow, the temperature is forecast to be {fcast.temp}, the wind speed is forecast to be {fcast.wind.speed} m/s, and the amount of precipitation is forecast to be {fcast.precip}. Make a list of suitable leisure activities."

# Call GPT
response_activities = chat("You are a travel guide.", [user_msg_weather])

display(Markdown(response_activities))