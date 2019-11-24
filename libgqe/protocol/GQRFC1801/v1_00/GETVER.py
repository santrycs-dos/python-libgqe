"""
GQ-RFC1801 protocol implementation: Command - GETVER

Copyright (c) Bernard Nauwelaerts 2019.
All rights reserved

This program is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; version 2.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program;
if not, write to the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

"""

from libgqe.protocol import Protocol
from libgqe.protocol.GQRFC1201 import GQRFC1201


class GETVER(GQRFC1201):
    """Get hardware model and version"""
    ARGUMENTS = None
    # Todo protocol : needs either terminator or fixed length
    RESPONSE_TYPE = Protocol.Response.Terminator(b'')

    def _parse_response(self, value):
        # Todo parse strings which can be of variable length (plus models)
        mod = value[0:9]
        val = value[9:16]
        return mod.decode(), val.decode()