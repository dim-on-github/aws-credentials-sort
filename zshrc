function tg-aws-profile () {
    export NEW_AWS_PROFILE=$(pwd | sed -nE 's/.+\/payments\/([a-z]+)\/(.+[0-9][0-9])-.+/rbua-payments-\1-\2/p')
    if [ -z "$AWS_PROFILE" ] && [ ! -z "$NEW_AWS_PROFILE" ]; then
        export AWS_PROFILE=${NEW_AWS_PROFILE}
    fi
    unset NEW_AWS_PROFILE

}
tg-aws-profile

function preexec () {
    tg-aws-profile
}

