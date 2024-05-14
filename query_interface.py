# query_interface/query_interface.py

import os

def search_logs(query):
    log_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), 'log_ingestor'))
    if not os.path.exists(log_directory):
        print("Log directory not found.")
        return

    log_files = [f for f in os.listdir(log_directory) if f.endswith('.log')]
    if not log_files:
        print("No log files found.")
        return

    for log_file in log_files:
        with open(os.path.join(log_directory, log_file), 'r') as file:
            for line in file:
                if query in line:
                    print(f"Found in {log_file}: {line.strip()}")

def main():
    search_query = input("Enter search query: ")
    search_logs(search_query)

if __name__ == "__main__":
    main()
