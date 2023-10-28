template <typename T>
Muscle3Grid<T>::Muscle3Grid(libmuscle::DataConstRef const & data) {
    if (!data.is_a_grid_of<T>())
        throw std::runtime_error(
                std::string("Expected to receive a grid of type ")
                + typeid(T).name() + ", but received something else");
    shape_ = data.shape();
    strides_ = std::vector<std::size_t>(shape_.size());

    if (data.storage_order() == libmuscle::StorageOrder::first_adjacent) {
        strides_[0] = 1u;
        for (std::size_t i = 1u; i < strides_.size(); ++i)
            strides_[i] = strides_[i - 1u] * shape_[i - 1u];
    }
    else {
        strides_[strides_.size() - 1u] = 1u;
        for (std::size_t i = strides_.size() - 1u; i > 0u; --i)
            strides_[i - 1u] = strides_[i] * shape_[i];
    }

    elements_ = data.elements<T>();
}


template <typename T>
std::size_t Muscle3Grid<T>::shape(std::size_t i) const {
    return shape_.at(i);
}


template <typename T>
T Muscle3Grid<T>::operator()(std::size_t i0) const {
    if (strides_.size() != 1u)
        throw std::runtime_error(
                "Expected a 1D grid, but this one has " +
                std::to_string(strides_.size()) + " dimensions");
    return elements_[i0];
}


template <typename T>
T Muscle3Grid<T>::operator()(std::size_t i0, std::size_t i1) const {
    if (strides_.size() != 2u)
        throw std::runtime_error(
                "Expected a 2D grid, but this one has " +
                std::to_string(strides_.size()) + " dimensions");
    return elements_[i0 * strides_[0u] + i1 * strides_[1u]];
}

