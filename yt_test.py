from __future__ import unicode_literals
import youtube_dl
import sys
import os.path
import argparse
import subprocess

ydl_opts = {
	#'verbose': True,
	'dump_single_json': True,
	#'batchfile': 
	#'format': "720p-1",
	#'autonumber_size': 1
	#'outtmpl':
	'writethumbnail': True,
	'subtitlesformat': "srt",
	'subtitleslangs': "enUS",
	'writesubtitles': True,
	'prefer_ffmpeg': True,
	'embedsubtitles': True,
	'embedthumbnail': True
	#'postprocessor_args'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.crunchyroll.com/is-the-order-a-rabbit/episode-1-i-knew-at-first-glance-that-it-was-no-ordinary-fluffball-653243'])