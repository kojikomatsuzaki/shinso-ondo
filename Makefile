.PHONY: serve metadata verify write pages

serve:
	python3 -m http.server 8000

metadata:
	python tools/update_audio_metadata.py

verify:
	python tools/update_audio_metadata.py --verify

write:
	python tools/update_audio_metadata.py --write

pages:
	# 将来 Pages を生成するコマンド
