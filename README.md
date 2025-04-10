Документація до команд для налаштування та використання aws-credentials-sort

# Install aws-credentials-sort:

1. Clone the repo
   ```
   git clone https://github.com/dim-on-github/aws-credentials-sort.git 
   cd aws-credentials-sort
   ```
2. Link required files to folders
   ```
    ln -s aws-credentials-sort.plist ~/Library/LaunchAgents/
    ln -s ${PWD}/aws-credentials-sort.py ${HOME}/.local/bin/aws-credentials-sort.py
   ```
3. Створення каталогу для налаштувань AWS (якщо його немає)
   ```
    mkdir ~/.aws
   ```
4. Встановлення бібліотеки boto3 через pip3
   ```
    /usr/bin/pip3 install boto3 --break-system-packages
   ```
5. Allow access to disk in Mac OS in System Settings > Privacy & Security > Full Disk Access
    - Add /bin/sh
6. Завантаження та запуск служби через launchctl
   ```
    launchctl load -w -F ~/Library/LaunchAgents/aws-credentials-sort.plist
   ```
7. Check service status, has to be "0" in second column
   ```
    launchctl list | grep aws
   ```
8. Перегляд помилок та логу після встановлення
   ```
    cat /tmp/aws-credentials-sort.error
    cat /tmp/aws-credentials-sort.out
   ```

# Troubleshooting:

- If you made changes to aws-credentials-sort.plist file, you should reload launchctl configuration:
    ```
    launchctl unload ~/Library/LaunchAgents/aws-credentials-sort.plist ;
    launchctl load -w -F ~/Library/LaunchAgents/aws-credentials-sort.plist
    ```
- Налаштування профілю AWS
   ```
     export AWS_PROFILE=rbua-payments-multi-test-05
   ```
- Перевірка доступу до S3 через AWS CLI
   ```
     aws s3 ls
   ```
- Встановлення сертифікатів CA через Homebrew
   ```
     brew install ca-certificates
   ```
- Встановлення AWS SAM CLI через Homebrew
   ```
     brew install aws-sam-cli
   ```
- Завантаження та встановлення Session Manager Plugin для AWS CLI
   ```
     curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
     unzip sessionmanager-bundle.zip
     sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
     rm -rf ./sessionmanager-bundle ./sessionmanager-bundle.zip
   ```
- Перевірка сертифікатів CA
   ```
     ls /opt/homebrew/etc/ca-certificates/cert.pem
   ```
- Налаштування конфігурації AWS через файл ~/.aws/config
   ```
     vim ~/.aws/config
   ```
- Встановлення змінної середовища для шляху до сертифікатів
   ```
     echo "export AWS_CA_BUNDLE=/opt/homebrew/etc/ca-certificates/cert.pem" >> ~/.zshrc
   ```
- Налаштування AWS регіону через змінні середовища
   ```
     export AWS_REGION=eu-central-1
   ```
- Підключення до сервера з детальним відлагодженням
   ```
     ssh -vvv iuada142@i-0e8d4028dc7171181
   ```
- Налаштування профілю AWS для сесії SSH
   ```
     export AWS_PROFILE=rbua-payments-multi-test-05
   ```
- Налаштування конфігурації SSH
   ```
     vim ~/.ssh/config #TODO ????
   ```
- Перевірка налаштування змінної середовища для AWS Profile
   ```
     echo $AWS_PROFILE
   ```
