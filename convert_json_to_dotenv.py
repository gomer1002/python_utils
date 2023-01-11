'''
Script that allows to convert json config file to .env file
and using it with python dotenv library.

12.01.2023
'''

from dotenv import load_dotenv
import os
import json


base_dir = os.path.abspath(os.path.dirname(__file__))
conf = json.loads(open(os.path.join(base_dir, "config.json"), "r").read())


def json_to_dotenv(json_dict: dict = None, json_path: str = None, out_filename: str = ".env") -> None:
    if not json_dict or not json_path:
        print("Pass json dict object or path to json file as a string!")
        return

    if not json_dict and json_path:
        # There might be a lot of errors that needs to be handled but whatever
        json_dict = json.loads(
            open(out_filename, "r", encoding="utf-8").read())

    with open(out_filename, "w", encoding="utf-8") as f:
        keys = json_dict.keys()

        for key in sorted(keys):
            value = json_dict[key]

            # Check if value is dict and convert it to string
            if type(value) is dict:
                f.write(f"{str(key)}='{json.dumps(value)}'\n")
            else:
                f.write(f"{str(key)}='{str(value)}'\n")
    print("done")


json_to_dotenv(conf, ".env")

# At this point we have all environment variables that was in json
# stored in .env file near this script in propper way.
# All keys in json becomes name of variables.
# All values of json variables becomes values of environment variables.
# All stored as string.
# To get environment variable you can use os.environ["VAR_NAME"]

load_dotenv(".env")

# At this point we have all environment variables that was in json file.
