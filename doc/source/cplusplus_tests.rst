C++ unit tests
==============

Some of the C++ code is covered by unit tests that test whether it works
correctly. These tests can be found in ``tests/`` subdirectories within
``src/``. They use the ``Catch2`` testing framework, which provides some useful
macros for structuring tests and checking results. The best way to learn about
this is to look at the existing tests' source code and the `Catch2 documentation
<https://github.com/catchorg/Catch2/blob/devel/docs/tutorial.md>`_.


Mocking
-------

There is one somewhat non-standard aspect of these tests that deserves an
explanation, and that's the mocking system. When you're testing a class or a
function ``A`` that depends on another class or function ``B``, you end up
testing the whole combined collection of functions and classes. For a unit test,
that's not what you want.

The solution to this is called mocking, which means that you replace the real
``B`` by a different class or function that has the same interface as the real
``B``  (so that ``A`` can call it) but that records what ``A`` did, and feeds it
a pre-set response. The recording in this mock class or mock function can then
be checked after calling ``A`` to make sure everything worked as expected.

In a language like Python, this replacement is easy to do because it's a dynamic
language, meaning that functions and classes are just objects that can be
replaced from the test code. In C++, functions and classes are combined together
at compile time, and cannot be changed at runtime unless you've explicitly
programmed it like this. As a result, we cannot just replace ``B`` with a mock
``B`` from the test code.


Dependency inversion
--------------------

One way to solve this is by a mechanism called dependency inversion. Instead of
writing

.. code-block:: cpp

    class B {
        public:
            g();
    };

    class A {
        public:
            f() { b_.g() };

        private:
            B b_;
    };


we do

.. code-block:: cpp

    /* Interface for B */
    class IB {
        public:
            g();
    };

    class B {
        public:
            g() { ... };
    };

    class A {
        public:
            A(shared_ptr<IB> b) : b_(b) {};

            f() { b_->g() };

        private:
            IB b_;
    };


Now we can put a real B into A when we create it in the real code, and a mock B
(which also implements ``IB``) in the test code.

As you can see however, this means writing a lot more code because now there are
these interfaces everywhere, and you need to make separate factory classes to
make all the objects and wire them together, and it all gets very complicated,
just to be able to write a unit test! This is the normal approach in Java, and
one of the reasons that Java programs tends to have so much boilerplate.


Preprocessor-based mocking
--------------------------

In C++, there's another way of doing mocks that avoids all this extra
abstraction, and that is to use the preprocessor. If your C++ code is nicely
organised, then every class is declared in a header (e.g. ``class.hpp``) and
defined in a corresponding source file (``class.cpp``). To compile the program,
each source file is compiled, and then they are all linked together into a
single executable. To use one class from another class, you ``#include`` the
header, which contains all the information needed to use the class.

Now it would be nice if, when building the test, we could just compile as usual
except using a ``mock_class.cpp`` that contains a mock implementation. However,
that's unlikely to work because the mock probably needs different or at least
some extra member variables to store information on how it was called, and those
member variables are in the header. So the header needs to be replaced too.

To make this possible, we make a small modification to ``b.hpp`` to make it look
like this:

.. code-block:: cpp

    #ifdef _MOCK_B_HPP_
    #include _MOCK_B_HPP_
    #else

    class B {
        public:
            g() { ... };
    };

    #endif


When we're compiling the model normally, ``_MOCK_B_HPP_`` is not defined, and
``B`` works normally. When we're compiling the test, we set ``_MOCK_B_HPP_`` to
the name of a header file that declares a mock ``class B`` with a compatible
interface, but with test logic inside of it. The real ``A`` will then be
compiled against the mock ``B``, and linked to the mock ``B`` as well, after
which the test can make an ``A`` and ask the mock ``B`` what ``A`` did.

The tests are not actually built one file at a time. Instead, the test itself is
a program defined in a ``.cpp`` file which includes all the other necessary
code directly. This is somewhat of an ugly hack, and there are corner cases for
which it just plain doesn't work, but the alternative is a very hacky
``Makefile`` to build it all and that's not great either.

If you look at the tests, for example
``src/adhesions/tests/test_adhesion_mover.cpp``, you'll see the following
pattern:

.. code-block:: c++

    // Tell the preprocessor to replace some real files with mocks
    #define _MOCK_ADHESION_INDEX_HPP_ "mock_adhesion_index.hpp"
    ...

    // Now load the real implementations, which will now use the mocks
    #include "adhesion_mover.cpp"
    ...

    // And add the mock implementations
    #include "mock_adhesion_index.cpp"
    ...


When this file is compiled, the preprocessor will first run into the definition
of ``_MOCK_ADHESION_INDEX_HPP_``, which it sets. Then it goes and loads
``adhesion_mover.cpp``, which includes ``adhesion_index.hpp``, so it loads that
as well. However, because ``_MOCK_ADHESION_INDEX_HPP_`` has been set, instead of
taking the real ``AdhesionIndex`` class, it loads ``mock_adhesion_index.hpp``
which contains the mock declaration. Finally, it'll include the mock's
implementation, so that we get this:

.. code-block:: cpp

    // begin adhesion_mover.cpp

        // begin adhesion_mover.hpp
            // real AdhesionMover declaration
        // end adhesion_mover.hpp

        // begin adhesion_index.hpp

            // begin mock_adhesion_index.hpp
                // mock AdhesionIndex declaration
            // end mock_adhesion_index.hpp

            // declaration of real AdhesionIndex omitted
        // end adhesion_index.hpp

        // real AdhesionMover implementation
    // end adhesion_mover.cpp

    // begin mock_adhesion_index.cpp
        // mock AdhesionIndex implementation
    // end mock_adhesion_index.cpp


As you can see, we now have the real ``AdhesionMover`` declaration and
definition, and the mock ``AdhesionIndex``, with only four extra lines added to
``adhesion_index.hpp`` and no other changes to the code.


Including source files (as opposed to headers) directly is pretty much always
evidence of something having gone seriously wrong, but in this case I think it's
justifiable. The alternative would be a very complex make target that needs to
be carefully kept in sync with the test. Including everything means that there's
a nice overview at the top of the file of what is real code under test, and what
has been mocked, and that is easy to modify as needed as tests are added. Things
will break if you have two ``.cpp`` files that declare a local symbol with the
same name, but we don't have any of that here so it all works fine.

