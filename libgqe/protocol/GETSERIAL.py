"""
GQ-RFC protocols implementation: Command - GETSERIAL

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


class GETSERIAL(Protocol):
    """ Get serial number """
    ARGUMENTS = None
    RESPONSE_TYPE = Protocol.Response.Bytes(7)

    def _parse_response(self, value):
        r = ''
        for b in bytearray(value):
            r += "{:0>2x}".format(b)
        return r
