import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    return city, month, day
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
while True:

       city = input('Which city do you want to explore Chicago, New York or Washington? \n> ').lower()

       if city in CITIES:

           break
    # TO DO: get user input for month (all, january, february, ... , june)
month = input(" Which month - January, February, March, April, May, or June? '\' You can type \'all\' again to apply no day filter. \n. ").lower()
print("you Enter is:", month)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, '\' You can type \'all\' again to apply no day filter. \n").lower()

print("you Enter is:", day)

print('-'*40)
#return city, month, day


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])



    # extract month and day of week and hour from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':

        month =  MONTHS.index(month) + 1

        df = df[ df['month'] == month ]



    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[ df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].value_counts().idxmax()

    print("The most common month is :", most_common_month)

    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].value_counts().idxmax()

    print("The most common day of week is :", most_common_day_of_week)

    # TO DO: display the most common start hour

    most_common_start_hour = df['hour'].value_counts().idxmax()

    print("The most common start hour is :", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    most_common_start_station = df['Start Station'].value_counts().idxmax()

    print("The most commonly used start station :", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()

    print("The most commonly used end station :", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]

    print("The most commonly used start station and end station : {}, {}"\

            .format(most_common_start_end_station[0], most_common_start_end_station[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel = df['Trip Duration'].sum()

    print("Total travel time :", total_travel)

    # TO DO: display mean travel time
    
    mean_travel = df['Trip Duration'].mean()

    print("Mean travel time :", mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:\n")

    user_counts = df['User Type'].value_counts()
    
    for index, user_count in enumerate(user_counts):
        print("{}: {}".format(user_counts.index[index], user_count))

    print()

    if 'Gender' in df.columns:

        user_stats_gender(df)

    if 'Birth Year' in df.columns:
        user_stats_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time ))

    print('-'*40)

def user_stats_gender(df):
    # TO DO: Display counts of gender
    
    print("Counts of gender:\n")

    gender_counts = df['Gender'].value_counts()

    for index,gender_count   in enumerate(gender_counts):

        print("  {}: {}".format(gender_counts.index[index], gender_count))

    

    print()

def user_stats_birth(df):
    # TO DO: Display earliest, most recent, and most common year of birth
    #birth_year = df['Birth Year']
# the most common birth year
    most_common_year = df['Birth Year'].value_counts().idxmax()
    print("The most common birth year:", most_common_year)

    # the most recent birth year
    most_recent = df['Birth Year'].max()
    print("The most recent birth year:", most_recent)

    # the most earliest birth year
    earliest_year = df['Birth Year'].min()
    print("The most earliest birth year:", earliest_year)
    
def table_stats(df, city):

    """Displays statistics on bikeshare users."""

    print('\nCalculating Dataset Stats...\n')

    

    # counts the number of missing values in the entire dataset

    number_of_missing_values = np.count_nonzero(df.isnull())

    print("The number of missing values in the {} dataset : {}".format(city, number_of_missing_values))



    # counts the number of missing values in the User Type column

    number_of_nonzero = np.count_nonzero(df['User Type'].isnull())

    print("The number of missing values in the \'User Type\' column: {}".format(number_of_missing_values))

    
def display_data(df):

    """Displays raw bikeshare data."""

    row_length = df.shape[0]



    # iterate from 0 to the number of rows in steps of 5

    for i in range(0, row_length, 5):

        

        yes = input('\nWould you like to examine the particular user trip data? Type \'yes\' or \'no\'\n> ')

        if yes.lower() != 'yes':

            break

        

        # retrieve and convert data to json format

        # split each json row data 

        row_data = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')

        for row in row_data:

            # pretty print each user data

            parsed_row = json.loads(row)

            json_row = json.dumps(parsed_row, indent=2)

            print(json_row)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        table_stats(df, city)
        display_data(df)
       # user_stats_gender(df)
       # user_stats_birth(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
