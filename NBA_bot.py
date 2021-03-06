# built following Matt Makai's guide 
# https://www.fullstackpython.com/blog/build-first-slack-bot-python.html


import os
from slackclient import SlackClient
import time

nba_bot_name = os.environ.get('nba_bot')
nba_bot_token = os.environ.get('nba_bot_token')
bot_id = os.environ.get('bot_id')

slack_client = SlackClient(nba_bot_token)

# consts
bot_const = "<@" + bot_id +">"


def handle_order(order, channel):
    response = "Not sure what you mean. Use the *" + EXAMPLE_order + \
               "* order with numbers, delimited by spaces."
    if order.startswith(player):
        # checkfor stats/last n games/ 
    elif order.startswith("Get high priority"):
    	repsonse = "Getting your high priority tickets"
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)



def parse_slack_output(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and bot_const in output['text']:
                # return text after the @ mention, whitespace removed
                print output['text'] #want to take a look to see how I can change this
                return output['text'].split(bot_const)[1].strip().lower(),output['channel']
    return None, None


#pulls in all rtm data off slack 
if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("NBA bot dribbling")
        while True:
            order, channel = parse_slack_output(slack_client.rtm_read())
            if order and channel:
                handle_order(order, channel)
            time.sleep(1)
    else:
        print("Connection fucked. Bad slack token or bot ID")