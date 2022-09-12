from re import match

valid_zipcode = lambda zipcode : bool(match("^\d{5}(?:[-\s]\d{4})?$", zipcode))

print(valid_zipcode("48001"))