def calculate_statistics(incidents):

    total = len(incidents)

    high = len([
        i for i in incidents
        if i["severity"] == "HIGH"
    ])

    medium = len([
        i for i in incidents
        if i["severity"] == "MEDIUM"
    ])

    low = len([
        i for i in incidents
        if i["severity"] == "LOW"
    ])

    return {
        "total": total,
        "high": high,
        "medium": medium,
        "low": low
    }
