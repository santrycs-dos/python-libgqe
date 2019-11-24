"""
GQ-RFC1701 protocol v2.00 implementation

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
from libgqe.protocol.GQRFC1701.v1_00 import V1_00
from libgqe.protocol.GQRFC1701.v1_00 import GETVER, GETSERIAL, POWER, REBOOT, GETGYRO, SPEAKER, GETVOLT, ECHO
from libgqe.protocol.GQRFC1701.v1_00 import KEY, KEYHOLD, GETMODE, GETSCREEN, GETEMF, GETEF, GETRF, RESETRFPEAK
from libgqe.protocol.GQRFC1701.v1_00 import GETCFG, ECFG, WCFG, CFGUPDATE, FACTORYRESET
from libgqe.protocol.GQRFC1701.v1_00 import SETDATEYY, SETDATEMM, SETDATEDD, SETTIMEHH, SETTIMEMM, SETTIMESS
from libgqe.protocol.GQRFC1701.v1_00 import GETDATETIME, SETDATETIME
from libgqe.protocol.GQRFC1701.v1_00 import SPIR, SPIE
from libgqe.protocol.GQRFC1701.v1_00 import GETBANDDATA, SETSPECTRUMBAND

__all__ = [
    # Parent Classes
    "Protocol", "V2_00",
    # Commands
    "GETVER", "KEY", "KEYHOLD", "GETEMF", "GETEF", "GETBANDDATA", "GETMODE", "GETSCREEN",
    "GETCFG", "ECFG", "WCFG", "GETSERIAL", "POWER", "CFGUPDATE",
    "SETDATEYY", "SETDATEMM", "SETDATEDD", "SETTIMEHH", "SETTIMEMM", "SETTIMESS", "GETDATETIME", "SETDATETIME",
    "FACTORYRESET", "REBOOT",
    "GETGYRO", "SPEAKER", "GETVOLT", "ECHO",
    "SPIR", "SPIE", "GETRF", "SETSPECTRUMBAND", "RESETRFPEAK",
    "GETXYZ", "RESETBANDDATA", "GETSPECTRUMFULLSCANFLAG"
]


class V2_00(V1_00):
    """ Added GETXYZ, RESETBANDDATA and GETSPECTRUMFULLSCANFLAG """
    def __init__(self, *args, **kwargs):
        V1_00.__init__(self, *args, **kwargs)
        # print("Initializing protocol version {}".format('V2_00'))