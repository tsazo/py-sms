from random import choice

def response_handler(body):
    message = ""
    # if body == 'music:sad':
    #     message = "How are you feeling today?"    
    if body == 'music:sad':
        message = "Click this link for some music suggestions: https://open.spotify.com/user/trinivy/playlist/5XWsj8JAxK3bYqkcSsxorF"
        choicequotes = ["hi", "bye", "wassup"]
    elif body == 'music:happy':
        message = "Click this link for some music suggestions: https://open.spotify.com/user/psanchez7870-us/playlist/6ywxHnVNdzct4ZpEeePHn6"
        quotes = ["", "", ""]
        send_media(choice(quotes))
    elif body == 'music:angry':
        message = "Click this link for some music suggestions: hi"
        quotes = ["", "", ""]
        send_media(choice(quotes))
    elif body == 'music:inspired':
        message = "Click this link for some music suggestions: https://open.spotify.com/user/trinivy/playlist/7mZhXBHm17byBfUqeJTv1l"
        quotes = ["", "", ""]
        send_media(choice(quotes))
    elif body == 'music:brokenhearted':
        message == "Click this link for some music suggestions: https://open.spotify.com/user/trinivy/playlist/5XWsj8JAxK3bYqkcSsxorF"
        quotes = ["", "", ""]
        send_media(choice(quotes))
    elif body == "music:love":
        message = "Click this link for some music suggestions: https://open.spotify.com/user/trinivy/playlist/5yl3DXV8oY4BvL45QqHunV"
    elif body == 'music:throwback':
        message = "Click this link for some music suggestions: https://open.spotify.com/user/trinivy/playlist/4HCiAU9cO1Es2LgsaH244L"
    elif body == 'music:workout':
        message = "Click this link for some music suggestions: https://open.spotify.com/user/psanchez7870-us/playlist/62eRNgiFPEmWeHhcJ5GPl6"
    #elif body == 'food ideas':
    #    message = "hey"
    else:
        message = "Invalid command. Type in 'music:mood' (possible moods are 'sad', 'happy', 'workout', 'brokenhearted', 'love', 'throwback', 'inspired', 'angry') if you want some music to hear."
    return message