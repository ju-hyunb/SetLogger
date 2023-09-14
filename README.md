## SetLogger

The reasons for creating the log are as follows.

1. Understand service operational status (*monitoring)
2. Identify and handle faults
3. Performance improvement through service metrics verification

Avoid indiscriminate use of print() statements and record logs enable efficient memory use and accurate debugging.

--------

When executing a file that you want to leave a log, you can use it anywhere by passing the location of the log setting file to a factor.
By changing the name of the log file for each executable file, the log file may be managed independently for each service.

#### For example

```python
python3 example.py "/home/user/setlog/"
```

```python
example.py.debug.log
example.py.exception.log
```


-------------


Log Level __[debug, info, warn, error, exception]__

I added the ability to specify the log level I want to use


```python
import SetLogger as logger
logger.get_logger(script, ["debug", "info", "exception"])
```


```python
config['loggers']['root']['handlers'] = []
for level in levels:
    config['handlers'][f'file_{level}']['filename'] = script_name + '.' + config['handlers'][f'file_{level}']['filename']
    config['loggers']['root']['handlers'].append(f'file_{level}')

loglevel = ["debug", "info", "warn", "error", "exception"]
for level in loglevel:
    if level not in levels:
        del config["handlers"][f"file_{level}"]

```


-----------

If you want receive notification about serious log, you can use `AlertSalck.py`.
- Requirements
  1. Slack API(App)
  2. Slakc API Token and Channel
  3. `pip install slackclient`




__Create a SlackHandler__

```python
class SlackHandler(logging.Handler):
    def emit(self, record):
        message = self.format(record)
        try:
            response = slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
            if not response["ok"]:
                print(f"Failed to send message to Slack: {response['error']}")
        except SlackApiError as e:
            print(f"Error sending message to Slack: {e.response['error']}")
```


__Result__

![image](https://github.com/ju-hyunb/SetLogger/assets/104177526/b6af34e3-030f-4e53-8a84-7578e8af77c9)
