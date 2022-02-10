import pandas as pd


# Function for sending random word from dictionary
def get_words():
    dataframe = pd.read_csv('words_b.csv')
    dataframe_sample = dataframe.sample() # For randomize words from dictionary
    # For get 2 columns from dictionary and covert it in string for sending to user
    dataframe_word = dataframe_sample['English'].to_string(header=False, index=False).capitalize()
    dataframe_url = dataframe_sample[['URL']].to_string(header=False, index=False)
    # For get tuple from this 3 columns
    dataframe_all = [dataframe_word, dataframe_url]
    return dataframe_all

# Function for sending random phrase from dictionary
def get_phrase():
    dataframe = pd.read_csv('words_b.csv')
    # For generate a random mnemonic phrase 
    dataframe_phrase = dataframe.sample(n=12)['English'].to_list() #.to_string(header=False, index=False)]
    return dataframe_phrase

def main():
    get_phrase()


if __name__ == '__main__':
    main()

