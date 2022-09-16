import random
import re


ignore_authors = {"HHGTTG_bot", "Future-Guess-366"}


def find_word_in_text(text, word):
    """
    Finds if a word is within a text
    :param text: The text to search
    :param word: Word to look for in text
    :return: True if the word appears as a word in the text, False otherwise
    """
    found = re.compile(r'\b({0})\b'.format(
        word), flags=re.IGNORECASE).search(text)
    if found:
        return True
    return False


def get_comment_reply(text, trigger_dictionary):
    """
    Takes the text of a comment, determines which reply to use for it
    :param text: Reddit comment text
    :param trigger_dictionary: A tuple -> string list dictionary of triggers and responses
    :return: String containing comment to reply with, None if no comment is applicable
    """
    for triggers, responses in trigger_dictionary.items():  # For every case in trigger_dictionary
        for trigger in triggers:  # For each string in the cases
            # If the Reddit comment contains the string
            if find_word_in_text(text, trigger):
                # Return a random string that corresponds to the matched tuple
                return random.choice(responses)


def handle_comment(bot, comment, trigger_dictionary):
    """
    Takes in a comment from reddit
    Maybe replies to it
    :param trigger_dictionary: A tuple -> string list dictionary of triggers and responses
    :param comment: PRAW comment object
    """

    if (comment.author.name in ignore_authors) or (comment.author == bot.user.me()):
        return  # Don't reply to any comment made by someone in ignore_authors

    reply = get_comment_reply(comment.body, trigger_dictionary)
    if reply is not None:  # If we found a reply for the comment
        comment.reply(reply)

    # ignored_comments.append(comment.id)
    # with open("ignore_comments.txt", "a") as f:
    #     f.write(comment.id + "\n")


def scan_comments(bot, trigger_dictionary):
    """
    Permanently scans for comments in reddit
    Passes comments it finds to handle_comment
    :param trigger_dictionary: A tuple -> string list dictionary of triggers and responses
    :param bot: PRAW Reddit instance of a bot account
    """
    replied_to = []
# working on a way to save the comments that have been replied to into ignore_comments.txt
    print("Starting " + bot.user.me().name + "!")
    try:
        for comment in bot.subreddit("all").stream.comments(skip_existing=True):
            handle_comment(bot, comment, trigger_dictionary)

    except Exception as e:
        print("Exception caught: ")
        print(e)
        scan_comments(bot, trigger_dictionary)
