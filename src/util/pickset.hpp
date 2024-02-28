#include <cstddef>
#include <functional>
#include <random>
#include <unordered_set>
#include <vector>

template <typename T, typename H = std::hash<T>> struct Hasher {
  std::size_t operator()(const T *const pt) const { return H()(*pt); }
};

template <class T, typename H = std::hash<T>> struct EqualTo {
  bool operator()(const T *x, const T *y) const {
    return Hasher<T, H>()(x) == Hasher<T, H>()(x);
  }
};

template <typename T, typename H = std::hash<T>> struct PickSet {

  void rebuildAndReserve() {
    _unorderedSet.clear();
    _unorderedSet.reserve(_vector.capacity());
    for (const T &t : _vector)
      _unorderedSet.insert(&t);
  }

  void insert(const T &t) {
    if (_unorderedSet.find(&t) == _unorderedSet.end()) {
      _vector.push_back(t);

      if (_unorderedSet.find(&(*(_vector.cbegin()))) != _unorderedSet.end()) {
        _unorderedSet.insert(&(*(_vector.crbegin())));
      } else {
        rebuildAndReserve();
      }
    }
  }

  void erase(const T &t) {
    auto fit = _unorderedSet.find(&t);

    if (fit != _unorderedSet.end()) {
      if (*fit != &(*(_vector.crbegin()))) {
        *(const_cast<T *>(*fit)) = *(_vector.rbegin());
      }
      _vector.pop_back();
    }
  }

  int size(const T &t) { return _unorderedSet.size(); }

  const T &pickRandom() const {
    return _vector[_distribution(_generator) % _vector.size()];
  }

  std::unordered_set<const T *, Hasher<T, H>, EqualTo<T, H>> _unorderedSet;
  std::vector<T> _vector;

  static std::default_random_engine _generator;
  static std::uniform_int_distribution<std::size_t> _distribution;
};

template <typename T, typename H>
std::default_random_engine
    PickSet<T, H>::_generator = std::default_random_engine();

template <typename T, typename H>
std::uniform_int_distribution<std::size_t>
    PickSet<T, H>::_distribution = std::uniform_int_distribution<std::size_t>();
