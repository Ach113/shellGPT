import os
import openai
import argparse

import util

openai.api_key = os.environ['OPENAI_API_KEY']


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='shellGPT',
        description='chatGPT interface inside terminal',
    )

    available_models = openai.Model.list()['data']
    available_model_names = set([x['root'] for x in available_models])
    parser.add_argument('-m', default='gpt-3.5-turbo', metavar='model',
                        choices=available_model_names,
                        help='which chat model to use, default `gpt-3.5-turbo`')
    parser.add_argument('-l', '--log', type=bool, default=False, metavar='log',
                        action=argparse.BooleanOptionalAction,
                        help='option to turn on conversation logging')
    return parser.parse_args()


def main():
    args = parse_arguments()
    util.clean()

    while True:
        prompt = input('$ ')
        file_path, mode = '', ''

        if prompt == 'q':
            util.clean()
            exit(0)

        if '>' in prompt:
            prompt, file_path, mode = util.process_redirect(prompt)

        if '<' in prompt:
            prompt = util.process_file_input(prompt)

        response = openai.ChatCompletion.create(
            model=args.m,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )

        response_text = response['choices'][0]['message']['content'].strip('\n')

        if args.log or mode:
            util.log_conv(prompt, response_text, args.log, file_path, mode)
        print(response_text)


if __name__ == '__main__':
    main()
