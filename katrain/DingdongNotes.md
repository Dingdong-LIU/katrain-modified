# Dingdong's Notes

## 1. Function change

### Solving
* AI thoughts generation 
  * [solved] happens in `katrain/core/ai.py`. 
    * There is a function called `generate_helper_advice` in line 527.
  * How to get match information? How to get board information?
  * [Partially] How to display to GUI?
    * Register a node in `cn`? Will it display some information?
    * [solved] Check `cn.ai_thoughts`, checking as follows
      * Tried to find what is a `node` in `cn`, success. Node is defined in `katrain/core/game_node.py`, line 38. It is discribed as a SGFNode node with one or more moves.
      * Found that `GameNode` class in `katrain/core/game_node.py` was modified to include more attributes. They were noted by `CirF`.
    * [solved] Check `cn.advice`, checking as follows
      * Used in `comment` function in `katrain/core/game_node.py` line 350.
      * no further reference in GUI, etc.
    * [success!] Try to display one more string in GUI.
      * Define one string `self.cost_notification` in `GameNode` class. Add it in `GameNode.comment()`.
      * It is shown in the GUI!
* Communication with KataGo server.
  * There is a `engine.py` file which includes `KataGoEngine` class.
* Check `generate_helper_advice()` by CirF.
  * [solved] `generate_helper_advice()` is called in `__main__.py`, warped in `_do_advice` function.
  * The `self._do_advice` is called only once.

