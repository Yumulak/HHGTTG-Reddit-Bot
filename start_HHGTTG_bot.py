import praw

from functions import scan_comments


trigger_dictionary = {
    ("so long", "thanks for the fish", "all the fish"): ["So long, and thanks for all the fish!! (https://www.youtube.com/watch?v=N_dUmDBfp6k)"],
    ("There is a theory",): ["There is a theory which states that if ever anyone discovers exactly what the Universe is for and why it is here, it will instantly disappear and be replaced by something even more bizarre and inexplicable. There is another theory which states that this has already happened."],
    ("It is a mistake", "potatoes"): ["It is a mistake to think you can solve any major problems just with potatoes."],
    ("new yorkers",): ["The last time anybody made a list of the top hundred character attributes of New Yorkers, common sense snuck in at number 79."],
    ("The answer", "question of life", "the universe", "everything"): ["The answer is 42"]
}

if __name__ == '__main__':
    HHGTTG_bot = praw.Reddit(
        "HHGTTG_bot", user_agent='HHGTTG quote bot by /u/Future-Guess-366')
    scan_comments(HHGTTG_bot, trigger_dictionary)
