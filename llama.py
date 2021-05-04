import json
import time
import twitter
import emoji
from emoji.unicode_codes.en import EMOJI_UNICODE_ENGLISH    # to get all the emojis we can use
import random



def loadkeys() -> dict:
    with open('keys.json', 'r') as infile:
        keys = json.load(infile)
    return {
        'consumer_key': keys['apiKey'],
        'consumer_secret': keys['apiSecretKey'],
        'access_token_key': keys['accessToken'],
        'access_token_secret': keys['accessTokenSecret'],
    }


def load_llama() -> str:
    with open('llama.txt', 'r') as infile:
        return infile.read()


def load_emojis() -> list:
    # returns all emojis that are able to be a length of 1 
    return [emoji.emojize(k) for k in EMOJI_UNICODE_ENGLISH.keys() if len(emoji.emojize(k)) == 1]


def post_llamas():
    emojis = load_emojis()
    llama = load_llama()
    api = twitter.Api(**loadkeys())

    # keep posting llamas until we have released all the llamas
    while 0 < len(emojis):
        selected_emoji = emojis.pop(random.randrange(0, len(emojis)))
        status = api.PostUpdate(llama.replace('?', selected_emoji))
        print(status.text)
        # the llama should sleep before posting again
        time.sleep(20)
        break   # debug break for now, replace on rPI

    print('enough llamas')

if __name__ == '__main__':
    """
    api = twitter.Api(**loadkeys())
    status = api.PostUpdate('I AM AN EMOJI LLAMA POSTING FROM THE CODE!!!!')
    print(status.text)
    """
    '''
    for emoji_code in load_emojis():
        print(f'{emoji_code} => {emoji.emojize(emoji_code)}\tlength: {len(emoji.emojize(emoji_code))}')
    '''
    post_llamas()