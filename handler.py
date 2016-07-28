def response_handler(body):
    message = "Type 'music' if you want some music to hear or 'food ideas' if you don't know what to eat today:"
    if body == 'music:sad':
        message = "How are you feeling today?"    
        if music == 'music:sad':
            message = "Here are some music suggestions: "
            quotes = ["", "", ""]
            send_media(choice(quotes))
        elif music == 'happy':
            message = "Here are some music suggestions: "
            quotes = ["", "", ""]
            send_media(choice(quotes))
        elif music == 'angry':
            message = "Here are some music suggestions: "
            quotes = ["", "", ""]
            send_media(choice(quotes))
        elif music == 'inspired':
            message = "Here are some music suggestions: "
            quotes = ["", "", ""]
            send_media(choice(quotes))
        elif music == 'Grieving Heart':
            message == "Here are some music suggestions: "
            quotes = ["", "", ""]
            send_media(choice(quotes))
        elif music == "Falling in Love":
            message = "Here are some music suggestions: "
        elif music == 'throwback':
            message = "Here are some music suggestions: "
        elif music == 'gym motivation':
            message = "Here are some music suggestions: "
    elif body == 'food ideas':
        message = "hi"
    else:
        message = "hi"
    return message

