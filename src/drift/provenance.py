"""Ordered provenance selection under the user-amended public-proxy rules."""
def select_source(candidates, menagerie_timestamp, pinned=None):
    if pinned:
        return {"method": "pinned", "confidence": "high", "candidate": pinned}
    matched = [c for c in candidates if c.get("matches") and not c.get("error")]
    dated = [c for c in matched if int(c["timestamp"]) <= int(menagerie_timestamp)]
    if dated:
        return {"method": "dated match", "confidence": "medium", "candidate": max(dated, key=lambda c: int(c["timestamp"]))}
    if any(c.get('history_incomplete') for c in candidates):
        return {"method":"unknown","confidence":"incomplete","candidate":None}
    # A proxy is permitted only when public history has no pre-conversion revision.
    if matched and not any(not c.get('deleted') and int(c["timestamp"]) <= int(menagerie_timestamp) for c in candidates):
        return {"method": "proxy", "confidence": "low", "candidate": min(matched, key=lambda c: int(c["timestamp"]))}
    if matched:
        return {'method':'unknown','confidence':'unclassified','candidate':None,
                'reason':'Matching revisions exist only after Menagerie, while older public nonmatching revisions exist; the specified proxy rule does not apply'}
    if any(c.get('error') for c in candidates):
        return {"method": "unknown", "confidence": "incomplete", "candidate": None}
    return {"method": "none", "confidence": "none", "candidate": None}


def class_with_provenance(m, s, h, quantity, method, tolerances, documented=False):
    from .compare import classify
    if method == "none":
        return "NO MATCHING SOURCE"
    value = classify(m, s, h, quantity, tolerances, documented)
    return value + " (inferred)" if method == "proxy" else value
