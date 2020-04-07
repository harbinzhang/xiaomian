from pydub import AudioSegment
from pydub.playback import play
from pydub.silence import split_on_silence, detect_silence
import matplotlib.pyplot as plt
import time
import collections

# sound = AudioSegment.from_mp3("wo.mp3")
kSTEP = 50



def main():

	deque = collections.deque()

	print("loading sound...")
	start_time = time.time()
	sound = AudioSegment.from_mp3("w.mp3")
	# sound = AudioSegment.from_mp3("wo_yao_chuan_yue.mp3")
	end_time = time.time()
	print("sound loaded in {}".format(end_time - start_time))

	start_time = end_time
	print("detect_silence...")
	# chunks = detect_silence(sound[:10000], min_silence_len=200, silence_thresh=-40)
	chunks = detect_silence(sound, min_silence_len=60, silence_thresh=-30)
	# sound.compress_dynamic_range()
	end_time = time.time()
	print("detect_silence done in {}".format(end_time - start_time))

	last = 0

	print(len(chunks))
	cnt = 0
	print("iterate chunks")
	start_time = time.time()
	for chunk in chunks:
		# play(sound[chunk[0]: chunk[1]])
		# print(chunk) 
		if chunk[0] - last > 3000:
			play(sound[last: chunk[0]])
			queue.append([last, chunk[0]])
			cnt+=1
		# time.sleep(1)
		# input('c')
		last = chunk[1]
	end_time = time.time()
	print("iteration done in {}".format(end_time - start_time))
	print(cnt)
	# sound.export("wo_1.mp3", format="mp3")

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

# compress audio block if it closes to the previous one in queue,
# otherwise simpily append it.
def AppendOrCompress(queue, item, threshold):
	if queue.count() == 0:
		queue.append(item)

	last = queue[-1]
	if item[0] - last[1] == 


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

