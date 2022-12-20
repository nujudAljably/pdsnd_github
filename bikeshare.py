import time
import pandas as pd
import numpy as np
import calendar


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_list=['January', 'February', 'March' , 'April', 'May', 'June', 'None']
city_name=['chicago', 'new york city', 'washington']
day_name=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','None']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    
    while True:
        city = input(" Type city name :  \n (chicago, new york city, washington)").lower()
        if city in city_name:
            break
        else:
            print ("Sorry, Type city name agine ")
            continue 
   # get user input for month (all, january, february, ... , june)
    while True:
        month = input(" Type month name :  \n(January, February, March , April, May, June, or 'none' to apply no month filter  \n)").title()
        if month in month_list:
            break
        else:
            print ("Sorry, Type month name agine ")
            continue 


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(" Type day name :  \n(Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday) or 'none' to apply no day filter\n").title()
        
        if day in day_name:
            break
        else:
            print ("Sorry, Type day name agine ")
            continue 

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    
    if month.title() != 'None':
        month = month_list.index(month) +1
        
        df=df[df['month'] == month]
        
    if day.title() !='None':
        df =df[df['day'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print('Most Common Month:',common_month)


    # display the most common day of week
    common_day=df['day'].mode()[0]
    print('Most Common Day:', common_day)

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    common_hour=df['hour'].mode()[0]
    print('Most Common hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station=df['Start Station'].mode()[0]
    print(" Most commonly used start station :",start_station)
    # display most commonly used end station
    end_station=df['End Station'].mode()[0]
    print(" Most commonly used end station :",end_station)

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + ' To ' + df['End Station']
    combination_station=df['trip'].mode()[0]
    print(" Most frequent combination of start station and end station trip :",combination_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time= df['Trip Duration'].sum()
    print('Total Travel Time: ',total_travel_time/60 , 'hour')

    # display mean travel time
    mean_travel_time= df['Trip Duration'].mean()
    print('Mean Travel Time:',mean_travel_time/60,'hour' )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types=df['User Type'].value_counts()
    print("\n User Type:\n",user_types)

    # Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print('\n Gender: \n',gender_counts)
    except KeyError:
        print("\n No data available. ")

    # Display earliest, most recent, and most common year of birth
    try:
        Earliest_Year = df['Birth Year'].min()
        print('\n Earliest Year:', Earliest_Year)        
    except KeyError:
        print("\n No data available. ")
        
    try:  
        Most_Recent_Year = df['Birth Year'].max()
        print('\n Most Recent Year:', Most_Recent_Year)          
    except KeyError:
        print("\n No data available. ")
      
    try:    
        Most_Common_Year = df['Birth Year'].value_counts().mode()[0]
        print('\n Most Common Year:', Most_Common_Year)         
    except KeyError:
        print("\n No data available. ")

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
        
        view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n")
        start_loc = 0
        print(df.head(start_loc))
        while True:
            if view_data.lower() != 'no':
                print(df.iloc[start_loc:start_loc+5])
                start_loc += 5
                view_data = input("Do you wish to continue?: ").lower()
                continue
            else :
                break
        
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
