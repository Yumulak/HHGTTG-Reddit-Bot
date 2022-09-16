# Hitchhikers Guide to the Galaxy bot

Reddit bot that replies to comments with certain keywords with quotes from Hitchhikers Guide to the Galaxy!

### Request a feature

Want to add quotes? Create an [issue](https://github.com/Yumulak/HHGTTG-Reddit-Bot/issues) on Github or message me on [Reddit](https://www.reddit.com/user/Future-Guess-366/)!

### Design

These bots are extremely simple by design so anyone can run them. The [license](https://github.com/Yumulak/HHGTTG-Reddit-Bot/blob/main/LICENSE) allows free use of the code is you likewise share the source code.

### Running

1. Download the codebase
2. Create a file called `praw.ini` and fill it out with your Reddit [bot info](https://www.reddit.com/r/redditdev/comments/hasnnc/where_do_i_find_the_reddit_client_id_and_secret/) (should look something like [this](https://i.imgur.com/wCuAGLG.png))
3. Run `pip install -r requirements.txt`
4. Run `python start_HHGTTG_bot.py (or whatever you named it)`

That's it!

### Modifying the triggers & responses

Edit the dictionary found at the top of the relevant bot file. Keep the same format!