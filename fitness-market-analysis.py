# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

#load the data in each csv file to a dataframe
workout = pd.read_csv('data/workout.csv')
three_keywords = pd.read_csv('data/three_keywords.csv')
workout_geo = pd.read_csv('data/workout_geo.csv')
three_keywords_geo = pd.read_csv('data/three_keywords_geo.csv')

#extract month and year of workout
workout['month'] = pd.to_datetime(workout['month'])
workout['year'] = workout['month'].dt.year

#peak global search for 'workout'
year_str = str(workout.sort_values(by = 'workout_worldwide', ascending = False)['year'].iloc[0])
print('peak global search for workout: ', year_str)

#extract month and year of three key words
three_keywords['month'] = pd.to_datetime(three_keywords['month'])
three_keywords['year'] = three_keywords['month'].dt.year

#filter the covid year(2020) and the current year(2023)
covid_year = three_keywords[three_keywords['year'] == 2020]
current_year = three_keywords[three_keywords['year'] == 2023]

#most popular keywords during pandemic
peak_covid = str(covid_year[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].mean().idxmax())
print('most popular keywords during pandemic: ', peak_covid)

#most popular keywords in 2023
current = current_year[['home_workout_worldwide', 'gym_workout_worldwide', 'home_gym_worldwide']].idxmax(axis=1).iloc[0]
print('most popular keywords in 2023: ', current)

#country with the highest interest for workouts
top_country = workout_geo[workout_geo['country'].isin(['United States', 'Australia', 'Japan'])].set_index('country')['workout_2018_2023'].idxmax()
print('country with the highest interest for workouts: ', top_country)

#country with the highest home workouts interest
home_workout_geo = three_keywords_geo[
    three_keywords_geo['Country'].isin(['Philippines', 'Malaysia'])].set_index('Country')['home_workout_2018_2023'].idxmax()
print('country with the highest home workouts interest: ', home_workout_geo)

#figure 1
plt.figure(figsize=(12, 6))
plt.plot(workout["month"], workout["workout_worldwide"])
plt.xticks(rotation=90)
plt.title('Peak global workout search year')
plt.show()

#figure 2
plt.figure(figsize=(12, 6))
plt.plot(three_keywords["month"], three_keywords["home_workout_worldwide"], label="Home workout")
plt.plot(three_keywords["month"], three_keywords["gym_workout_worldwide"], label="Gym workout")
plt.plot(three_keywords["month"], three_keywords["home_gym_worldwide"], label="Home gym")
plt.xticks(rotation=90)
plt.legend()
plt.title("Comparison of Global Interest in Home and Gym Workout Keywords Over Time")
plt.show()


