TESTS := test_test

RUN_COMMANDS := $(patsubst %,run_%,$(TESTS))

PKG_CONFIG_PATH=../../../$(CATCH2_BASE)/share/pkgconfig
export PKG_CONFIG_PATH

PKG_CONFIG := export PKG_CONFIG_PATH=../../../$(CATCH2_BASE)/share/pkgconfig && pkg-config

CATCH2_INCLUDES := $$(pkg-config --cflags catch2-with-main)
CATCH2_LIBS := $$(pkg-config --libs catch2-with-main)

CXXFLAGS := $(CATCH2_INCLUDES) $(CCFLAGS)
LDFLAGS := $(CATCH2_LIBS) $(LDFLAGS)


.PHONY: run_all_tests
run_all_tests: $(RUN_COMMANDS)


.PHONY: run_%
run_%: %
	./$^


test_test: test_test.cpp
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)


clean:
	rm -f $(TESTS)
