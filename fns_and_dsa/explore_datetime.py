import datetime # import the datetime module

def display_current_datetime():

    # get current date and time
    current_date = datetime.datetime.now()

    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

    # get the number of days from the user
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    # get the current date and time
    current_date = datetime.datetime.now()
    # add the specified number of days using timedelta
    future_date = current_date + datetime.timedelta(days=number_of_days)
    # format the future date as 'YYYY-MM-DD'
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # call functions to display current date/time and calculate future date
    display_current_datetime()
    calculate_future_date()

# ensure the script runs when executed directly

if __name__ == "__main__":
    main()

