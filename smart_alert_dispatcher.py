from security_logging_service import logger

def dispatch_alert(alert_type, severity):

    logger.warning(
        f"ALERT GENERATED: {alert_type} severity={severity}"
    )

    return {
        "alert_dispatched": True,
        "severity": severity
    }
