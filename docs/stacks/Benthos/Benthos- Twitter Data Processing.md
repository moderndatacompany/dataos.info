# Benthos- Twitter Data Processing

This use case demonstrates the creation of the Benthos service in DataOS, which can consume tweets matching a given search string using the recent Twitter search V2 API. While getting the response from API, it contains all the emojis and symbols in it, which are removed using the bloblang processor and converted to refined data of twitter which does not contain any emojis. This output can be saved into a JSON file.

## Prerequisites

Authentication is done using Oauth2 credentials generated from the Twitter API documentation. Below is the link to generate the credentials.

[https://developer.twitter.com/en](https://developer.twitter.com/en)

Here are the steps to get the Twitter data and perform modifications in the pipeline section.

### Step 1: Create Configuration YAML File

             - Define Input.

             - Define the ‘bloblang’ Processor.

             - Define Output.

### Step 2: Test the Processing

Once you test the processing for the desired results, add the `service` section in the configuration YAML file to create Benthos Service in DataOS. To learn more, refer to [Benthos.](./Benthos.md)


## Create Configuration File

Create a YAML file with the following configuration properties which will fetch the Twitter data that match the given search query. For pagination, the tweet id is stored in the cache resource.

## Define Input

1. query: A search expression to use.
2. tweet_fields: [optional] a list of additional fields to obtain for each tweet, by default only the fields `id` and `text` are returned. For more info refer to the [Twitter API docs](https://developer.twitter.com/en/docs/twitter-api/fields).
3. poll_period: The duration string to wait between each search request. This field can be set empty, in which case requests are made at the limit set by the rate limit.
4. backfill_period: A duration string indicating the maximum age of tweets to acquire when starting a search.
5. cache: A cache resource to use for request pagination.
6. cache_key: The key identifier used when storing the ID of the last tweet received.
7. rate_limit: An optional rate limit resource to restrict API requests with. 
8. api_key: An API key for OAuth 2.0 authentication. 
9. api_secret: An API secret for OAuth 2.0 authentication. 

> Note: Benthos allows you to dynamically set config fields with environment variables anywhere within a config YAML file. It is recommended that you populate these API fields using [environment variables](https://www.benthos.dev/docs/configuration/interpolation).
> 

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
```

## Define the `bloblang` Processors

You will get a response in the form of each JSON object. While getting the response from API, it contained all the emojis and symbols in it, which have to be removed.

1. root: the root indicates the whole JSON object. 
2. root.match: this is to point text key in JSON object.
3. root. text: this is to remove all the emojis and symbols from the JSON response.

```yaml
pipeline:
  processors:
    - bloblang: |
          root = this
          root.match = this.text.re_find_all("\n")
          root.text = this.text.re_find_all("`[0-9#*]️?⃣|[©®‼⁉™ℹ↔-↙↩↪⌨⏏⏭-⏯⏱⏲⏸-⏺Ⓜ▪▫▶◀◻◼☀-☄☎☑☘☠☢☣☦☪☮☯☸-☺♀♂♟♠♣♥♦♨♻♾⚒⚔-⚗⚙⚛⚜⚠⚧⚰⚱⛈⛏⛑⛓⛩⛰⛱⛴⛷⛸✂✈✉✏✒✔✖✝✡✳✴❄❇❣➡⤴⤵⬅-⬇〰〽㊗㊙🅰🅱🅾🅿🈂🈷🌡🌤-🌬🌶🍽🎖🎗🎙-🎛🎞🎟🏍🏎🏔-🏟🏵🏷🐿📽🕉🕊🕯🕰🕳🕶-🕹🖇🖊-🖍🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺🛋🛍-🛏🛠-🛥🛩🛰🛳]️?|[☝✌✍🕴🖐][️🏻-🏿]?|[⛹🏋🏌🕵](?:‍[♀♂]️?|[️🏻-🏿](?:‍[♀♂]️?)?)?|[✊✋🎅🏂🏇👂👃👆-👐👦👧👫-👭👲👴-👶👸👼💃💅💏💑💪🕺🖕🖖🙌🙏🛀🛌🤌🤏🤘-🤟🤰-🤴🤶🥷🦵🦶🦻🧒🧓🧕🫃-🫅🫰🫲-🫶][🏻-🏿]?|❤(?:‍[🔥🩹]|️(?:‍[🔥🩹])?)?|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|[🏃🏄🏊👮👰👱👳👷💁💂💆💇🙅-🙇🙋🙍🙎🚣🚴-🚶🤦🤵🤷-🤹🤽🤾🦸🦹🧍-🧏🧔🧖-🧝](?:‍[♀♂]️?|[🏻-🏿](?:‍[♀♂]️?)?)?|🏳(?:‍(?:⚧️?|🌈)|️(?:‍(?:⚧️?|🌈))?)?|🏴(?:‍☠️?|󠁧󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴|󠁷󠁬󠁳)󠁿)?|🐈(?:‍⬛)?|🐕(?:‍🦺)?|🐻(?:‍❄️?)?|👁(?:‍🗨️?|️(?:‍🗨️?)?)?|👨(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|👩(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:[👨👩]|💋‍[👨👩])|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[👯🤼🧞🧟](?:‍[♀♂]️?)?|😮(?:‍💨)?|😵(?:‍💫)?|😶(?:‍🌫️?)?|🧑(?:‍(?:[⚕⚖✈]️?|🤝‍🧑|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏼-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏽-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏼🏾🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏽🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏾]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[⌚⌛⏩-⏬⏰⏳◽◾☔☕♈-♓♿⚓⚡⚪⚫⚽⚾⛄⛅⛎⛔⛪⛲⛳⛵⛺⛽✅✨❌❎❓-❕❗➕-➗➰➿⬛⬜⭐⭕🀄🃏🆎🆑-🆚🈁🈚🈯🈲-🈶🈸-🈺🉐🉑🌀-🌠🌭-🌵🌷-🍼🍾-🎄🎆-🎓🎠-🏁🏅🏆🏈🏉🏏-🏓🏠-🏰🏸-🐇🐉-🐔🐖-🐺🐼-🐾👀👄👅👑-👥👪👹-👻👽-💀💄💈-💎💐💒-💩💫-📼📿-🔽🕋-🕎🕐-🕧🖤🗻-😭😯-😴😷-🙄🙈-🙊🚀-🚢🚤-🚳🚷-🚿🛁-🛅🛐-🛒🛕-🛗🛝-🛟🛫🛬🛴-🛼🟠-🟫🟰🤍🤎🤐-🤗🤠-🤥🤧-🤯🤺🤿-🥅🥇-🥶🥸-🦴🦷🦺🦼-🧌🧐🧠-🧿🩰-🩴🩸-🩼🪀-🪆🪐-🪬🪰-🪺🫀-🫂🫐-🫙🫠-🫧]|🫱(?:🏻(?:‍🫲[🏼-🏿])?|🏼(?:‍🫲[🏻🏽-🏿])?|🏽(?:‍🫲[🏻🏼🏾🏿])?|🏾(?:‍🫲[🏻-🏽🏿])?|🏿(?:‍🫲[🏻-🏾])?)?`g")

```

## Define Output

In this, we will get the output as the refined data of twitter which does not contain any emojis.

The output can be in a file or it can be from various sources like SQL, HTTP Server, JSON, CSV, Cloud buckets, etc.

```yaml
output:
  label: ""
  file:
    path: "output/tweets.json"
    codec: lines
```

## Configuration YAML File

Here is the complete `twitter.yaml` file.

```yaml
# All config fields, showing default values
input:
  label: "getting_twitter_data"
  twitter_search:
    query: "Ukraine"
    tweet_fields: []
    poll_period: 10s
    backfill_period: 5m
    cache: shashank
    cache_key: last_tweet_id
    rate_limit: ""
    api_key: "<API KEY>"
    api_secret: "<API SECRET>"
cache_resources:
  - label: shashank
    memory:
      ttl: 300
      compaction_interval: 60s
      init_values: {}
pipeline:
  processors:
    - bloblang: |
          root = this
          #root.match = this.text.re_find_all("\n")
          #root.emoji = this.text.re_find_all("`[0-9#*]️?⃣|[©®‼⁉™ℹ↔-↙↩↪⌨⏏⏭-⏯⏱⏲⏸-⏺Ⓜ▪▫▶◀◻◼☀-☄☎☑☘☠☢☣☦☪☮☯☸-☺♀♂♟♠♣♥♦♨♻♾⚒⚔-⚗⚙⚛⚜⚠⚧⚰⚱⛈⛏⛑⛓⛩⛰⛱⛴⛷⛸✂✈✉✏✒✔✖✝✡✳✴❄❇❣➡⤴⤵⬅-⬇〰〽㊗㊙🅰🅱🅾🅿🈂🈷🌡🌤-🌬🌶🍽🎖🎗🎙-🎛🎞🎟🏍🏎🏔-🏟🏵🏷🐿📽🕉🕊🕯🕰🕳🕶-🕹🖇🖊-🖍🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺🛋🛍-🛏🛠-🛥🛩🛰🛳]️?|[☝✌✍🕴🖐][️🏻-🏿]?|[⛹🏋🏌🕵](?:‍[♀♂]️?|[️🏻-🏿](?:‍[♀♂]️?)?)?|[✊✋🎅🏂🏇👂👃👆-👐👦👧👫-👭👲👴-👶👸👼💃💅💏💑💪🕺🖕🖖🙌🙏🛀🛌🤌🤏🤘-🤟🤰-🤴🤶🥷🦵🦶🦻🧒🧓🧕🫃-🫅🫰🫲-🫶][🏻-🏿]?|❤(?:‍[🔥🩹]|️(?:‍[🔥🩹])?)?|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|[🏃🏄🏊👮👰👱👳👷💁💂💆💇🙅-🙇🙋🙍🙎🚣🚴-🚶🤦🤵🤷-🤹🤽🤾🦸🦹🧍-🧏🧔🧖-🧝](?:‍[♀♂]️?|[🏻-🏿](?:‍[♀♂]️?)?)?|🏳(?:‍(?:⚧️?|🌈)|️(?:‍(?:⚧️?|🌈))?)?|🏴(?:‍☠️?|󠁧󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴|󠁷󠁬󠁳)󠁿)?|🐈(?:‍⬛)?|🐕(?:‍🦺)?|🐻(?:‍❄️?)?|👁(?:‍🗨️?|️(?:‍🗨️?)?)?|👨(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|👩(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:[👨👩]|💋‍[👨👩])|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[👯🤼🧞🧟](?:‍[♀♂]️?)?|😮(?:‍💨)?|😵(?:‍💫)?|😶(?:‍🌫️?)?|🧑(?:‍(?:[⚕⚖✈]️?|🤝‍🧑|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏼-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏽-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏼🏾🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏽🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏾]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[⌚⌛⏩-⏬⏰⏳◽◾☔☕♈-♓♿⚓⚡⚪⚫⚽⚾⛄⛅⛎⛔⛪⛲⛳⛵⛺⛽✅✨❌❎❓-❕❗➕-➗➰➿⬛⬜⭐⭕🀄🃏🆎🆑-🆚🈁🈚🈯🈲-🈶🈸-🈺🉐🉑🌀-🌠🌭-🌵🌷-🍼🍾-🎄🎆-🎓🎠-🏁🏅🏆🏈🏉🏏-🏓🏠-🏰🏸-🐇🐉-🐔🐖-🐺🐼-🐾👀👄👅👑-👥👪👹-👻👽-💀💄💈-💎💐💒-💩💫-📼📿-🔽🕋-🕎🕐-🕧🖤🗻-😭😯-😴😷-🙄🙈-🙊🚀-🚢🚤-🚳🚷-🚿🛁-🛅🛐-🛒🛕-🛗🛝-🛟🛫🛬🛴-🛼🟠-🟫🟰🤍🤎🤐-🤗🤠-🤥🤧-🤯🤺🤿-🥅🥇-🥶🥸-🦴🦷🦺🦼-🧌🧐🧠-🧿🩰-🩴🩸-🩼🪀-🪆🪐-🪬🪰-🪺🫀-🫂🫐-🫙🫠-🫧]|🫱(?:🏻(?:‍🫲[🏼-🏿])?|🏼(?:‍🫲[🏻🏽-🏿])?|🏽(?:‍🫲[🏻🏼🏾🏿])?|🏾(?:‍🫲[🏻-🏽🏿])?|🏿(?:‍🫲[🏻-🏾])?)?`g")
          root.text = this.text.re_replace("`[^\n*]|[0-9#*]️?⃣|[©®‼⁉™ℹ↔-↙↩↪⌨⏏⏭-⏯⏱⏲⏸-⏺Ⓜ▪▫▶◀◻◼☀-☄☎☑☘☠☢☣☦☪☮☯☸-☺♀♂♟♠♣♥♦♨♻♾⚒⚔-⚗⚙⚛⚜⚠⚧⚰⚱⛈⛏⛑⛓⛩⛰⛱⛴⛷⛸✂✈✉✏✒✔✖✝✡✳✴❄❇❣➡⤴⤵⬅-⬇〰〽㊗㊙🅰🅱🅾🅿🈂🈷🌡🌤-🌬🌶🍽🎖🎗🎙-🎛🎞🎟🏍🏎🏔-🏟🏵🏷🐿📽🕉🕊🕯🕰🕳🕶-🕹🖇🖊-🖍🖥🖨🖱🖲🖼🗂-🗄🗑-🗓🗜-🗞🗡🗣🗨🗯🗳🗺🛋🛍-🛏🛠-🛥🛩🛰🛳]️?|[☝✌✍🕴🖐][️🏻-🏿]?|[⛹🏋🏌🕵](?:‍[♀♂]️?|[️🏻-🏿](?:‍[♀♂]️?)?)?|[✊✋🎅🏂🏇👂👃👆-👐👦👧👫-👭👲👴-👶👸👼💃💅💏💑💪🕺🖕🖖🙌🙏🛀🛌🤌🤏🤘-🤟🤰-🤴🤶🥷🦵🦶🦻🧒🧓🧕🫃-🫅🫰🫲-🫶][🏻-🏿]?|❤(?:‍[🔥🩹]|️(?:‍[🔥🩹])?)?|🇦[🇨-🇬🇮🇱🇲🇴🇶-🇺🇼🇽🇿]|🇧[🇦🇧🇩-🇯🇱-🇴🇶-🇹🇻🇼🇾🇿]|🇨[🇦🇨🇩🇫-🇮🇰-🇵🇷🇺-🇿]|🇩[🇪🇬🇯🇰🇲🇴🇿]|🇪[🇦🇨🇪🇬🇭🇷-🇺]|🇫[🇮-🇰🇲🇴🇷]|🇬[🇦🇧🇩-🇮🇱-🇳🇵-🇺🇼🇾]|🇭[🇰🇲🇳🇷🇹🇺]|🇮[🇨-🇪🇱-🇴🇶-🇹]|🇯[🇪🇲🇴🇵]|🇰[🇪🇬-🇮🇲🇳🇵🇷🇼🇾🇿]|🇱[🇦-🇨🇮🇰🇷-🇻🇾]|🇲[🇦🇨-🇭🇰-🇿]|🇳[🇦🇨🇪-🇬🇮🇱🇴🇵🇷🇺🇿]|🇴🇲|🇵[🇦🇪-🇭🇰-🇳🇷-🇹🇼🇾]|🇶🇦|🇷[🇪🇴🇸🇺🇼]|🇸[🇦-🇪🇬-🇴🇷-🇹🇻🇽-🇿]|🇹[🇦🇨🇩🇫-🇭🇯-🇴🇷🇹🇻🇼🇿]|🇺[🇦🇬🇲🇳🇸🇾🇿]|🇻[🇦🇨🇪🇬🇮🇳🇺]|🇼[🇫🇸]|🇽🇰|🇾[🇪🇹]|🇿[🇦🇲🇼]|[🏃🏄🏊👮👰👱👳👷💁💂💆💇🙅-🙇🙋🙍🙎🚣🚴-🚶🤦🤵🤷-🤹🤽🤾🦸🦹🧍-🧏🧔🧖-🧝](?:‍[♀♂]️?|[🏻-🏿](?:‍[♀♂]️?)?)?|🏳(?:‍(?:⚧️?|🌈)|️(?:‍(?:⚧️?|🌈))?)?|🏴(?:‍☠️?|󠁧󠁢(?:󠁥󠁮󠁧|󠁳󠁣󠁴|󠁷󠁬󠁳)󠁿)?|🐈(?:‍⬛)?|🐕(?:‍🦺)?|🐻(?:‍❄️?)?|👁(?:‍🗨️?|️(?:‍🗨️?)?)?|👨(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨|👦(?:‍👦)?|👧(?:‍[👦👧])?|[👨👩]‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?👨[🏻-🏿]|🤝‍👨[🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|👩(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:[👨👩]|💋‍[👨👩])|👦(?:‍👦)?|👧(?:‍[👦👧])?|👩‍(?:👦(?:‍👦)?|👧(?:‍[👦👧])?)|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏼-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏽-🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻🏼🏾🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏽🏿]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?[👨👩][🏻-🏿]|🤝‍[👨👩][🏻-🏾]|[🌾🍳🍼🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[👯🤼🧞🧟](?:‍[♀♂]️?)?|😮(?:‍💨)?|😵(?:‍💫)?|😶(?:‍🌫️?)?|🧑(?:‍(?:[⚕⚖✈]️?|🤝‍🧑|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽])|🏻(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏼-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏼(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏽-🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏽(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻🏼🏾🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏾(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏽🏿]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?|🏿(?:‍(?:[⚕⚖✈]️?|❤️?‍(?:💋‍)?🧑[🏻-🏾]|🤝‍🧑[🏻-🏿]|[🌾🍳🍼🎄🎓🎤🎨🏫🏭💻💼🔧🔬🚀🚒🦯-🦳🦼🦽]))?)?|[⌚⌛⏩-⏬⏰⏳◽◾☔☕♈-♓♿⚓⚡⚪⚫⚽⚾⛄⛅⛎⛔⛪⛲⛳⛵⛺⛽✅✨❌❎❓-❕❗➕-➗➰➿⬛⬜⭐⭕🀄🃏🆎🆑-🆚🈁🈚🈯🈲-🈶🈸-🈺🉐🉑🌀-🌠🌭-🌵🌷-🍼🍾-🎄🎆-🎓🎠-🏁🏅🏆🏈🏉🏏-🏓🏠-🏰🏸-🐇🐉-🐔🐖-🐺🐼-🐾👀👄👅👑-👥👪👹-👻👽-💀💄💈-💎💐💒-💩💫-📼📿-🔽🕋-🕎🕐-🕧🖤🗻-😭😯-😴😷-🙄🙈-🙊🚀-🚢🚤-🚳🚷-🚿🛁-🛅🛐-🛒🛕-🛗🛝-🛟🛫🛬🛴-🛼🟠-🟫🟰🤍🤎🤐-🤗🤠-🤥🤧-🤯🤺🤿-🥅🥇-🥶🥸-🦴🦷🦺🦼-🧌🧐🧠-🧿🩰-🩴🩸-🩼🪀-🪆🪐-🪬🪰-🪺🫀-🫂🫐-🫙🫠-🫧]|🫱(?:🏻(?:‍🫲[🏼-🏿])?|🏼(?:‍🫲[🏻🏽-🏿])?|🏽(?:‍🫲[🏻🏼🏾🏿])?|🏾(?:‍🫲[🏻-🏽🏿])?|🏿(?:‍🫲[🏻-🏾])?)?`g","")
output:
  label: ""
  file:
    path: "output/tweets_covid_v8.json"
    codec: lines
```

## Test Processing

You can run this configuration YAML file on your local machine to test the processing steps for the desired output.

Use the following command:

```yaml
benthos -c path_of_file/filename.yaml
```

API response before applying processor:

```yaml
{"id":"1494608923936292864","text":"@PriapusIQ US media. Russia to start a nuclear war with Ukraine 🇺🇦, how could a country do this to another.."}
```

API response after applying processor:

```yaml
{"id":"1494608923936292864","text":"@PriapusIQ US media. Russia to start a nuclear war with Ukraine, how could a country do this to another.."}
```