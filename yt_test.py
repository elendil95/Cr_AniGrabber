from __future__ import unicode_literals
import youtube_dl
import sys
import os.path
import argparse
import subprocess

ydl_opts = {
	'verbose': True,
	'dump_single_json': True
	#'batchfile': 
	'format': "720p-1"
	#'autonumber_size': 1
	'outtmpl':
	'writethumbnail': True
	'subtitlesformat': "srt"
	'subtitleslangs': "enUS"
	'writesubtitles': True
	'prefer_ffmpeg': True
	#'postprocessor_args'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.crunchyroll.com/konosuba-gods-blessing-on-this-wonderful-world/episode-1-this-self-proclaimed-goddess-and-reincarnation-in-another-world-692393'])