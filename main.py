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

# Function for sending random phrase from dictionary
def get_phrase():
    df = pd.read_csv('words_b.csv')
    # For generate a random mnemonic phrase 
    df_12w = df.sample(n=12)['English'].to_list() #.to_string(header=False, index=False)]
    df_w = print(*df_12w, sep=', ')
    return df_w

def main():
    get_phrase()

if __name__ == '__main__':
    main()
