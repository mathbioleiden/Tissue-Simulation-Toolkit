

#include "vec2.hpp"
#include <deque>

/**
 * @brief Polarity of cell is based on $n$ previous centers of mass (COMs).
 */
class CellPolarity
{
public:
    CellPolarity(int maximum_history)
        :  maximum_history(maximum_history), fixed(false)
    {
    }

    /**
     * @brief Add a COM to the history of the cell.
     * @param COM to be added.
     */
    void add_com(Vec2<double>);

    /**
     * @brief Returns cell polarity based on the maximum_history number of COMs.
     * @return The unit vector in the direction of cell polarisation or
     * zerovector if there is no polarity yet
     */
    Vec2<double> get() const;

    /**
     * @brief set the maximum history
     * @param max_history the maximum history
     */
    void set_maximum_history(int max_history);

    /**
     * @brief Fix the direction of cell polarity. This function deactivates the add_com function.
     * @param direction that should be fixed
     */
    void fix(Vec2<double> direction);

    /**
     * @brief Debugging getter for private data used for testing.
     * @return com_history 
     */
    friend std::deque<Vec2<double>> get_com_history(CellPolarity&);
private:
    int maximum_history;
    std::deque<Vec2<double>> com_history;
    bool fixed;
    Vec2<double> fixed_direction;
};