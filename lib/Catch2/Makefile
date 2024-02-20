.PHONY: all
all:
	mkdir -p build
	cd build && cmake --install-prefix ${CURDIR}/catch2 ../src
	$(MAKE) -C build
	$(MAKE) -C build install

clean:
	rm -rf build
	rm -rf catch2
