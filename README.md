Документація до команд для налаштування та використання aws-credentials-sort

1. Копіювання файлу конфігурації до LaunchAgents
    cp aws-credentials-sort.plist ~/Library/LaunchAgents/
2. Перевірка наявності файлу в LaunchAgents
    ls ~/Library/LaunchAgents/
3. Завантаження та запуск служби через launchctl
    launchctl load -w -F ~/Library/LaunchAgents/aws-credentials-sort.plist
4. Перевірка статусу служби
    aunchctl list | grep aws
5. Встановлення бібліотеки boto3 через pip3
    pip3 install boto3 --break-system-packages
6. Перегляд виведення та помилок після установки
    cat /tmp/aws-credentials-sort.error
    cat /tmp/aws-credentials-sort.out
7. Створення каталогу для налаштувань AWS (якщо його немає)
    mkdir ~/.aws
8. Вивантаження служби
    launchctl unload ~/Library/LaunchAgents/aws-credentials-sort.plist
9. Повторне завантаження служби після вивантаження
    launchctl load -w -F ~/Library/LaunchAgents/aws-credentials-sort.plist
10. Налаштування профілю AWS
     export AWS_PROFILE=rbua-payments-multi-test-05
11. Перевірка доступу до S3 через AWS CLI
     aws s3 ls
12. Встановлення сертифікатів CA через Homebrew
     brew install ca-certificates
13. Встановлення AWS SAM CLI через Homebrew
     brew install aws-sam-cli
14. Завантаження та встановлення Session Manager Plugin для AWS CLI
     curl "https://s3.amazonaws.com/session-manager-downloads/plugin/latest/mac_arm64/sessionmanager-bundle.zip" -o "sessionmanager-bundle.zip"
     unzip sessionmanager-bundle.zip
     sudo ./sessionmanager-bundle/install -i /usr/local/sessionmanagerplugin -b /usr/local/bin/session-manager-plugin
     rm -rf ./sessionmanager-bundle ./sessionmanager-bundle.zip
15. Перевірка сертифікатів CA
     ls /opt/homebrew/etc/ca-certificates/cert.pem
16. Налаштування конфігурації AWS через файл ~/.aws/config
     vim ~/.aws/config
17. Встановлення змінної середовища для шляху до сертифікатів
     export AWS_CA_BUNDLE=/opt/homebrew/etc/ca-certificates/cert.pem
18. Внесення змін до файлу .zshrc для зберігання змінних середовища
     vim ~/.zshrc
19. Налаштування AWS регіону через змінні середовища
     export AWS_REGION=eu-central-1
20. Підключення до сервера з детальним відлагодженням
     ssh -vvv iuada142@i-0e8d4028dc7171181
21. Налаштування профілю AWS для сесії SSH
     export AWS_PROFILE=rbua-payments-multi-test-05
22. Налаштування конфігурації SSH
     vim ~/.ssh/config
23. Перевірка налаштування змінної середовища для AWS Profile
     echo $AWS_PROFILE

