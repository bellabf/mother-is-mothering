"""This Python script contains a function called `mothers_words` that prints a random selection of lyrics from Taylor Swift songs.

The function accomplishes this by:
1. The original data comes from Taylor Swift (and collaborators), but it was copiled from this [source](https://docs.google.com/document/d/17uOl0-tOKdJrudRani4e4XXt-MKDELDdJ4GJT5kYDyE/edit?usp=sharing)

2. I cleaned song names, dates, and commentaries from the original file before I pickled it into the ts-lyrics.pkl file. There is chance a song titled didn't follow the regular expressions (if you find it, please report it so we can get it fixed)

3. Loading previously pickled and cleaned song lyrics data from the "../ts-lyrics.pkl" file.

4. Generating a random starting index and ending index within the range of available lines in the dataset, the max number of lyrics you can have is five.

5. Extracting a subsection of the lyrics based on the generated indices.

6. Joining the selected lines into a single string.

7. Printing the resulting string to the console.

To run the script, simply execute it using a Python interpreter.
The randomly selected lyrics will be printed directly to the console.

Dependencies:
* `numpy` - used for generating random integers.
* `pickle` - used for loading previously saved data."""


def mothers_words():
    """Generates and prints a random selection of lyrics from the TS song library.

    This function selects a contiguous block of lines from the loaded song lyrics data and prints them to the console.
    Sometimes it can mix lyrics from different songs, those are also mother's words.

    Returns:
        None
    """

    import numpy as np
    import pickle

    with open("../ts-lyrics.pkl", "rb") as f:
        cleaned_lines = pickle.load(f)

    max_index = len(cleaned_lines)
    start_index = np.random.randint(low=0, high=max_index, size=1)[0]
    num_lines = np.random.randint(low=1, high=6, size=1)[0]
    end_index = min([start_index + num_lines, max_index])

    output_string = "\n".join(cleaned_lines[start_index:end_index])

    print(output_string)


if __name__ == "__main__":
    mothers_words()
