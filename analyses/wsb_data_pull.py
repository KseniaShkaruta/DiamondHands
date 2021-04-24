import requests
from datetime import datetime
import traceback
import time
import json, csv
import sys

username = ""  # put the username you want to download in the quotes
subreddit = "WallStreetBets"  # put the subreddit you want to download in the quotes
# leave either one blank to download an entire user's or subreddit's history
# or fill in both to download a specific users history from a specific subreddit

filter_string = None
if username == "" and subreddit == "":
	print("Fill in either username or subreddit")
	sys.exit(0)
elif username == "" and subreddit != "":
	filter_string = f"subreddit={subreddit}"
elif username != "" and subreddit == "":
	filter_string = f"author={username}"
else:
	filter_string = f"author={username}&subreddit={subreddit}"

url = "https://api.pushshift.io/reddit/{}/search?limit=1000&sort=desc&{}&before="

start_time = datetime.utcnow()


def downloadFromUrl(filename, object_type):
	print(f"Saving {object_type}s to {filename}")

	count = 0
	handle = open(filename, 'w', newline = '', encoding='utf-8')
	writer = csv.writer(handle)
	header = ['author', 'timestamp', 'id', 'score', 'text', 'link_id', 'parent_id']
	writer.writerow(header)
	previous_epoch = int(start_time.timestamp())
	for i in range(10000):
		new_url = url.format(object_type, filter_string)+str(previous_epoch)
		json_text = requests.get(new_url, headers={'User-Agent': "Post downloader by /u/Watchful1"})
		time.sleep(1)  # pushshift has a rate limit, if we send requests too fast it will start returning error messages
		try:
			json_data = json_text.json()
		except json.decoder.JSONDecodeError:
			time.sleep(1)
			continue
		if 'data' not in json_data:
			break
		objects = json_data['data']
		if len(objects) == 0:
			break

		for object in objects:
			previous_epoch = object['created_utc'] - 1
			count += 1
			if object_type == 'comment':
				try:
					score = str(object['score'])
					# print(object)
					timestamp = datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d, %H:%M:%S")
					body = object['body']#.encode(encoding='ascii', errors='ignore').decode()
					comment_id = object['id']#.encode(encoding='ascii', errors='ignore')
					author = object['author']#.encode(encoding='ascii', errors='ignore')
					parent_id = object['parent_id']
					link_id = object['link_id']
					writer.writerow([author, timestamp, comment_id, score, body, parent_id, link_id])
				except Exception as err:
					print(f"Couldn't print comment: https://www.reddit.com{object['permalink']}")
					print(traceback.format_exc())
			elif object_type == 'submission':
				if object['is_self']:
					if 'selftext' not in object:
						continue
					try:
						score = str(object['score'])
						timestamp = datetime.fromtimestamp(object['created_utc']).strftime("%Y-%m-%d, %H:%M:%S")
						body = object['selftext']#.encode(encoding='ascii', errors='ignore').decode()
						comment_id = object['id']#.encode(encoding='ascii', errors='ignore')
						author = object['author']#.encode(encoding='ascii', errors='ignore')
						writer.writerow([author, timestamp, comment_id, score, body, '', ''])
					except Exception as err:
						print(f"Couldn't print post: {object['url']}")
						print(traceback.format_exc())

		print("Saved {} {}s through {}".format(count, object_type, datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))

	print(f"Saved {count} {object_type}s")
	handle.close()


downloadFromUrl("posts.csv", "submission")
downloadFromUrl("comments.csv", "comment")
