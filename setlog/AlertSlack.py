import logging
from slack import WebClient
from slack.errors import SlackApiError


SLACK_API_TOKEN = input("INPUT YOUR SLACK API TOKEN : ")
SLACK_CHANNEL = input("INPUT YOUR SLACK CHANNEL : ")

slack_client = WebClient(token=SLACK_API_TOKEN)
formatter = logging.Formatter(fmt="[%(asctime)s][%(funcName)s:%(levelname)s:%(lineno)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")



class SlackHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        try:
            response = slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
            if not response["ok"]:
                print(f"Failed to send message to Slack: {response['error']}")
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")




def Send(obj):
    
    slack_handler = SlackHandler()
    slack_handler.setLevel(logging.ERROR)
    slack_handler.setFormatter(formatter)
    obj.addHandler(slack_handler)
