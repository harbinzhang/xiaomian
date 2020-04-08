from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence, detect_silence
import time
import collections

# sound = AudioSegment.from_mp3("wo.mp3")
kSTEP = 50
kSONG_INTERVAL = 3000
kSONG_THRESHOLD = 1000

def main():

	

	print("loading sound...")
	start_time = time.time()
	sound = AudioSegment.from_mp3("w.mp3")
	# sound = AudioSegment.from_mp3("wo_yao_chuan_yue.mp3")
	print("sound loaded in {}".format(time.time() - start_time))

	start_time = time.time()
	print("detect_silence...")
	# chunks = detect_silence(sound[:10000], min_silence_len=200, silence_thresh=-40)
	chunks = detect_silence(sound, min_silence_len=60, silence_thresh=-30)
	# sound.compress_dynamic_range()
	print("detect_silence done in {}".format(time.time() - start_time))

	last = 0

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
			AppendOrCompressSong(song_time_blocks, [last, chunk[0]], kSONG_THRESHOLD)
		# time.sleep(1)
		# input('c')
		last = chunk[1]
	print("iteration done in {}".format(time.time() - start_time))
	print("Found {} song_blocks".format(len(song_time_blocks)))

	print("GetSoundWithoutSong...")
	start_time = time.time()
	soundWithoutSong = GetSoundWithoutSong(sound, song_time_blocks)
	print("GetSoundWithoutSong done in {}".format(time.time() - start_time))

	# play(soundWithoutSong)

	print("Exporting to SoundWithoutSong")
	start_time = time.time()
	soundWithoutSong.export("out.mp3", format="mp3")
	print("Export to SoundWithoutSong done in {}".format(time.time() - start_time))

	# i = 0

	# sounds = []
	# stat_cnt = {}
	# stat_time = {}

	# loudness = []

	# for step in sound[::kSTEP]:
	# 	sounds.append(step)
	# 	loudness.append(step.rms)
	# 	count(stat_cnt, step.rms / 1000, 1)
	# 	# if (step.rms / 1000 >= 25): 
	# 	# 	# play(step)
	# 	# 	print(i/10)
	# 	i+=1

	# for k in stat_cnt:
	# 	print("{}: {}".format(k, stat_cnt[k]))

	# plt.plot(loudness)
	# # plt.plot([1, 2, 3, 4])
	# plt.show()

def GetSoundWithoutSong(sound, song_time_blocks):
	res = sound[0:1]
	last = 0
	for block in song_time_blocks:
		print("skip time {} to {}".format(last, block[0]))
		res += sound[last:block[0]]
		last = block[1]
	res += sound[last:]
	return res

# compress audio block if it closes to the previous one in queue,
# otherwise simpily append it.
def AppendOrCompressSong(deque, item, threshold):
	if len(deque) == 0:
		deque.append(item)

	last = deque[-1]
	if item[0] - last[1] < threshold:
		deque[-1][1] = item[1]
	else:
		deque.append(item)


def CountByRms(stat, k, v): 
	if k not in stat:
		stat[k] = 0
	stat[k] = stat[k] + v

if __name__ == "__main__":
    main()



# start = sounds[0]

# for i in range(0, 100):
# 	print("{}: {}".format(i, sounds[i].rms))
	# start += sounds[i]
	# play(sounds[i])

# normalized = start.normalize(1)
# i = 0
# for step in normalized[::kSTEP]:
# 	print("{}: {}".format(i, step.rms))
# 	i += 1

# play(normalized)

