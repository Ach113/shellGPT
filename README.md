## shellGPT
Interface for chatGPT inside Windows PowerShell terminal.

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