.PHONY: all
all: muscle3

.PHONY: muscle3
muscle3: muscle3/lib/libmuscle.so

muscle3/lib/libmuscle.so:
	$(MAKE) -C muscle3_src
	PREFIX=$(CURDIR)/muscle3 $(MAKE) -C muscle3_src install

.PHONY: clean
clean:
	$(MAKE) -C muscle3_src distclean
	rm -rf muscle3

