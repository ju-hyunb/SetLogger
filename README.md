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
