.PHONY: first
first: MyFirstQtDesignerApp.ipynb mainwindow_test.py
	jupyter nbconvert --to=python MyFirstQtDesignerApp.ipynb
	python3 MyFirstQtDesignerApp.py

.PHONY: designer
designer:
	designer *.ui &

mainwindow_test.py: mainwindow_test.ui
	pyuic5 mainwindow_test.ui -o mainwindow_test.py

dialog_test.py: dialog_test.ui
	pyuic5 dialog_test.ui -o dialog_test.py
