# Dingdong's Notes

## 1. Function change

### Solving
* AI thoughts generation 
  * [solved] happens in `katrain/core/ai.py`. 
    * There is a function called `generate_helper_advice` in line 527.
    * However, it seems the match analysis didn't happen in `generate_helper_advice` function. So try to trace where this function is called.
    * Seems like `cn = game.current_node` is already analyzed when `generate_helper_advice` is called.
    * Failed to track further.
  * How to get match information? How to get board. information?
  * [Partially] How to display to GUI?
    * Register a node in `cn`? Will it display some information?
    * [solved] Check `cn.ai_thoughts`, checking as follows
      * Tried to find what is a `node` in `cn`, success. Node is defined in `katrain/core/game_node.py`, line 38. It is described as a `SGFNode` node with one or more moves.
      * Found that `GameNode` class in `katrain/core/game_node.py` was modified to include more attributes. They were noted by `CirF`.
    * [solved] Check `cn.advice`, checking as follows
      * Used in `comment` function in `katrain/core/game_node.py` line 350.
      * no further reference in GUI, etc.
    * [success!] Try to display one more string in GUI.
      * Define one string `self.cost_notification` in `GameNode` class. Add it in `GameNode.comment()`.
      * It is shown in the GUI!
* Communication with `KataGo` server.
  * There is a `engine.py` file which includes `KataGoEngine` class.
  * Tracking `engine.request_analysis`. 
    * It is called in `katrain/core/ai.py` line 248. Warped as member function`request_ai_analysis()`. But is never called in our workflow.
    * Also in `katrain/core/game_node.py` and warped as member function `analysis()`. But is called everywhere and I'm not sure what is the worflow.
  * Found that `engine` is an attribute in Game class
    * Question: what is the node passed into "request analysis"?
    * Question: where is the `engine` instantiated?
* Check `generate_helper_advice()` by CirF.
  * [solved] `generate_helper_advice()` is called in `__main__.py`, warped in `_do_advice` function.
  * The `self._do_advice` is called only once.

* Question: what is the `mainloop()`?
  * The game will run the `start()` function in mainloop only once.
  *  How is `KataGo` server instantiated?
     *  In `start()` function in mainloop.
*  About `KataGo` server.
   *  In `katrain/core/engine.py`, there is a function called `send_query`, which put the query into a queue called `self.write_queue`.
   *  In the `KataGoEngine.request_analysis()`, `send_query` is called. Here board information is collected from game and passed into 
* [Question] A new Game is constructed at when? Solved. Only once in mainloop
* How is analysis received.
  * In node level. There is a set of functions from `set_analysis` to `update_move_analysis`.
## Implementation Idea

### Basic Idea
1. There is a `Game` object passed everywhere. It contains `self.engine` object, which is a running `KataGo` server. We can request the `KataGo` server to do analysis.
2. There are 3 costs and 1 benifits in the design. 
   1. [NOT_CLEAR] Intervention Cost is independent of the step evaluation. We only need to now what is the place a player plays and whether it is the same as AI's suggestion.
   2. [CLEAR] Cognititive Depth is the number of visits that an AI did to perform analysis. (It is a good indicator of how much time the AI spent on the analysis.) I can do this by extracting the information from `GameNode` class.
      1. Use the response field `moveInfos.visits`: `visits` - The number of visits invested into the move, according to GitHub: https://github.com/lightvector/KataGo/blob/master/docs/Analysis_Engine.md
   3. [CLEAR] Idea Difference. May need to call the analysis engine one more time. Equation: gain_by_next_human_move - gain_by_next_ai_move.
3. Problem: 
   1. How to get human's next step?


Join Zoom Meeting
https://hkust.zoom.us/j/93868940901

Meeting ID:  938 6894 0901

---

One tap mobile
+12532158782,,93868940901# US (Tacoma)
+13017158592,,93868940901# US (Washington DC)

---

Dial by your location
• +1 253 215 8782 US (Tacoma)
• +1 301 715 8592 US (Washington DC)
• +1 305 224 1968 US
• +1 309 205 3325 US
• +1 312 626 6799 US (Chicago)
• +1 346 248 7799 US (Houston)
• +1 360 209 5623 US
• +1 386 347 5053 US
• +1 507 473 4847 US
• +1 564 217 2000 US
• +1 646 558 8656 US (New York)
• +1 646 931 3860 US
• +1 669 444 9171 US
• +1 669 900 9128 US (San Jose)
• +1 689 278 1000 US
• +1 719 359 4580 US
• +1 253 205 0468 US

Meeting ID:  938 6894 0901

Find your local number: https://hkust.zoom.us/u/axTfOgsuJ

---

Join by SIP
• 93868940901@zoomcrc.com

---

Join by H.323
• 162.255.37.11 (US West)
• 162.255.36.11 (US East)
• 221.122.88.195 (China)
• 115.114.131.7 (India Mumbai)
• 115.114.115.7 (India Hyderabad)
• 213.19.144.110 (Amsterdam Netherlands)
• 213.244.140.110 (Germany)
• 103.122.166.55 (Australia Sydney)
• 103.122.167.55 (Australia Melbourne)
• 209.9.211.110 (Hong Kong SAR)
• 149.137.40.110 (Singapore)
• 64.211.144.160 (Brazil)
• 149.137.68.253 (Mexico)
• 69.174.57.160 (Canada Toronto)
• 65.39.152.160 (Canada Vancouver)
• 207.226.132.110 (Japan Tokyo)
• 149.137.24.110 (Japan Osaka)

Meeting ID:  938 6894 0901



