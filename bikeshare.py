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
    while True:
      city = input("\n choose a city to filter by from (new york city, chicago or washington):\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print(" you need to write the city correct.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month = input("\nchoose a month to filter by from (january, february, march, april, may, june) or type 'all' if you do not want a prticular month:\n").lower()           
      if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print("Sorry, but you have to write one of the chooses right.")
        continue
      else:
        break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("\nchoose a day to filter by from(sunday, monday, tuesday, wednesday, thursday, friday, saturday) or type 'all' if you do not want a particular day. :\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("Sorry, but you have to write one of the chooses right.")
        continue
      else:
        break

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

     
    df = pd.read_csv(CITY_DATA[city])

   
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    
    if month != 'all':
   
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

   
        df = df[df['month'] == month]

       
    if day != 'all':
       
        df = df[df['day_of_week'] == day.title()]

    return df





def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('the most common month is:', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most common day is:', popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common hour is:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('the most commonly used start station is:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nthe most commonly used end station is:', End_Station)
    
    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count.idmax()[0]
    print('\nthe most frequent used combination of start station and end station trip is:', Start_Station, " and ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = sum(df['Trip Duration'])
    print('the total travel time is:', total_travel_time/86400, " days")

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('the mean travel time is:', mean_travel_time/60, " minutes")


    print("\nthis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print('\ngender types:\n', gender_types)
    except KeyError:
      print("\ngender types:\nNo data available for this.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      earliest_year = df['Birth Year'].min()
      print('\nearliest year:', earliest_year)
    except KeyError:
      print("\nearliest year:\nNo data available for this.")

    try:
      most_recent_year = df['Birth Year'].max()
      print('\nmost recent year:', most_recent_year)
    except KeyError:
      print("\nmost recent year:\nNo data available for this.")

    try:
      most_common_year = df['Birth Year'].value_counts().idxmax()
      print('\nmost common year:', most_common_year)
    except KeyError:
      print("\nmost common year:\nNo data available for this.")

    print("\nthis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    keep_asking = True
    while (keep_asking):
       print(df.iloc[start_loc:start_loc + 5])
       start_loc += 5
       view_display = input("Do you wish to continue? enter yes or no: ").lower()
       if view_display == "no": 
           keep_asking = False

 

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
        restart = input('\nWould you like to restart the programe? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
