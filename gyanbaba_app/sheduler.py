modal_response = {
	"type": "modal",
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True
			},
			"label": {
				"type": "plain_text",
				"text": "Write your message",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Date to schedule"
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hours"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select hours",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Minutes"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select Minutes",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Repeat"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select repeat pattern",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "*this is plain_text text*",
							"emoji": True
						},
						"value": "value-2"
					}
				]
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Date to end scheduling"
			},
			"accessory": {
				"type": "datepicker",
				"initial_date": "1990-04-28",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a date",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select channels (optional)"
			},
			"accessory": {
				"type": "channels_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a channels",
					"emoji": True
				}
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Select users (optional)"
			},
			"accessory": {
				"type": "users_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a user",
					"emoji": True
				}
			}
		}
	]
}