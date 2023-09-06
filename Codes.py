from enum import Enum

# Author: Thomas Pelegrin
# date: 11/27/2022
class Codes( Enum ):
    """ Represents the various codes used in the P2P messages """
    ERROR = 0       
    PEER = 1        # peer request
    FIND = 2        # find file request
    FOUND = 3       # found file
    GET = 4         # get (download) file request
    READY = 5       # ready to download file
    SEND = 6        # sending file
    QUIT = 7