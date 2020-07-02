## SERVER-SLACK_APP API

### GET `slash/joke`

#### REQUEST

```json{
    "channel_id":"XBYYSHD87"
}
```

#### RESPONSE

##### If Unique data present

```json
{
	"res_id": 8,
	"flag": true,
	"payload": {
		"alt": "Poisson distributions have no value over negative numbers",
		"title": "Poisson",
		"img_src": "https://imgs.xkcd.com/comics/poisson.jpg"
	},
	"up_votes": 5,
	"down_votes": 2
}
```

#### If no Unique data present

```json
{
	"flag": false,
	"payload": {
		"text": "NOTHING NEW FOR TODAY"
	}
}
```

---

### GET `slash/quote`

#### REQUEST

```json
{
	"channel_id": "XBYYSHD87"
}
```

#### RESPONSE

##### If Unique data present

```json
{
	"res_id": 1,
	"flag": true,
	"payload": {
		"text": "Genius is one percent inspiration and ninety-nine percent perspiration.",
		"author": "Thomas Edison"
	},
	"up_votes": 27,
	"down_votes": 6
}
```

#### If no Unique data present

```json
{
	"flag": false,
	"payload": {
		"text": "NOTHING NEW FOR TODAY"
	}
}
```

---

### GET `slash/video`

#### REQUEST

```json{
    "channel_id":"XBYYSHD87"
}
```

#### RESPONSE

##### If Unique data present

```json
{
	"res_id": 11,
	"flag": true,
	"payload": {
		"title": "15 Min Daily Yoga Routine for Beginners (Follow Along)",
		"video_url": "https://youtube.com/watch?v=s2NQhpFGIOg",
		"description": "15 Minute Daily Yoga Routine for Beginners (Follow Along) Buy ARATA's New Plant Based Grooming Products - https://www.arata.in/collections/fittuber (Special ..."
	},
	"up_votes": 12,
	"down_votes": 6
}
```

#### If no Unique data present

```json
{
	"flag": false,
	"payload": {
		"text": "NOTHING NEW FOR TODAY"
	}
}
```

---

### POST `/addvote/<res_id>`

#### REQUEST

```json{
    "user_id":"BHYUD67H",
    "vote_name":"up_votes"
}
```

#### RESPONSE

```json
{
	"res_id": 1,
	"footprint": true,
	"category_name": "quote",
	"payload": {
		"text": "Genius is one percent inspiration and ninety-nine percent perspiration.",
		"author": "Thomas Edison"
	},
	"up_votes": 28,
	"down_votes": 6
}
```

---

### GET `/load`

#### RESPONSE

```json{
    'loaded_data'
}
```
