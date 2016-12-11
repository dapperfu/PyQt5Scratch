.PHONY: gui
gui: qtscratch.ui
	pyuic5 qtscratch.ui -o qtscratch.py
