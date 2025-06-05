import ipaddress

def lookup_country(ip: str) -> str:
    """Return a dummy country code for an IP address."""
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return "Unknown"
    # Dummy logic: categorize by first octet
    first_octet = int(ip.split('.')[0])
    if 0 <= first_octet <= 126:
        return "US"
    elif 128 <= first_octet <= 191:
        return "EU"
    else:
        return "APAC"
