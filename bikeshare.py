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
        city = input('Enter city to filter by:\n Chicago, New York City, Washington\n').lower()
        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print('Invalid input.. Try again!')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter month to filter by:\n All, January, February, March, April, May, June\n').lower()
        if month.lower() not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('Invalid input,.. Try again')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter day to filter by:\n All, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday\n').lower()
        if day.lower() not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Invalid input.. Try again!')
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
    # TO DO: load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # TO DO: convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: extract month and day of the week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # TO DO: filter by month if applicable
    if month != 'all':

        # TO DO: use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # TO DO: filter by month to create the new dataframe
        df = df[df['month'] == month]

    # TO DO: filter by day of week if applicable
    if day != 'all':

        # TO DO: filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week: {}'.format(common_day_of_week))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: {}'.format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print('The most commonly used start station: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print('The most commonly used end station: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination = df.groupby(['Start Station', 'End Station']).count()
    print('The most frequent combination for both start and end station: {}'.format(combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = (df['Trip Duration'].sum())/ 3600 # In hours
    print('Total travel time: {} hours'.format(total_time))

    # TO DO: display mean travel time
    mean_time = (df['Trip Duration'].mean())/ 3600 # In hours
    print('Mean travel time: {} hours'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User types count: {}'.format(user_types))

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('Gender count: {}'.format(gender_count))
    except KeyError:
        print('Gender count: NULL')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth: {}'.format(earliest_year))
    except KeyError:
        print('The earliest year of birth: NULL')

    try:
        recent_year = df['Birth Year'].max()
        print('The most recent year of birth: {}'.format(recent_year))
    except KeyError:
        print('The most recent year of birth: NULL')

    try:
        common_year = df['Birth Year'].value_counts().idxmax()
        print('The most common year of birth: {}'.format(common_year))
    except KeyError:
        print('The most common year of birth: NULL')

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

        #Displays five lines of data if the user specifies that they would like to view. If so, the loop continues until the user says no

        display_data = input('Would you like to see raw data?\n Enter Yes or No\n')
        start_data = 0

        while True:
            if display_data.lower() != 'no':
                print(df.iloc[start_data : start_data + 5])
                start_data += 5
                display_data = input('Would you like to see more data?\n Enter Yes or No\n').lower()
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
