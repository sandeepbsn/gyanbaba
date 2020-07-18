import datetime 


def modal_scheduler():
	curr_date = datetime.datetime.now().date()

	hours = []
		
	for i in range(0,24):
		if i < 10:
			text = "0"+str(i)
		else:
			text = str(i)

		block = {
			"text": {
				"type": "plain_text",
				"text": text,
				"emoji": True
			},
			"value": text
		}

		hours.append(block)

	minutes = []

	for i in range(0,60):
		if i < 10:
			text = "0"+str(i)
		else:
			text = str(i)
		block = {
			"text": {
				"type": "plain_text",
				"text": text,
				"emoji": True
			},
			"value": text
		}

		minutes.append(block)

	modal_response = {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": "GyanBaba",
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
				"block_id": "message",
				"element": {
					"type": "plain_text_input",
					"multiline": True,
					"action_id": "text"
				},
				"label": {
					"type": "plain_text",
					"text": "Write your message",
					"emoji": True
				}
			},
			{
				"type": "section",
				"block_id": "date_sched",
				"text": {
					"type": "mrkdwn",
					"text": "Date to schedule"
				},
				"accessory": {
					"type": "datepicker",
					"initial_date": str(curr_date),
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					}
				}
			},
			{
				"type": "section",
				"block_id": "hours",
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
					"options": hours
				}
			},
			{
				"type": "section",
				"block_id": "minutes",
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
					"options": minutes
				}
			},
			{
				"type": "section",
				"block_id": "repeat",
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
				"block_id": "date_end",
				"text": {
					"type": "mrkdwn",
					"text": "Date to end scheduling"
				},
				"accessory": {
					"type": "datepicker",
					"initial_date": str(curr_date),
					"placeholder": {
						"type": "plain_text",
						"text": "Select a date",
						"emoji": True
					}
				}
			},
			{
				"type": "input",
				"block_id":"channels",
				"element": {
					"type": "multi_channels_select",
					"action_id": "name",
					"placeholder": {
						"type": "plain_text",
						"text": "Select channels",
						"emoji": True
					}
				},
				"label": {
					"type": "plain_text",
					"text": "Channels",
					"emoji": True
				}
			}
		]
	}

	return modal_response


def modal_pin():
	pin_response = {
		"type": "modal",
		"title": {
			"type": "plain_text",
			"text": "GyanBaba",
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
				"block_id": "keyword",
				"element": {
					"type": "plain_text_input",
					"action_id": "search_text"
				},
				"label": {
					"type": "plain_text",
					"text": "Search keyword",
					"emoji": True
				}
			},
			{
				"type": "section",
				"block_id": "pin_channels",
				"text": {
					"type": "mrkdwn",
					"text": "Pin items from channel"
				},
				"accessory": {
					"type": "channels_select",
					"placeholder": {
						"type": "plain_text",
						"text": "Select a channel",
						"emoji": True
					}
				}
			}
		]
	}

	return pin_response
