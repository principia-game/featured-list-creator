import json
import struct
from pathlib import Path

def u32(data):
	if not 0 <= data <= 4294967295:
		print("u32 out of range: %s" % data, "INFO")
		data = 0
	return struct.pack("<I", data)

def main():
	data = json.loads(open(Path("data/data.json"), "r").read())

	if len(data['featured_levels']) > 4:
		raise ValueError("Principia only supports up to 4 featured levels at once.")
	if len(data['gettingstarted_list'])  > 12:
		raise ValueError("Principia can, at best, only fit up to 12 getting started links at once.")

	with open('fl.cache', 'wb+') as f:
		f.write(u32(len(data['featured_levels'])))		# featured_level_count
		for feat_level in data['featured_levels']:
			with open(Path(feat_level['jpeg_image']), "rb") as jpeg_file:
				jpeg_stream = jpeg_file.read()

			f.write(u32(feat_level['id']))				# fl_id
			f.write(u32(len(feat_level['name'])))		# fl_name_size
			f.write(feat_level['name'].encode())		# fl_name
			f.write(u32(len(feat_level['author'])))		# fl_author_size
			f.write(feat_level['author'].encode())		# fl_author
			f.write(u32(len(jpeg_stream)))				# fl_jpegstream_size
			f.write(jpeg_stream)						# fl_jpegstream

		f.write(u32(0))									# unknown_7ef28c
		f.write(u32(len(data['gettingstarted_list'])))	# gettingstarted_list_count
		for gettingstarted in data['gettingstarted_list']:
			f.write(u32(len(gettingstarted['name'])))	# gs_name_size
			f.write(gettingstarted['name'].encode())	# gs_name
			f.write(u32(len(gettingstarted['link'])))	# gs_link_size
			f.write(gettingstarted['link'].encode())	# gs_link

if __name__ == "__main__":
	main()