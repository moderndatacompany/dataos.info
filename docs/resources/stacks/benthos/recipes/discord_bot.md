# Discord Bot

Creating a Discord bot using Benthos can be done in just a few simple steps:

## Step 1: Create a new Discord application

Go to the Discord Developer [Portal](https://discord.com/developers/applications) and create a new application. Give your application a name and click "Create". Then, go to the "Bot" tab and click "Add Bot" to create a new bot for your application.

## Step 2: Obtain your bot token

On the "Bot" tab of your application, you can find your bot's token. This token will be used to authenticate your bot with the Discord API. Copy the token and keep it secure, as it will be used in the next step.

## Step 3: Configure your Benthos bot

Create a new Benthos configuration file (e.g., "bot.yaml") and add the following configuration:

```yaml
input:
  discord:
    poll_period: 3s
    channel_id: ${DISCORD_CHANNEL}
    bot_token: ${DISCORD_BOT_TOKEN}
    cache: request_tracking
    limit: 10

cache_resources:
  - label: request_tracking
    file:
      directory: /tmp/discord_bot

pipeline:
  processors:
    - mapping: |
        root = if !this.content.has_prefix("SHOUTS BACK") {
          "SHOUTS BACK BOT SAYS " + this.content.uppercase()
        } else {
          deleted()
        }

output:
  discord:
    channel_id: ${DISCORD_CHANNEL}
    bot_token: ${DISCORD_BOT_TOKEN}
```

Replace `${DISCORD_BOT_TOKEN}` with the bot token you obtained in Step 2 and `${DISCORD_CHANNEL}` with the ID of the Discord channel where you want your bot to post messages. You can obtain the channel ID by right-clicking on the channel and selecting "Copy ID".

## Step 4: Start your Benthos bot

Open a terminal and run the following command to start your Benthos bot:

```bash
benthos -c bot.yaml
```

This will start the Benthos server and connect it to the Discord API using your bot token. Your bot should now be up and running, ready to post messages to your designated channel.

## Step 5: Add commands and functionality to your bot

Now that your bot is connected to the Discord API, you can add commands and functionality using Benthos. For example, you can use the `http_server` input to create an HTTP server that listens for commands, or you can use the `slack` output to send messages to a Slack channel. 

That's it! You have now successfully created a Discord bot using Benthos. With just a few lines of configuration, you can have a powerful and flexible bot that can interact with the Discord API in a variety of ways.