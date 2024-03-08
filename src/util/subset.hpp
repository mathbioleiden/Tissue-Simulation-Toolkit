template <class T> class SubsetVector {
private:
  struct Entry {
    T element;
    int index_in_subset = -1;
  };

public:
  explicit SubsetVector(unsigned size = 0) : m_entries(size) {
    m_subset_indices.reserve(size);
  }

  void push_back(const T &element) { m_entries.push_back(Entry{element, -1}); }
  const T &operator[](unsigned index) const { return m_entries[index].element; }
  T &operator[](unsigned index) { return m_entries[index].element; }

  void insert_in_subset(unsigned index) {
    if (m_entries[index].index_in_subset < 0) {
      m_entries[index].index_in_subset = m_subset_indices.size();
      m_subset_indices.push_back(index);
    }
  }
  void erase_from_subset(unsigned index) {
    if (m_entries[index].index_in_subset >= 0) {
      auto subset_index = m_entries[index].index_in_subset;
      auto &entry_to_fix = m_entries[m_subset_indices.back()];
      std::swap(m_subset_indices[subset_index], m_subset_indices.back());
      entry_to_fix.index_in_subset = subset_index;
      m_subset_indices.pop_back();
      m_entries[index].index_in_subset = -1;
    }
  }
  unsigned subset_size() const { return m_subset_indices.size(); }
  T &subset_at(unsigned subset_index) {
    auto index = m_subset_indices.at(subset_index);
    return m_entries.at(index).element;
  }
  const T &subset_at(unsigned subset_index) const {
    auto index = m_subset_indices.at(subset_index);
    return m_entries.at(index).element;
  }

private:
  std::vector<Entry> m_entries;
  std::vector<unsigned> m_subset_indices;
};
