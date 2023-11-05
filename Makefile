tracking: src/c++/tracking.cpp build/tracking
	echo "compiling files"
	g++ src/c++/tracking.cpp -I /usr/local/include/opencv4 -L /usr/local/lib/*.so.* /usr/local/lib/*.so -o ./build/tracking

plotter:
	python3 src/python/plotter.py

avg:
	python3 src/python/avg.py

pformat:
	yapf -i --style=google ./src/python/coordinate.py 

cformat:
	clang-format -i src/c++/tracking.cpp 

