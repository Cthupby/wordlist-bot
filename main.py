import pandas as pd

# Function for sending random word from dictionary
def get_words():
    df = pd.read_csv('words_b2.csv')
    df_s = df.sample() # For randomize words from dictionary
    # For get 2 columns from dictionary and covert it in string for sending to user
    df_worde = df_s['English'].to_string(header=False, index=False).capitalize()
    df_wordr = df_s['Russian'].to_string(header=False, index=False).capitalize()
    df_url = df_s[['URL']].to_string(header=False, index=False)
    # For get tuple from this 3 columns
    df_all = [df_wordr, df_worde, df_url]
    return df_all

def main():
    print(get_words())

if __name__ == '__main__':
    main()
