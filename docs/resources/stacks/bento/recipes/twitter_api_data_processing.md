# Twitter

To bring Twitter data from the API using Bento, you can follow these steps:

## Step 1: Create a Twitter developer account

To access the Twitter API, you need to create a developer account with Twitter. You can do so by visiting the Twitter developer portal ([https://developer.twitter.com/en/portal/dashboard](https://developer.twitter.com/en/portal/dashboard)) and following the instructions to create an account.

## Step 2: Create a Twitter application

Once you have a developer account, you need to create a Twitter application to access the API. To do this, go to the Twitter developer dashboard ([https://developer.twitter.com/en/portal/dashboard](https://developer.twitter.com/en/portal/dashboard)) and click on the "Projects & Apps" tab. Then click on the "Create App" button and follow the instructions to create an application. Make sure to note down your API key and API secret key.

## Step 3: Create a Bento configuration file

Bento is a stream processing stack that can be used to fetch data from the Twitter API. To do this, you need to create a configuration file that specifies the API endpoint, authentication credentials, and any other parameters you want to use. 

Here is an example Bento configuration file for fetching tweets from the Twitter API:

```yaml
# All config fields, showing default values
input:
  label: "getting_twitter_data"
  twitter_search:
    query: "Ukraine"
    tweet_fields: []
    poll_period: 10s
    backfill_period: 5m
    cache: twitter
    cache_key: last_tweet_id
    rate_limit: ""
    api_key: "<<API KEY>>"
    api_secret: "<<API SECRET>>"
cache_resources:
  - label: twitter
    memory:
      ttl: 300
      compaction_interval: 60s
      init_values: {}
pipeline:
  processors:
    - bloblang: |
          root = this
          root.match = this.text.re_find_all("\n")
          root.text = this.text.re_find_all("`[0-9#*]️?⃣|[©®‼⁉™ℹ↔-↙↩↪⌨⏏⏭-⏯⏱⏲⏸-⏺Ⓜ▪▫▶◀◻◼☀-☄☎☑☘☠☢☣☦☪☮☯☸-☺♀♂♟♠♣♥♦♨♻♾⚒⚔-⚗⚙⚛⚜⚠⚧⚰⚱⛈⛏⛑⛓⛩⛰⛱⛴⛷⛸✂✈✉✏✒✔✖✝✡✳✴❄❇❣➡⤴⤵⬅-⬇〰〽㊗㊙🅰🅱🅾🅿🈂🈷🌡🌤-🌬🌶🍽🎖🎗🎙-🎛🎞🎟🏍🏎🏔-🏟🏵🏷🐿📽🕉🕊🕯🕰🕳🕶-🕹🖇🖊-🖍🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺🛋🛍-🛏🛠-🛥🛩🛰🛳]️?|[☝✌✍🕴🖐][️🏻-🏿]?|[⛹🏋🏌🕵](?:‍[♀♂]️?|[️🏻-🏿](?:‍[♀♂]️?)?)?|[✊✋🎅🏂🏇👂👃👆-👐👦👧👫-👭👲👴-👶👸👼💃💅💏💑💪🕺🖕🖖🙌🙏🛀🛌🤌🤏🤘-🤟🤰-🤴🤶🥷🦵🦶🦻🧒🧓🧕🫃-🫅🫰🫲-🫶][🏻-🏿]?|❤(?:‍[🔥🩹]|️(?:‍[🔥🩹])?)?|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|[🏃🏄🏊👮👰👱👳👷💁💂💆💇🙅-🙇🙋🙍🙎🚣🚴-🚶🤦🤵🤷-🤹🤽🤾🦸🦹🧍-🧏🧔🧖-🧝](?:‍[♀♂]️?|[🏻-🏿](?:‍[♀♂]️?)?)?|🏳(?:‍(?:⚧️?|🌈)|️(?:‍(?:⚧️?|🌈))?)?|🏴(?:‍☠️?|󠁧󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴|󠁷󠁬󠁳)󠁿)?|🐈(?:‍⬛)?|🐕(?:‍🦺)?|🐻(?:‍❄️?)?|👁(?:‍🗨️?|️(?:‍🗨️?)?)?|👨(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|👩(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:[👨👩]|💋‍[👨👩])|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[👯🤼🧞🧟](?:‍[♀♂]️?)?|😮(?:‍💨)?|😵(?:‍💫)?|😶(?:‍🌫️?)?|🧑(?:‍(?:[⚕⚖✈]️?|🤝‍🧑|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏼-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏽-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏼🏾🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏽🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏾]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[⌚⌛⏩-⏬⏰⏳◽◾☔☕♈-♓♿⚓⚡⚪⚫⚽⚾⛄⛅⛎⛔⛪⛲⛳⛵⛺⛽✅✨❌❎❓-❕❗➕-➗➰➿⬛⬜⭐⭕🀄🃏🆎🆑-🆚🈁🈚🈯🈲-🈶🈸-🈺🉐🉑🌀-🌠🌭-🌵🌷-🍼🍾-🎄🎆-🎓🎠-🏁🏅🏆🏈🏉🏏-🏓🏠-🏰🏸-🐇🐉-🐔🐖-🐺🐼-🐾👀👄👅👑-👥👪👹-👻👽-💀💄💈-💎💐💒-💩💫-📼📿-🔽🕋-🕎🕐-🕧🖤🗻-😭😯-😴😷-🙄🙈-🙊🚀-🚢🚤-🚳🚷-🚿🛁-🛅🛐-🛒🛕-🛗🛝-🛟🛫🛬🛴-🛼🟠-🟫🟰🤍🤎🤐-🤗🤠-🤥🤧-🤯🤺🤿-🥅🥇-🥶🥸-🦴🦷🦺🦼-🧌🧐🧠-🧿🩰-🩴🩸-🩼🪀-🪆🪐-🪬🪰-🪺🫀-🫂🫐-🫙🫠-🫧]|🫱(?:🏻(?:‍🫲[🏼-🏿])?|🏼(?:‍🫲[🏻🏽-🏿])?|🏽(?:‍🫲[🏻🏼🏾🏿])?|🏾(?:‍🫲[🏻-🏽🏿])?|🏿(?:‍🫲[🏻-🏾])?)?`g")
output:
  label: ""
  file:
    path: "output/tweets.json"
    codec: lines
```

Replace `YOUR_API_KEY`, `YOUR_API_SECRET_KEY`, `YOUR_ACCESS_TOKEN`, and `YOUR_ACCESS_TOKEN_SECRET` with your actual authentication credentials. You can also customize the `keywords` parameter to search for specific terms or hashtags.

## Step 4: Run Bento

You can now run the configuration file you created in step 3. Open a terminal or command prompt and navigate to the directory where your configuration file is saved. Then run the following command:

```bash
bento -c config.yaml
```

Replace `config.yaml` with the filename of your configuration file. This will start Bento and fetch tweets from the Twitter API using your configuration.

### **Example**

Here's an example of an API response before and after applying the processor:

API response before applying the processor:

```json
{"id":"1494608923936292864","text":"@PriapusIQ US media. Russia to start nuclear war with Ukraine 🇺🇦, how could a country do this to another.."}
```

API response after applying the processor:

```json
{"id":"1494608923936292864","text":"@PriapusIQ US media. Russia to start nuclear war with Ukraine, how could a country do this to another.."}
```

The emoji in the original response has been removed.

That's it! You should now be able to fetch tweets from the Twitter API using Bento.