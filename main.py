import pandas as pd

# Function for sending random word from dictionary
def get_words():
    df = pd.read_csv('words_b.csv')
    df_s = df.sample() # For randomize words from dictionary
    # For get 2 columns from dictionary and covert it in string for sending to user
    df_word = df_s['English'].to_string(header=False, index=False).capitalize()
    df_url = df_s[['URL']].to_string(header=False, index=False)
    # For get tuple from this 2 columns
    df_all = [df_word, df_url]
    return df_all

def main():
    get_words()

if __name__ == '__main__':
    main()
