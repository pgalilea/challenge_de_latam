import emoji

def extract_emojis(text):
    return [x.chars for x in emoji.analyze(text)]
