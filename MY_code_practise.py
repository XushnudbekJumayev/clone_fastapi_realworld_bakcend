import logging

# Configure logging
logging.basicConfig(
    force=True,
    datefmt= "%m,%d",
    level=logging.DEBUG,  # Change to INFO to hide debug messages
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_data():
    logging.debug("Starting to load data...")
    data = ["apple", "banana", "cherry"]
    logging.debug(f"Loaded data: {data}")
    
    return data

def process_data(data):
    logging.debug("Processing data...")
    processed = [item.upper() for item in data]
    logging.info(f"Processed data: {processed}")
    return processed

def main():
    logging.info("Program started.")
    data = load_data()
    result = process_data(data)
    logging.info("Program finished.")

if __name__ == "__main__":
    main()
