# **NuggetNet Server - Technical Overview and Design**

## **1. Purpose:**

To develop a server for the digital trading game **NuggetNet** that simulates an '80s style online trading platform. The primary goals are to highlight the outcomes of a deregulated market, with satirical overtones, and create an engaging player experience.

## **2. Server Architecture and Framework:**

- **Language:** Python
- **Asynchronous Framework:** Twisted
    * Handles a large number of concurrent connections and manages server-client interactions.
- **Task Queue:** Celery 
    * To manage tasks that can be deferred, like sending in-game mail or processing queued transactions.

## **3. Connection Interfaces:**

1. **Terminal Access over TCP/IP:** 
    * Resembling a classic BBS. This will be the primary interface for the players, ensuring compatibility with retro computer systems and standard terminals.
    * Custom client development is not required.
  
2. **Administrative Interface:** 
    * Will enable starting, stopping, and pausing the simulation, as well as viewing game metrics in real-time. It could be combined with the primary interface initially.
  
3. **Atari 8-bit Custom Client:** 
    * To be developed at a later stage. Will leverage the graphics capabilities of the Atari 8-bit home computers to create an '80s-style home trading environment.

## **4. Game Mechanics:**

- **Trading Environment:** Loosely-regulated with near-zero oversight, encouraging players to explore and exploit market inefficiencies.
- **Player Communication:** Via an in-game inbox system. Simulates '80s style online communication platforms.
- **Market Operations:**
    * Dynamic trading hours to simulate real-world trading hours and promote active gameplay. Configurable market hours with multiple sessions are in consideration.
    * Plans for a "reduced activity session" to mimic real-world post-market hours. Detailed mechanics pending.
- **Collusion Policy:** Players can form alliances, making gameplay more dynamic. However, self-collusion (e.g., multi-accounting) is discouraged.

## **5. Game Duration:**

- Games will have a fixed duration. Players will be made aware of the end-date. Reminders will be sent to the player's in-game inbox.

## **6. Development Roadmap:**

- **Phase 1:** Development of server internals while focusing on the terminal-based client interface.
- **Phase 2:** Integration of administrative controls and metrics viewing.
- **Phase 3:** Development of the Atari 8-bit client.
