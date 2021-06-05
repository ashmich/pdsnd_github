import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # use .lower() to ensure that user is able to input characters whether uppercase or lowercase 
    valid_cities = ('chicago','new york city', 'washington')
    wrong_city = True
    while wrong_city:
        city = input("Key in chicago, new york city or washington: ") 
        city = city.lower()
        if city in valid_cities:
            break  
        else:
            print('Incorrect city, please select either chicago, new york city, or washington')
            
                
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    right_month = True
    while right_month:
        month = input("Key in the selected months from january till june, or select all: ") 
        month = month.lower()
        if month in valid_months:
            break
        print('Invalid month. Please select from january till june or select all') 
        
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all')
    approve_day = True
    while approve_day:
        day = input("Key in the selected days from monday to sunday or select all: ")
        day = day.lower()
        if day in valid_days:
            break
        print('Invalid day. Please select only from monday to sunday or select all') 
    
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    # filter for city
    try:
        df = pd.read_csv(CITY_DATA[city])
    except:
        print("No such city data found.")
        return

    # filter for month
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Month"] = pd.DatetimeIndex(df["Start Time"]).month
    if month != "all":
        months_to_idx = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6}
        month_id = months_to_idx[month]
        
        df = df[df["Month"] == month_id]
    
    # filter for day
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["Day"] = pd.DatetimeIndex(df["Start Time"]).day
    if day != "all":
        days_to_idx = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}
        day_id = days_to_idx[day]
        df = df[df["Day"] == day_id] 
        
    return df    
 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    idx_to_months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    most_common_month_index = df["Month"].mode()[0]
    most_common_month = idx_to_months[most_common_month_index]
    print("The most common month is: ", most_common_month)

    # TO DO: display the most common day of week
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    day_of_week = df["Start Time"].dt.day_name().mode()[0]
    print("The most common day is: ", day_of_week) 
    
    # TO DO: display the most common start hour
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    hr = df["Start Time"].dt.hour.mode()[0]
    if hr > 12: 
        new_hour = hr - 12
        new_hour = str(new_hour) + "pm"
    else:
        new_hour = str(hr) + "am"
    print("The most common start hour is:", new_hour)

    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df["Start Station"].mode()[0]
    print("The most commonly used start station is: ", common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df["End Station"].mode()[0]
    print("The most commonly used end station is: ", common_end_station) 
    
    # TO DO: display most frequent combination of start station and end station trip
    station_most_common = df.groupby(["Start Station", "End Station"]).size().idxmax()
    station_frequency = df.groupby(["Start Station", "End Station"]).size().max()
    print(f"Most common stations are: '{station_most_common[0]}' and '{station_most_common[1]}', with a frequency of {station_frequency}") 
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df["Trip Duration"].sum() 
    print("The total travel time is:", "{:,}".format(total_travel_time))  


    # TO DO: display mean travel time
    mean_time = df["Trip Duration"].mean()
    print("The mean travel time is:", "{:.2f}".format(mean_time))
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_user_types = df['User Type'].value_counts()
    user_type_dict = count_of_user_types.to_dict()
    for key, value in user_type_dict.items():
        print(f'There are {value} for the user type {key}.') 
    
    
    # TO DO: Display counts of gender
    try:
        nan_values_in_gender = df["Gender"].isna().sum()
        print("The NaN values in gender are: ", "{:,0f}".format(nan_values_in_gender)) 

        male_fem = df["Gender"].value_counts()
        male_fem_dict = male_fem.to_dict()
        for key, value in male_fem_dict.items():
            print(f'There are {value} {key}.')
    except:
        print("There was an error loading the 'Gender' information from the data.")
        
        
    # TO DO: Display earliest, most recent, and most common year of birth
    
    try:
        earliest_birth = df["Birth Year"].min()
        print("The earliest year of birth is:","{:.0f}".format(earliest_birth)) 
        

        most_recent_birth = df["Birth Year"].max()
        print("The most recent birth is:","{:.0f}".format(most_recent_birth)) 

        common_birth_year = df["Birth Year"].mode()[0]
        print("The most common year of birth is:","{:.0f}".format(common_birth_year))
   
    except: 
        print("There was an error loading the 'Birth Year' information from the data.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

#prompts user if they want to see five lines of raw data

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()
        
              
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
