import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


cities = {'ch': 'chicago',
          'ny': 'new york city',
          'wsh': 'washington'}

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'monday', 'tuesday',
        'wednesday', 'friday', 'saturday', 'sunday']


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

    city = ""
    month = ""
    day = ""

    while city.lower() not in cities.keys():
        print("Please choose a city.")
        for key, value in cities.items():  # Loops through the cities dictionary and lists the keys and values
            print("- Use {} for {}".format(key, value.title()))
        city = input("Enter a city >> ")
        if city.lower() not in cities.keys():
            print("You have entered an incorrect value please try again.")
        if city.lower() in cities.keys():
            print("You have chosen {}".format(cities[city.lower()].title()))

    # TO DO: get user input for month (all, january, february, ... , june)

    while month.lower() not in months:
        print("Now choose a month you would like to investigate")
        print("The available options are:")
        for m in months:
            print("-", m)
        month = input("What month would you like >> ")
        if month.lower() not in months:
            print("You have made an invalid entry please try again.")
        if month.lower() in months:
            print("You have chosen {}".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while day.lower() not in days:
        print("Now choose a day you would like to investigate")
        print("The available options are:")
        for d in days:
            print("-", d)
        day = input("What day would you like >> ")
        if day.lower() not in days:
            print("You have made an invalid entry please try again.")
        if day.lower() in days:
            print("You have chosen {}".format(day.title()))

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

    df = pd.read_csv(CITY_DATA[cities[city.lower()]])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    com_month = df['month'].mode()[0]
    com_month = months[int(com_month)]
    print("The most common month of travel is: {}".format(com_month.title()))
    # TO DO: display the most common day of week
    com_day = df['day'].mode()[0]
    print("The most common day of travel is: {}".format(com_day))
    # TO DO: display the most common start hour
    com_hour = df['hour'].mode()[0]
    print("The most common hour of travel is: {}".format(com_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    com_start_station = df['Start Station'].mode()[0]
    print("The most common start station is {}".format(com_start_station))

    # TO DO: display most commonly used end station

    com_end_station = df['End Station'].mode()[0]
    print("The most common end station is {}".format(com_end_station))

  #  TO DO: display most frequent combination of start station and end station trip
    com_trip = (df['Start Station'] + " to " + df['End Station']).mode()[0]
    print("The most common trip made is {}".format(com_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_dur = df['Trip Duration'].sum()
    print('The total time traveled was {} seconds.\n'.format(int(total_trip_dur)))

    # TO DO: display mean travel time
    avg_trip_dur = df['Trip Duration'].mean()
    print('The average travel time was {} seconds.\n'.format(int(avg_trip_dur)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The total amount of each user type is:\n{}\n'.format(user_type))

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print('The total in each gender are:\n{}\n'.format(gender))
    except:
        print('Unfortunately there is no gender data for this city.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_yob = min(df['Birth Year'])
        print('The earliest year of birth is {}.\n'.format(int(earliest_yob)))
        most_recent_yob = max(df['Birth Year'])
        print('The most recent year of birth is {}.\n'.format(int(most_recent_yob)))
        most_common_yob = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}.\n'.format(int(most_common_yob)))
    except:
        print('Unfortunately there is no birth data for this city.\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))    
    print('-'*40)

def display_raw_data(df):
    """Displays raw bikeshare data."""
    
    raw = ""
    start = 0
    end = 5
    while raw.lower() != "no":
        raw = input('\nWould you like to view 5 (more) lines of raw bikeshare data? Enter yes or no.\n')
        if raw.lower() == 'yes':
            print(df[df.columns[0:]].iloc[start:end])
            start += 5
            end += 5
        else:
            print("You have entered an incorrect value please try again")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
