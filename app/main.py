import pandas as pd

from typing import List


def get_words() -> List[str]:
    '''
    Function for sending random word from dictionary.
    '''
    dataframe = pd.read_csv('words_b.csv')
    dataframe_sample = dataframe.sample()
    '''
    Get 2 columns from dictionary
    and covert it in string for sending to user.
    '''
    dataframe_word = dataframe_sample['English'].to_string(
        header=False,
        index=False
    ).capitalize()
    dataframe_url = dataframe_sample[['URL']].to_string(
        header=False,
        index=False
    )
    '''
    Get tuple from this 3 columns.
    '''
    dataframe_all = [dataframe_word, dataframe_url]
    return dataframe_all


def get_phrase() -> List[str]:
    '''
    Function for sending random phrase from dictionary.
    '''
    dataframe = pd.read_csv('words_b.csv')
    '''
    Generate a random mnemonic phrase.
    '''
    dataframe_phrase = dataframe.sample(n=12)['English'].to_list()
    return dataframe_phrase


def main():
    get_phrase()


if __name__ == '__main__':
    main()
