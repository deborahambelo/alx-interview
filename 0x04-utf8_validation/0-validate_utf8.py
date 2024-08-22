def validUTF8(data):
    """Checks if a given list of integers data set represents a valid UTF-8 encoding."""
    
    def is_continuation(byte):
        """Check if a byte is a continuation byte (starts with 10)."""
        return (byte & 0b11000000) == 0b10000000

    i = 0
    while i < len(data):
        # Consider only the 8 least significant bits
        first_byte = data[i] & 0xFF
        
        if first_byte >> 7 == 0:  # 1-byte character
            i += 1
        elif first_byte >> 5 == 0b110:  # 2-byte character
            if i + 1 >= len(data) or not is_continuation(data[i+1] & 0xFF):
                return False
            i += 2
        elif first_byte >> 4 == 0b1110:  # 3-byte character
            if i + 2 >= len(data) or not is_continuation(data[i+1] & 0xFF) or not is_continuation(data[i+2] & 0xFF):
                return False
            i += 3
        elif first_byte >> 3 == 0b11110:  # 4-byte character
            if i + 3 >= len(data) or not is_continuation(data[i+1] & 0xFF) or not is_continuation(data[i+2] & 0xFF) or not is_continuation(data[i+3] & 0xFF):
                return False
            i += 4
        else:
            return False
    
    return True
