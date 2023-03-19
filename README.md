## shellGPT
Most bare-bones interface for chatGPT inside terminal.

## Install:
```
git clone https://github.com/Ach113/shellGPT
pip install .
```

## Usage:
```
usage: shellGPT [-h] [-m model]

chatGPT interface inside PowerShell terminal

options:
  -h, --help  show this help message and exit
  -m, --model    which chat model to use, default `gpt-3.5-turbo`
```
Before running, make sure to set the value of environment variable
`OPENAI_API_KEY` to your private API key.
```
$env:OPENAI_API_KEY = "your key here"
```
Now you can interface with chatGPT directly from the terminal:
```
> shellGPT
    $ hello there!
    Hello! How can I assist you today?
```

## Why?
I mostly use PyCharm for development, and I find it very convenient
to be able to use chatGPT within the PyCharm terminal.

## Planned features
1. add option to log messages by specifying `--log` 
2. load logged messages to the model