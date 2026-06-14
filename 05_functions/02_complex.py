#Splitting complex tasks

def fetch_sales():
    print('1/3 fetching sales data...')

def filter_valid_sales():
    print('2/3 Filtering valid sales...')

def summarize_data():
    print('3/3 Summarizing data...')

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report Generated.")

generate_report()