# BASIS BallsDex Discord Bot

BallsDex is a bot for collecting countryballs on Discord and exchange them with your friends!

This is a custom fork of the bot for use in a local friend group.

To run with docker use the following commands.
```bash
docker compose build
docker compose up bot
docker compose up
```

To stop the bot use `Control + C`, then run the following to make sure the bot is stopped.
```bash
docker compose down
```

To delete all containers use `docker rm $(docker ps -a -q)`

To create a terminal with sudo by default, use the following command: `sudo -i`

## License

This repository is released under the [MIT license](https://opensource.org/licenses/MIT).

If distributing this bot, credits to the original authors must not be removed.
