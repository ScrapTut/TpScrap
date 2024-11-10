import datetime
import pandas as pd

def main():
    # Your main code here
    current_time = datetime.datetime.now()
    print(f"Script ran successfully at {current_time}")
    
    # Example: Create a log file
    with open('log.txt', 'a') as f:
        f.write(f"Script ran at {current_time}\n")

if __name__ == "__main__":
    main()
