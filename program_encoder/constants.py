import re

# label regex for line label or goto target
GENERIC_LABEL = r"[A-E]\d*"

# label group in square brackets
LINE_LABEL = fr"(?:\[(?P<LABEL>{GENERIC_LABEL})\])"

# label group for goto target
TARGET_LABEL = fr"(?P<TARGET>{GENERIC_LABEL})"

# variable group
VAR = r"(?P<VAR>(Y|[XZ]\d*))"

# backreference to VAR capture group
VAR_BACKREF = r"(?P=VAR)"

# assignment operator
ASSIGNMENT = r"(?:←|<-?|<?=)"

# inequality operator
NEQ = r"(?:≠|!=|=/=)"

# NOOP - groups: LABEL, VAR
NOOP_REGEX = re.compile(
	fr"^\s*{LINE_LABEL}?\s*{VAR}\s*{ASSIGNMENT}\s*{VAR_BACKREF}\s*$"
)

# ADD - groups: LABEL, VAR
ADD_REGEX = re.compile(
	fr"^\s*{LINE_LABEL}?\s*{VAR}\s*{ASSIGNMENT}\s*{VAR_BACKREF}\s*[+]\s*1\s*$"
)

# MINUS - groups: LABEL, VAR
MINUS_REGEX = re.compile(
	fr"^\s*{LINE_LABEL}?\s*{VAR}\s*{ASSIGNMENT}\s*{VAR_BACKREF}\s*[-∸−]\s*1\s*$"
)

# GOTO - groups: LABEL, VAR, TARGET
GOTO_REGEX = re.compile(
	fr"^\s*{LINE_LABEL}?\s*IF\s+{VAR}\s*{NEQ}\s*0\s+GOTO\s+{TARGET_LABEL}\s*$"
)
