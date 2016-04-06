# -*- coding: utf-8 -*-


def state_str(domain):
    states = [
        "Unknown",
        "Running",
        "Blocked",
        "Paused",
        "In Shutdown",
        "Shut off",
        "Crashed",
        "PM Suspended"]

    return states[domain.state()[0] or 0]
