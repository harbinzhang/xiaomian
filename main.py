from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence, detect_silence
import time
import collections

kSTEP = 50
kSONG_MIN_LENGTH = 7000		# min length of song
kSONG_INTERVAL = 400		# length of spliting chunks
kSONG_THRESHOLD = 700		# max distance for concat

def main():
	HandleSound("wo_yao_chuan_yue")

def HandleSound(name):
	filename = name + ".mp3"

	print("loading sound...")
	start_time = time.time()
	sound = AudioSegment.from_mp3("mp3_source/new/{}".format(filename))
	# sound = AudioSegment.from_mp3("wo_yao_chuan_yue.mp3")
	print("sound loaded in {}".format(time.time() - start_time))

	start_time = time.time()
	print("detect_silence...")
	# chunks = detect_silence(sound[:10000], min_silence_len=200, silence_thresh=-40)
	chunks = detect_silence(sound, min_silence_len=60, silence_thresh=-30)
	# sound.compress_dynamic_range()
	print("detect_silence done in {}".format(time.time() - start_time))

	last = 0
	cnt = 0
	print(len(chunks))
	print("iterate chunks...")
	start_time = time.time()
	song_time_blocks = collections.deque()
	for chunk in chunks:
		# play(sound[chunk[0]: chunk[1]])
		# print(chunk) 
		if chunk[0] - last > kSONG_INTERVAL:
			# play(sound[last: chunk[0]])
			# deque.append([last, chunk[0]])
			cnt+=1
			AppendOrCompressSong(song_time_blocks, [last, chunk[0]])
		# time.sleep(1)
		# input('c')
		last = chunk[1]
	# print(song_time_blocks)
	print("iteration done in {}".format(time.time() - start_time))
	print("Found {} song_blocks with cnt={}".format(len(song_time_blocks),cnt))

	print("GetSoundWithoutSong...")
	start_time = time.time()
	soundWithoutSong, song = GetSoundWithoutSong(sound, song_time_blocks)
	print("GetSoundWithoutSong done in {}".format(time.time() - start_time))

	print("Exporting to SoundWithoutSong")
	start_time = time.time()
	output_name = name + "_out.mp3"
	soundWithoutSong.export("sound_without_song/new/{}".format(output_name), format="mp3")
	print("Export to SoundWithoutSong done in {}".format(time.time() - start_time))

	print("Exporting to song")
	start_time = time.time()
	song_name = name + "_song.mp3"
	song.export("sound_without_song/new/{}".format(song_name), format="mp3")
	print("Export to song done in {}".format(time.time() - start_time))


def GetSoundWithoutSong(sound, song_time_blocks):
	if song_time_blocks[-1][1] - song_time_blocks[-1][0] < kSONG_MIN_LENGTH:
		song_time_blocks.pop()

	res = sound[0]
	song = sound[0]
	last = 0
	for block in song_time_blocks:
		print("Add time {} to {} to output sound".format(last, block[0]))
		res += sound[last:block[0]]
		song += sound[block[0]:block[1]]
		last = block[1]
		# play(sound[block[0]:block[1]])
	res += sound[last:]
	return res, song

# compress audio block if it closes to the previous one in queue,
# otherwise simpily append it.
def AppendOrCompressSong(deque, item):
	if len(deque) == 0:
		deque.append(item)

	last = deque[-1]
	if item[0] - last[1] < kSONG_THRESHOLD:
		deque[-1][1] = item[1]
	else:
		if deque[-1][1] - deque[-1][0] < kSONG_MIN_LENGTH:
			deque.pop()
		deque.append(item)


def CountByRms(stat, k, v): 
	if k not in stat:
		stat[k] = 0
	stat[k] = stat[k] + v

if __name__ == "__main__":
    main()

