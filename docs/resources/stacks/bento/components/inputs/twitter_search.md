# twitter_search

> 🗣 EXPERIMENTAL
This component is experimental and, therefore subject to change or removal outside of major version releases.

Consumes tweets matching a given search using the Twitter recent search V2 API.

## YAML Configurations

### Common Config

```yaml
# Common config fields, showing default values
input:
  label: ""
  twitter_search:
    query: ""
    tweet_fields: []
    poll_period: 1m
    backfill_period: 5m
    cache: ""
    api_key: ""
    api_secret: ""
```

Continuously polls the [Twitter recent search V2 API](https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-recent) for tweets that match a given search query.

Each tweet received is emitted as a JSON object message with a field `id` and `text` by default. Extra fields [can be obtained from the search API](https://developer.twitter.com/en/docs/twitter-api/fields) when listed with the `tweet_fields` field.

In order to paginate requests that are made, the ID of the latest received tweet is stored in a cache resource, which is then used by subsequent requests to ensure only tweets after it are consumed. It is recommended that the cache you use is persistent so that Bento can resume searches at the correct place on a restart.

Authentication is done using OAuth 2.0 credentials which can be generated within the [Twitter developer portal](https://developer.twitter.com/).

## Fields

### `query`

A search expression to use.

Type: `string`

---

### `tweet_fields`

An optional list of additional fields to obtain for each tweet, by default, only the fields `id` and `text` are returned. For more info, refer to the [twitter API docs.](https://developer.twitter.com/en/docs/twitter-api/fields)

Type: `array`

Default: `[]`

---

### `poll_period`

The length of time (as a duration string) to wait between each search request. This field can be set empty, in which case requests are made at the limit set by the rate limit. This field also supports cron expressions.

Type: `string`

Default: `"1m"`

---

### `backfill_period`

A duration string indicating the maximum age of tweets to acquire when starting a search.

Type: `string`

Default: `"5m"`

---

### `cache`

A cache resource to use for request pagination.

Type: `string`

---

### `cache_key`

The key identifier used when storing the ID of the last tweet received.

Type: `string`

Default: `"last_tweet_id"`

---

### `rate_limit`

An optional rate limit resource to restrict API requests with.

Type: `string`

Default: `""`

---

### `api_key`

An API key for OAuth 2.0 authentication. It is recommended that you populate this field using environment variables.

Type: `string`

---

### `api_secret`

An API secret for OAuth 2.0 authentication. It is recommended that you populate this field using environment variables.

Type: `string`