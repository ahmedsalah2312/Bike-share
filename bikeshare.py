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
    city = input('Enter city name from (chicago, new york city, washington):').lower()
    while city not in CITY_DATA.keys():
        print('Can you enter valid city, please!')
        city = input('Enter city name from (chicago, new york city, washington):').lower()
        
    

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['jan', 'feb', 'mar', 'apr', 'may', 'june','all']
    while True:
        month = input('Enter month please from (jan, feb, mar, apr, may, june, all): ').lower()
        if month in months :
            break
        else:
            print('Not a valid input')
            
          
        

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sun','mon','tue','wed','thu','fri','sat','all']
    while True:
        day=input('Can you enter a day please from (sun,mon,tue,wed,thu,fri,sat,all):').lower()
        if day in days:
            break
        else:
            print('Not a valid input')

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
    
    df['day_of_week'] = df['Start Time'].dt.week
    
    df['hour'] = df['Start Time'].dt.hour
    
 
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print ('the most common month : {}'.format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print ('the most common day of week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    print ('the most common start hour: {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station is : {} '.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('most commonly used end station is : {} '.format(common_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    start_end_combine=(df['Start Station']+','+['End Station']).mode()[0]
    print('most frequent combination of start station and end station : {} '.format(start_end_combine))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data_to_user(df):
    # prompt the user if they want to see 5 lines of raw data 
    i = 0
    user_input_answer = input('do you want to display 5 rows of raw data?: yes or no :').lower()
        
    if user_input_answer == 'no':
       
        print('Thanks!')
    elif user_input_answer not in ['yes','no']:
        
        print('not a valid answer!: please type yes or no :')
     # Continue iterating these prompts and displaying the next 5 lines of raw data at each iteration   
    else:
        while i+5 < df.shape[0]:
            print(df.iloc[i:i+5])
            i += 5 
            user_input_answer = input('do you want to display the next 5 rows of raw data?: yes or no : ').lower()
            if user_input_answer == 'no':
                print('Thanks!')
                break           
           

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is : {}'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('mean travel time is : {}'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user type
    counts_of_user_type = df['User Type'].value_counts()
    print('Counts of user types : {} '.format(counts_of_user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df:
        counts_of_gender = df['Gender'].value_counts()
        print('Counts of gender is: {} '.format(counts_of_gender))
    else:
        print('not a valid data')
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        
        earliest_year = int(df['Birth Year'].min())
        print('Earliest year of birth is : {} '.format(earliest_year))
          
        most_recent_year = int(df['Birth Year'].max())
        print('Most recent year of birth is : {} '.format(most_recent_year))
    
        Most_common_year = int(df['Birth Year'].mode()[0])
        print('Most common year of birth is : {} '.format(Most_common_year))
    else:
        print('not a valid data')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        display_data_to_user(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
