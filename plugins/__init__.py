#!/usr/bin/env python3
# Copyright (C) @ZauteKm
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .utils import (
   get_filter_results,
   get_file_details,
   is_subscribed,
   get_poster,
   Media
)
from .channel import (
   RATING,
   GENRES
)

HELP = """
**💢 Q & A 💢**

Q : මොකක්ද්ද මෙ බොට්ගෙන් වෙන්නෙ?
A : ඔයාට ඔනෙ සින්හල Subtitle එකක් Inline ක්‍රමයට හෝ Film එකෙ හෝ සීරීස් එකෙ නම බොට්ට ලබාදීමෙන් Subtitle File එක ලබාගන්න පුළුවන්. 😺
    
Q : කොහොමද ලෙසියෙන්ම Subtitle File එකක් බොට්ගෙන් ගන්නෙ?
A : ඔයාට කරන්න තියෙන්නෙ ඔයාට ඔනෙ Film Or  Series එකෙ හරි නම බොට්ව Start කරලා දාන්න විතරයි. එතකොට බොට් ඒ Film එකට හෝ සීරීස් එකට අදාල Subtitles ෆයිල් එක හොයලා දෙනවා. 😊

Q : කොහොමද Inline ක්‍රමයට Subtitle File එක ගන්නෙ?
A : බොට්ව Start කරාම ප්‍රදාන මෙනුවේ ඇති " සොයන්න 🔎 " 
කියන Button එක ටච් කරලා එන Option එකෙන් ඔනෙ Subtitle ෆයිල් එක ගන්න පුළුවන්. ඔයා මෙ Option එක වැඩිය දන්නෙ නැත්නම් ෆිල්ම් එකෙ නම විතරක් බොට්ට දාන්න. 🐦🐦 (මෙ Option එක Use කරනවනම් හරි නම විතරක්ම ඇතුලත් කරන්න වෙන මොකුත් නැතිව.)

වැඩි විස්තර සදහා අපෙ [Telegram Discussion Group](T.ME/MPMCHATZONE) එකට Join වෙන්න.

"""

ABOUT = """
**💃 About Bot 💃**

**▷🤖 Name: Sinhala Subtitles bot
    
▷👨‍💻 Creator : [MPM](https://t.me/Whtsappgang)

▷🌏 Language : Python3

▷🌱Database : MongoDB

▷♻️ Library : Pyrogram Asyncio 1.13.0**
"""
