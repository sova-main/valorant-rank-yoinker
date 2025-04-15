# Changes
1) Added Rank Reveal of all acts i.e Current_Rank|Prev_Rank|Prev_Rank|Prev_Rank|Prev_Rank
2) Added Level Reveal i.e 0 if its hidden. 100 if its not hidden
3) Removed twitch checks and so on.... So, we only have data as follows:
  ```
    Jett - ABCDE#0104 - 69 - A3|Imm1|Imm1|Imm1|A2|A3|Imm2
  ```
4) First Run Game -> Run python main.py
5) If you get error: **Client Activation Error**, then repeat step **3**

# Valorant Rank Yoinker
Find the real username behind all hidden names by bypassing streamer mode, check all possible twitch names and print if a streamer is live


# How to use
**MAKE SURE VALORANT IS OPEN BEFORE RUNNING.** Wait for a game to start, and then names will start printing and being checked. Make sure to adjust your settings.json file to your preferences. You can open this file in any text editor (e.g Notepad).

settings.json:

    - stateInterval: int. change for faster or slower delays between gamestate loop (Slower = less CPU usage. Faster = more CPU usage)

    - twitchReqDelay: int. leave it as is....
    
    - skipTeamPlayers: boolean. leave it as it is.
    
    - skipPartyPlayers: boolean. leave it as it is.


# Regions
The program will ask you for your region. The available regions are NA, EU, LATAM, BR, AP, KR, and PBE. Type the region that you play on. Here is a list of server locations and their respective region: https://support-valorant.riotgames.com/hc/en-us/articles/360055678634-Server-Select

# Is This Bannable
USE AT YOUR OWN RISK. With all programs like this, there is no guarantee that it's safe because using the VALORANT API in this manner is against Riot's Terms of Service. No suspensions have been reported so far from using this program. All things considered, I would use this only on an alt account if you don't want to risk the API abuse account suspension on your main, albeit unlikely.


# License
Copyright (c) 2023 deadly

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
