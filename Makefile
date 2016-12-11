.PHONY: window
window: mainwindow_test.ui
	pyuic5 mainwindow_test.ui -o mainwindow_test.py

.PHONY: dialog
dialog: dialog_test.ui
	pyuic5 dialog_test.ui -o dialog_test.py

