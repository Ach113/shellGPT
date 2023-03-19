import os
import openai
import argparse

openai.api_key = os.environ['OPENAI_API_KEY']


def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='shellGPT',
        description='chatGPT interface inside PowerShell terminal',

    )

    available_models = openai.Model.list()['data']
    available_model_names = set([x['root'] for x in available_models])
    parser.add_argument('-m', default='gpt-3.5-turbo', metavar='model',
                        choices=available_model_names,
                        help='which chat model to use, default `gpt-3.5-turbo`')

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_arguments()

    while True:
        prompt = input('$ ')
        response = openai.ChatCompletion.create(
            model=args.m,
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )
        print(response['choices'][0]['message']['content'].strip('\n'))
