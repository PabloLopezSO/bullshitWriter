from datetime import datetime


dates =  ["Junio", "December", "June", 
              "January", "Jule", "January"]  
      
    # Sort the list in ascending order of dates 
dates.sort(key = lambda date: datetime.strptime(date, '%b'))
    
    # Print the dates in a sorted order 
print(dates) 