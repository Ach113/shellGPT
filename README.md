## shellGPT
Most bare-bones interface for chatGPT inside terminal.

## Install:
```
git clone https://github.com/Ach113/shellGPT
cd shellGPT
pip install .
```

## Usage:
```
usage: shellGPT [-h] [-m model] [-l | --log | --no-log]

chatGPT interface inside PowerShell terminal

options:
  -h, --help           show this help message and exit       
  -m model             which chat model to use, default `gpt-3.5-turbo`
  -l, --log, --no-log  option to turn on message logging (default: False)

```
Before running, make sure to set the value of environment variable
`OPENAI_API_KEY` to your private API key.
```
$env:OPENAI_API_KEY = "your key here"
```
Now you can interface with chatGPT directly from the terminal:
```
> shellgpt
    $ hello there!
    Hello! How can I assist you today?
```
You can use redirect operators `>` and `>>` to redirect bot's 
response to a specified filename:
```
$ Whats the meaning of life? > answer.txt
```
`>` indicates write mode (a new file will be created). \
`>>` indicates append mode (query, along with the response will 
be appended to existing file).

Alternatively, you can enable logging by indicating flag `-l` to store all your conversations 
with the chatbot for the current session. 
## Why?
I mostly use PyCharm for development, and I find it very convenient
to be able to use chatGPT within the PyCharm terminal.

## Planned features
1. add a way to load logged conversations into the model