from __future__ import unicode_literals
import youtube_dl
import sys
import os.path
import argparse
import subprocess

ydl_opts = {
	'verbose': True,
	#'simulate': True,
	#'dump_single_json': True,
	#'batchfile': 
	#'format': "720p-1",
	#'autonumber_size': 1
	#'outtmpl':
	#'writethumbnail': True,
	#'embedthumbnail': True,
	#'listsubtitles': True,
	'writesubtitles': True,
	'subtitlesformat': "srt",
	'allsubtitles': True,
	#'subtitleslangs': "en",
	'prefer_ffmpeg': True,
	'embedsubtitles': True,
	#'postprocessor_args'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	 info_dict = ydl.extract_info("http://www.crunchyroll.com/is-the-order-a-rabbit/episode-1-i-knew-at-first-glance-that-it-was-no-ordinary-fluffball-653243", download=False)
	 print(info_dict.re)
	 ##SUbtitle information and all the other stuff can be extracted from the dictionary given the chanche
	  
	#ydl.list_subtitles("http://www.crunchyroll.com/is-the-order-a-rabbit/episode-1-i-knew-at-first-glance-that-it-was-no-ordinary-fluffball-653243")
   #ydl.download(['http://www.crunchyroll.com/is-the-order-a-rabbit/episode-1-i-knew-at-first-glance-that-it-was-no-ordinary-fluffball-653243'])