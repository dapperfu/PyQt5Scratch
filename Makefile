control_gui.py: control_gui.ui
	@echo "Building $? -> $@"
	pyuic5 $? -o $@
	@echo ""

.PHONY: run
run: control_gui.py
	python3 control_app.py 
