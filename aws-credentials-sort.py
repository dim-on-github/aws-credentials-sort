import configparser
import os
import re
import boto3

NEW_CREDENTIALS = "/Users/IUADA0KI/Downloads/aws_credentials"
CREDENTIALS_PATH = "/Users/IUADA0KI/.aws"


def main():

    new_config = configparser.RawConfigParser()
    new_config.read(NEW_CREDENTIALS)
    main_config = configparser.RawConfigParser()
    main_config.read(f"{CREDENTIALS_PATH}/credentials")

    credentials = {}
    for key in ("aws_access_key_id", "aws_secret_access_key", "aws_session_token"):
        credentials[key] = new_config.get("default", key)

    # print(credentials)

    iam = boto3.client("iam",
                       region_name="eu-central-1",
                       aws_access_key_id=credentials["aws_access_key_id"],
                       aws_secret_access_key=credentials["aws_secret_access_key"],
                       aws_session_token=credentials["aws_session_token"]
                       )

    account = re.search(r".+[0-9][0-9]", iam.list_account_aliases()["AccountAliases"][0]).group(0)

    print(account)

    for key in ("aws_access_key_id", "aws_secret_access_key", "aws_session_token"):
        if not main_config.has_section(account):
            main_config.add_section(account)
        main_config.set(account, key, credentials[key])

    with open(f"{CREDENTIALS_PATH}/credentials", "w") as configfile:
        main_config.write(configfile)

    os.remove(NEW_CREDENTIALS)


if __name__ == "__main__":
    if os.path.exists(NEW_CREDENTIALS):
        main()

