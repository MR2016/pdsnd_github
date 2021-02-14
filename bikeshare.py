import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday']


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
    city_name=''
    while(city_name.lower() not in CITY_DATA ):
        city_name=input("\nEnter the city for which you want to perform the analysis (valid values- chicago/new york city/washington) : \n")
        if city_name.lower() in CITY_DATA:
           city=CITY_DATA[city_name.lower()]
        else:
            print("\nOops !! You have entered invalid city name.")
                

    # TO DO: get user input for month (all, january, february, ... , june)
    month_name=''
    while(month_name.lower() not in MONTH_DATA ):
        month_name=input("\nEnter the month for which you want to perform the ananlysis(valid values- 'all', 'january', 'february', 'march', 'april', 'may', 'june') : \n")
        if month_name.lower() in MONTH_DATA:
            month=month_name.lower()
                
        else:
            print("\nOops !! You have entered invalid month name.")
                 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name=''
    while(day_name.lower() not in DAY_DATA ):
            day_name=input("\nEnter the day for which you want to perform the ananlysis(valid values- 'all', 'monday', 'tuesday', 'wednesday','thursday', 'friday', 'saturday', 'sunday'): \n")
            if day_name.lower() in DAY_DATA:
                day=day_name.lower()
            else:
             print("\nOops !! You have entered invalid day name.")

    print('-'*100)
    return city,month,day


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
    df = pd.read_csv(city)
   # print(df)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(df['Start Time'])
    
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    #print(df)
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
       # print(month)
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]
        
    #print("\nPrint the data frame\n")
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\n1-Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('\n Most Popular month:', popular_month)

     #TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nMost Popular day of the week:', popular_day)

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nMost Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n2-Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nMost Popular Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nMost Popular End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    # Find the most frequent combination of start and end time by creating a new column frequent combination
    frequent_combination =df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost frequent trip :\n', frequent_combination )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n3-Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel_Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel_Time'].sum()
    print("\n Total travel time : ",total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time=df['Travel_Time'].mean()
    print("\n Mean travel time : ",mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n4-Calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertype_counts=df['User Type'].value_counts()
    print('\nCalculating user counts : \n',usertype_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts()
        print('\nCalculating gender counts : \n',gender_counts)
    except:
        print('\nUnavailable data for gender for the selected combination.\n')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
       earliest_DOB=df['Birth Year'].min()
       print('\nCalculating earliest DOB: \n',earliest_DOB)
       latest_DOB=df['Birth Year'].max()
       print('\nCalculating latest DOB: \n',latest_DOB)
       common_DOB=df['Birth Year'].mode()[0]
       print('\nCalculating most common DOB: \n',common_DOB)
    except:
       print('\nUnavailable data for Birth Year for the selected combination of city,month and day.\n')
              
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*100)
    
    
def display_raw_data(df):
   
    """ Displays the set of 5 raw data used to compute the stats """
    start=0
    end=5
    print("print shape of the data frame :",df.shape)
    raw_data = input("\n Do you like to view five rows of raw data used for computation? Please write 'yes' or 'no' \n").lower()
    
    if raw_data == 'yes':
        while end <= df.shape[0]:
            print(df.iloc[start:end])
            start+=5
            end+=5
            raw_data = input("\n Do you like to view five rows of raw data used for computation? Please write 'yes' or 'no' \n").lower()
            if raw_data == 'no':
                break
        
    print('-'*100)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n Would you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
