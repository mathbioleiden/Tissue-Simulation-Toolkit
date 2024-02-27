template <class T> class Edges {
public:
  const std::array<int, 4> &operator[](unsigned index) const {
    return edgemap[edgeVector[index]];
  }
  std::array<int, 4> &operator[](unsigned index) {
    return edgemap[edgeVector[index]];
  }

  void insert(std::array<int, 4> edge) {
    std::pair<iterator, bool> insertion =
        edgemap.insert(edge, edgevector.size()) if (insertion->second) {
      edgevector.push_back(insertion->first);
    }
  }
  void erase(std::array<int, 4> edge) {
    try {
      index = edgemap.at(edge);
      // std::unordered_map<std::array<int,4>,int>::iterator last_it =
      // edgevector
      edgevector.swap(index, edgevector.size() - 1);
      edgemap[egdevector[index]] = index;
    } catch (const std::out_of_range &oor) {
    }
  }
  unsigned size_map() const { return edgemap.size(); }
  unsigned size_vector() const { return edgevector.size(); }

private:
  std::unordered_map<std::array<int, 4>, int> edgemap;
  std::vector<std::unordered_map<std::array<int, 4>, int>::iterator> edgevector;
};
